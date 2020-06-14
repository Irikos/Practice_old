import requests
import nltk
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import numpy as np
from nltk.wsd import lesk
import itertools
wnl = WordNetLemmatizer()

# it has some errors, doesn't work

def wikipedia_disambiguation(page_title):
    disambiguation = [page_title]
    #create a connection(session)
    r_session = requests.Session()

    #url for the MediaWiki action API
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query", #we are creating a query
        "titles": "soda", #for the title car    
        "prop": "redirects", #asking for all the redirects (to the title car)
        "format": "json" #and we want the output in a json format
    }

    #we obtain the response to the get request with the given parmeters
    query_response = r_session.get(url=URL, params=PARAMS)
    json_data = query_response.json()
    print()
    wikipedia_pages = json_data["query"]["pages"]
    #we iterate through items and print all the redirects (their title and id)
    try:
        for k, v in wikipedia_pages.items():
            for redir in v["redirects"]:
                print("{} redirect to {}({})".format(redir["title"], v["title"], redir["pageid"]))
                disambiguation.append(v["title"])
                pageid = redir["pageid"]
                PARAMS2 = {
                    "action": "query", #we are creating a query    
                    "prop": "info", #asking for all the redirects (to the title car)
                    "format": "json", #and we want the output in a json format
                    "pageids": pageid
                }
                query_response2 = r_session.get(url=URL, params=PARAMS2)
                json_data2 = query_response2.json()
                wiki = json_data2["query"]["pages"]
#                 print(wiki)
#                 print(query_response.json["query"]["pages"][pageid]["title"])
            
    except KeyError as err:
        if err.args[0]=='redirects':
            print("It has no redirects")
        else:
            print(repr(err))
            
    # I know it's a stupid way to do it, but couldn't find fast how to include many prop
    PARAMS = {
        "action": "query", #we are creating a query
        "titles": "soda", #for the title car    
        "prop": "categories", #asking for all the redirects (to the title car)
        "format": "json" #and we want the output in a json format
    }

    #we obtain the response to the get request with the given parmeters
    query_response = r_session.get(url=URL, params=PARAMS)
    json_data = query_response.json()
    wikipedia_pages = json_data["query"]["pages"]
    #we iterate through items and print all the redirects (their title and id)
    try:
        for k, v in wikipedia_pages.items():
            for cat in v['categories']:
                print(cat["title"]) ##### HOW DO YOU GET THE SYNTACTIC HEAD???
                disambiguation.append(cat['title'])
                   
            
    except KeyError as err:
        if err.args[0]=='redirects':
            print("It has no redirects")
        else:
            print(repr(err))
            
    
    
    print(disambiguation)
    return disambiguation
    
    wikipedia_disambiguation("soda")

def get_context(sentence):
    sentence_split = nltk.word_tokenize(sentence.lower())    
    only_words = [word.lower() for word in sentence_split if word.isalnum()]
    relevant_words = [word for word in only_words if word not in stopwords.words('english')]
    lemmatized = [wnl.lemmatize(word) for word in relevant_words]
    return lemmatized

def wordnet_disambiguation(word, part_of_speech, number): # part_of_speech = "n" / "v" etc. No is 1 2 etc etc
    disambiguation = []
    synset = ""
    # get the synset
    for ss in wn.synsets(word):
        if (ss.pos().lower() == part_of_speech):
            synset = ss
            
    # add its synonyms
    disambiguation += synset.lemma_names()
    
    # add the hypernyms and hyponyms
    for hyp in synset.hypernyms():
        disambiguation.append(hyp.name().split('.')[0])
        print(hyp.root_hypernyms())
#         print(dir(hyp))
        
    for hyp in synset.hyponyms():
        disambiguation.append(hyp.name().split('.')[0])        
    # add the gloss, keeping only the lemmatized content words
    disambiguation += get_context(synset.definition())
    
    # systerhood?
    disambiguation += synset.similar_tos()
    print (disambiguation)
    
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

wordnet_sense = wordnet_disambiguation("soda", "n", "1")
wikipedia_senses = wikipedia_disambiguation("soda")

def mapping_algorithm(wikipedia_sense, wordnet_senses):
    mapping = []
    # for w in wikipedia_senses:
    #     ### Who is epsilon here??
    #     print("not sure who is epsilon to add it to the mapping")
    # for w in wikipedia_senses:
    #     if 
        
        
##### Algorithm from the paper. I tried understanding it, but couldn't manage. 
# I understood a bit of it, but too much doesn't really make sense (ha, pun intended)
# Input: SensesWiki, SensesWN
# Output: a mapping µ : SensesWiki → SensesWN
# 1: for each w ∈ SensesWiki
# 2: µ(w) := 
# 3: for each w ∈ SensesWiki
# 4: if |SensesWiki(w)| = |SensesWN(w)| = 1 then
# 5: µ(w) := w
# 1
# n
# 6: for each w ∈ SensesWiki
# 7: if µ(w) =  then
# 8: for each d ∈ SensesWiki s.t. d redirects to w
# 9: if µ(d) 6=  and µ(d) is in a synset of w then
# 10: µ(w) := sense of w in synset of µ(d); break
# 11: for each w ∈ SensesWiki
# 12: if µ(w) =  then
# 13: if no tie occurs then
# 14: µ(w) := argmax
# s∈SensesWN(w)
# p(s|w)
# 15: return µ