from nltk.corpus import wordnet

# 1. Create a function that receives a word and prints the 
# associated glosses for all the possible senses of that word 
# (you must find all its corresponding synsets and print the gloss 
# for each).

def print_gloss(word):
    for synset in wordnet.synsets(word):
        print (synset.definition())
        
print_gloss('school')

# 2. Create a function that receives two words as parameters. 
# The function will check, using WordNet if the two words can be 
# synonyms (there is at least one synset that contains the two 
# words).If such synset is found, print the gloss for that synset.
def print_if_synonyms(word1, word2):
    for synset1 in wordnet.synsets(word1):
        for synset2 in wordnet.synsets(word2):
            if (synset1 == synset2):
                print (synset1.name())
                print ("", synset1.definition())

print_if_synonyms('soil', 'dirt')


# 3. Create a function that receives a synset object and returns 
# a tuple with 2 lists. The first list contains the holonyms 
# (all types of holonyms) and the second one the meronyms 
# (all types). Find a word that has either holonyms or meronyms 
# of different types. Print them separately (on cathegories of 
# holonyms/meronyms) and then all together using the created 
# function (in order to check that it prints them all).

def get_holo_mero(synset):
    holonyms = []
    meronyms = []
    holonyms += synset.substance_holonyms()
    holonyms += synset.part_holonyms()
    holonyms += synset.member_holonyms()
    
    meronyms += synset.substance_meronyms()
    meronyms += synset.part_meronyms()
    meronyms += synset.member_meronyms()
    
    return (holonyms, meronyms)

# testing: root has substance_meroynms as well as part_meronyms. Seems to work fine.

sn = wordnet.synsets('root')[0]

print(sn.substance_holonyms())
print(sn.part_holonyms())
print(sn.member_holonyms())

print(sn.substance_meronyms())
print(sn.part_meronyms())
print(sn.member_meronyms())

x = get_holo_mero(sn)

print (x)


# 4. Create a function that for a given synset, prints the path 
# of hypernyms (going to the next hypernym, and from that hypernym 
# to the next one and so on, until it reaches the root).
sn = wordnet.synsets('woman')[0]
# I print the names of the synsets. Remove ".name()" for complete synset output
def parse_hypernyms(synset):
    print(synset.name())
    for hypernym in synset.hypernyms():
        print("", hypernym.name())
        spacing = " "
        while len(hypernym.hypernyms()) > 0:
            hypernym = hypernym.hypernyms()[0]
            print (spacing, hypernym.name())
            spacing += " "
        
parse_hypernyms(sn)

# 5. Create a function that receives two synsets as parameters. We consider d1(k) the length of 
# the path from the first word to the hypernym k (the length of the path is the number of hypernyms 
# it goes through, to reach k) and d2(k) the length of the path from the second word to the hypernym 
# k. The function will return the list of hypernyms having the property that d1(k)+d2(k) is minimum 
# (there can be multiple hypernyms with this property ; all having equal distances that are this 
# minimum number; you must print them all).
path_sn_1 = []
path_sn_2 = []

def find_all_paths(target_synset, current_synset, current_path, path, other_path):
    if (target_synset == current_synset):
        path.append(current_path)
        return 1
    else:
        other_path.append(current_path)
    
    initial_path = current_path.copy()
    for hypernym in current_synset.hypernyms():
        current_path.append(hypernym)
        find_all_paths(target_synset, hypernym, current_path, path, other_path)
        current_path = initial_path

def find_shortest_path(synset1, synset2):
    shared_hypernyms = sn_1.lowest_common_hypernyms(sn_2)
    for hypernym in shared_hypernyms:
        find_all_paths(hypernym, sn_1, [sn_1], path_sn_1, path_sn_2)
        find_all_paths(hypernym, sn_2, [sn_2], path_sn_2, path_sn_1)
    print("Shared hypernyms:", shared_hypernyms)
    
    min_distance = -1
    min_d1 = []
    min_d2 = []
    min_path_1 = []
    min_path_2 = []
    for path_1, path_2 in zip(path_sn_1, path_sn_2):
        d1 = len(path_1)
        d2 = len(path_2)
        if (min_distance > (d1 + d2) or min_distance == -1):
            min_distance = d1 + d2
            
    
    for path_1, path_2 in zip(path_sn_1, path_sn_2):
        d1 = len(path_1)
        d2 = len(path_2)
        if (d1 + d2 == min_distance and (path_1 not in min_path_1 or path_2 not in min_path_2)):
            min_d1.append(d1)
            min_d2.append(d2)
            min_path_1.append(path_1)
            min_path_2.append(path_2)

    for i in range(len(min_path_1)):
        print("d1(k) =", min_d1[i])
        print("d2(k) =",  min_d2[i])
        print("d1(k) + d2(k) =", min_d1[i] + min_d2[i])
        print(min_path_1[i])
        print(min_path_2[i])
    
    return min_path_1, min_path_2

