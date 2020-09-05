# 1. Implement Original Lesk algorithm with the help of a function that computes the score for two 
# given glosses. For a given text and a given word, try to find the sense of that word, considering 
# the Lesk measure. Check your result with the already implemented (simplified) lesk algorithm in 
# nltk. You may have different results, as the simplified Lesk algorithm compares the target word 
# glosses with the words from the context (not their definitions).
def get_context(sentence):
    sentence_split = nltk.word_tokenize(sentence.lower())    
    only_words = [word.lower() for word in sentence_split if word.isalnum()]
    relevant_words = [word for word in only_words if word not in stopwords.words('english')]
    return relevant_words

def simplified_lesk(sentence, word, part_of_speech):
    best_sense = ""
    max_overlap = 0
    context = get_context(sentence)
    for synset in wordnet.synsets(word):
        if (str(synset.pos()) == part_of_speech):
            overlap = 0
            split_def = synset.definition().split(' ')
            polished_def = [word for word in split_def if word not in stopwords.words('english')]

            intersection = get_intersection(context, polished_def)
            overlap += len(intersection)

            for example in synset.examples():
                example_context = get_context(example)
                example_intersection = np.intersect1d(context, example_context)

                overlap += len(example_intersection)
            if (overlap > max_overlap):
                max_overlap = overlap
                best_sense = synset
    return (best_sense)

def get_intersection(gloss1, gloss2):
    return np.intersect1d(gloss1, gloss2)
    
    
# 2. Implement extended Lesk algorithm. For a list of 7-10 words, print the measure for each pair of 
# words (without repeating the words). Just like in the former exercise, try to obtain the word sense 
# for the given text and word. Can you find a text and word where simple Lesk gives the wrong answer, 
# however extended Lesk gives the right answer?

def extended_lesk(word1, word2):
    # call compute score on each word. Didn't get to finish it
    # but the compare function is done
    return 0

def compute_score(syn1, syn2):
    syn1 = wordnet.synsets(syn1)[0]
    syn2 = wordnet.synsets(syn2)[0]
    syn1_all = return_all(syn1)
    syn2_all = return_all(syn2)
    common = longest_common_sentence(syn1_all, syn2_all)
    common_all = ""
    score = 0
    i = 0
    while(len(common) > 0 and i < 5):
        if (common_all.find(common) == -1):
            print("da")
            score += len(common)
            common_all += common
        syn1_all.replace(common, '')
        syn2_all.replace(common, '')
        common = longest_common_sentence(syn1_all, syn2_all)
        i += 1
        print("common_all", common_all)
    print("common", common)
    print("Syn1", syn1_all)
    print("common_all", common_all)
        
    

def return_all(synset):
    syn_all = ""
    for hyp in synset.hypernyms():
        syn_all += " " + hyp.definition().lower()
    for hyp in synset.hyponyms():
        syn_all += " " + hyp.definition().lower()
    for hyp in synset.part_meronyms():
        syn_all += " " + hyp.definition().lower()
    for hyp in synset.substance_meronyms():
        syn_all += " " + hyp.definition().lower()
    for hyp in synset.member_meronyms():
        syn_all += " " + hyp.definition().lower()
    for hyp in synset.similar_tos():
        syn_all += " " + hyp.definition().lower()
    for hyp in synset.also_sees():
        syn_all += " " + hyp.definition().lower()
    return syn_all

### taken from stackoverflow
def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
            if m[x][y] > longest:
                longest = m[x][y]
                x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

def longest_common_sentence(s1, s2):
    s1_words = s1.split(' ')
    s2_words = s2.split(' ')  
    return ' '.join(longest_common_substring(s1_words, s2_words))


#nu am apucat sa implementez si functia cu cele 2 cuvinte

