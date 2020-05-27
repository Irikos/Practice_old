# imports
import os
import sys
import nltk
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser

os.environ['JAVAHOME'] = "/usr/bin/java"
os.environ['STANFORD_PARSER'] = './stanford-parser.jar'
os.environ['STANFORD_MODELS'] = './stanford-parser-3.9.2-models.jar'
parser = StanfordParser(model_path='./englishPCFG.ser.gz')
dependency_parser = StanfordDependencyParser(path_to_jar='./stanford-parser.jar', path_to_models_jar='./englishPCFG.ser.gz')

file = open("Lab 3-5 sentences.txt")

sentence_index = 0
for sentence in file:
    sentence_index += 1
    print('Sentence - number', sentence_index)
    propozitii = parser.raw_parse_sents((sentence, ''))
    for prop in propozitii:
        print(list(prop))
    dependente = dependency_parser.raw_parse(sentence)
    for dep in dependente:
        print(list(dep.triples()))
    print("--------------------------------------------------------------")