sn_1 = wordnet.synset('tree.n.01')
sn_2 = wordnet.synset('tower.n.01')

find_shortest_path(sn_1, sn_2)


# 6. Create a function that receives a synset object and a list of synsets (the list must contain at 
# least 5 elements). The function will return a sorted list. The list will be sorted by the 
# similarity between the first synset and the synsets in the list. For example (we consider we take 
# the firs synset for each word) we can test for the word cat and the list: animal, tree, house, 
# object, public_school, mouse.
def get_similiarity(synset, synsets):
    # a list where we associate a similarity value for each synset from the list
    similarity = []
    for sn in synsets:
        similarity.append(synset.path_similarity(sn))
        # I've also used Wu-Palmer Similarity, which yields different results (but similar). I've decided to stick with the one provided in the lab, tho'.
        # similarity.append(synset.wup_similarity(sn))
    # sorting the initial list based on the similarity list
    returned_list = [sn for _,sn in sorted(zip(similarity, synsets), reverse=True)]
    return returned_list

sn = wordnet.synsets('cat')[0]
sn_list = [wordnet.synsets('cat')[0], wordnet.synsets('animal')[0], wordnet.synsets('tree')[0], wordnet.synsets('dog')[0], wordnet.synsets('house')[0], wordnet.synsets('object')[0], wordnet.synsets('public_school')[0]]
print(get_similiarity(sn, sn_list))


# 7. Create a function that checks if two synsets can be indirect meronyms for the same synset. 
# An indirect meronym is either a part of the givem element or a part of a part of the given element 
# (and we can exten this relation as being part of part of part of etc....). This applies to any type 
# of meronym.
index = 0
sn_1 = wordnet.synset('hand.n.01')
sn_2 = wordnet.synset('leg.n.01')
sn_1_meronyms = [sn_1]
sn_2_meronyms = [sn_2]

def get_all_meronyms(meronyms, index):
    if (index >= len(meronyms)):
        return 1
    
    for meronym in meronyms[index].substance_meronyms():
        if (meronym not in meronyms):
            meronyms.append(meronym)
    
    for meronym in meronyms[index].part_meronyms():
        if (meronym not in meronyms):
            meronyms.append(meronym)
            
    for meronym in meronyms[index].member_meronyms():
        if (meronym not in meronyms):
            meronyms.append(meronym)
            
    get_all_meronyms(meronyms, index + 1)

get_all_meronyms(sn_1_meronyms, 0)
get_all_meronyms(sn_2_meronyms, 0)
# print(sn_1_meronyms)
# print(sn_2_meronyms)


def intersection(list1, list2): 
    aux = set(list2) 
    list3 = [value for value in list1 if value in aux] 
    return list3

intersection = intersection(sn_1_meronyms, sn_2_meronyms)
if (intersection != []):
    print ("Yes, they have the following meronyms in common:", intersection)
else:
    print("The two synsets have no meronyms in common.")    


# 8. Print the synonyms and antonyms of an adjective (for example, "beautiful"). If it's polisemantic,
# print them for each sense, also printing the gloss for that sense (synset).
def syn_ant(word):
    synonyms = []
    antonyms = []
    for synset in wordnet.synsets(word):
        print ("Word:", word)
        print ("Meaning:", synset.definition())
        for lemma in synset.lemmas():
            if (lemma.name().lower() != word.lower()):
                synonyms.append(lemma.name())
            for antonym in lemma.antonyms():
                if (antonym.name().lower() != word.lower()):
                    antonyms.append(antonym.name())
            
        print ("Synonyms:", synonyms)
        synonyms = []
        print ("Antonyms:", antonyms)
        antonyms = []
        print("")
        
syn_ant("worse")


