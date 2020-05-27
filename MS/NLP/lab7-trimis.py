import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.corpus import senseval
nltk.download('senseval')
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from nltk.stem import WordNetLemmatizer
from sklearn.naive_bayes import MultinomialNB
import random

lem=WordNetLemmatizer()

def lemmatize_tuple(tupl):
    if (tupl[0].lower() not in stopwords.words('english')):
        if(tupl[1].lower()) in ['nn', 'nns', 'nnp', 'nnps']:
            return ((lem.lemmatize(tupl[0], wordnet.NOUN).lower(), 'n'))

        if(tupl[1].lower()) in ['vb', 'vbd', 'vbg', 'vbn', 'vbp', 'vbz']:
            return ((lem.lemmatize(tupl[0], wordnet.VERB).lower(), 'v'))

        if(tupl[1].lower()) in ['jj', 'jjr', 'jjs']:
            return ((lem.lemmatize(tupl[0], wordnet.ADJ).lower(), 'j'))

        if(tupl[1].lower() in ['rb', 'rbr', 'rbs']):
            return ((lem.lemmatize(tupl[0], wordnet.ADV).lower(), 'r'))
    
    return False

inst=senseval.instances('interest.pos')

lemmatized_inst = []
for row in inst:
    for tup in row.context:
        new_tup = lemmatize_tuple(tup)
        if ((new_tup != False) and (new_tup not in lemmatized_inst)):
            lemmatized_inst.append(new_tup)

matrix = np.zeros((len(inst), len(lemmatized_inst)))

matrix.shape

# refactor later, wrote in a hurry
index = 0
for row in inst:
    for tup in row.context:
        new_tup = lemmatize_tuple(tup)
        index2 = 0
        for element in lemmatized_inst:
            if (new_tup == element):
                matrix[index][index2] += 1
            index2 += 1
    index += 1       

Y = []
for row in inst:
    Y.append(row.senses[0])

# I went with matrix initially, but moved to X for convention
X = matrix
# random.shuffle(X)
X.shape

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)

pred_y = clf.predict(X_test)

acc = accuracy_score(y_test, pred_y)
print(acc)

f = open("lab7-output.txt", "w")
f.write("Accuracy: " + str(acc))
f.close()