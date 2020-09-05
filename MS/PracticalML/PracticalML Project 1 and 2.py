print("Hello, world!")
print("Starting project...")
print("Importing libraries...")
#imports 
import numpy as np
import collections as cl
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import precision_score, recall_score, confusion_matrix, plot_confusion_matrix, classification_report, accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import GridSearchCV
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
print("Done importing libraries.")

# Useful functions
# data must pe mapped to 3D using PCA or t-SNE
def plot_in_3D(data, target, legend, colors, figsize=(20,20)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    length = data.shape[0]
    for i in range(0, length):
        if (i == int(length / 2)): # just to see how long it takes
            print("Plotted half of the points")
        if (target[i] == 0):
            c1 = ax.scatter(data[i,0], data[i,1], data[i,2] ,c=colors[0])
        if (target[i] == 1):
            c2 = ax.scatter(data[i,0], data[i,1], data[i,2], c=colors[1])

    plt.legend((c1, c2),legend)
    plt.show()
    print("Done.")
    
# data must pe mapped to 2D using PCA or t-SNE
def plot_in_2D(data, target, legend, colors, figsize=(20,20)):
    fig = plt.figure(figsize=figsize)
    length = data.shape[0]
    
    for i in range(0, length):
        if (i == int(length / 2)): # just to see how long it takes
            print("Plotted half of the points")
        if (target[i] == 0):
            c1 = plt.scatter(data[i,0], data[i,1],c=colors[0])
        if (target[i] == 1):
            c2 = plt.scatter(data[i,0], data[i,1],c=colors[1])

    plt.legend((c1, c2), legend)
    plt.show()
    print("Done.")
    # plotting functions

# data must pe mapped to 3D using PCA or t-SNE
def plot_in_3D_results(data, target, predicted, legend, colors, figsize=(20,20)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    length = data.shape[0]
    for i in range(0, length):
        if (i == int(length / 2)): # just to see how long it takes
            print("Plotted half of the points")
        if (target[i] == 0 and predicted[i] == 0):
            c1 = ax.scatter(data[i,0], data[i,1], data[i,2] ,c=colors[0])
        if (target[i] == 1 and predicted[i] == 1):
            c2 = ax.scatter(data[i,0], data[i,1], data[i,2], c=colors[1])
            
        if (target[i] == 0 and predicted[i] != 0):
            c3 = ax.scatter(data[i,0], data[i,1], data[i,2] ,c=colors[2])
        if (target[i] == 1 and predicted[i] != 1):
            c4 = ax.scatter(data[i,0], data[i,1], data[i,2], c=colors[3])

    plt.legend((c1, c2, c3, c4),legend)
    plt.show()
    print("Done.")
    
# data must pe mapped to 2D using PCA or t-SNE
def plot_in_2D_results(data, target, predicted, legend, colors, figsize=(20,20)):
    fig = plt.figure(figsize=figsize)
    length = data.shape[0]
    
    for i in range(0, length):
        if (i == int(length / 2)): # just to see how long it takes
            print("Plotted half of the points")
        if (target[i] == 0 and predicted[i] == 0):
            c1 = plt.scatter(data[i,0], data[i,1],c=colors[0])
        if (target[i] == 1 and predicted[i] == 1):
            c2 = plt.scatter(data[i,0], data[i,1],c=colors[1])
            
        if (target[i] == 0 and predicted[i] != 0):
            c3 = plt.scatter(data[i,0], data[i,1],c=colors[2])
        if (target[i] == 1 and predicted[i] != 1):
            c4 = plt.scatter(data[i,0], data[i,1],c=colors[3])

    plt.legend((c1, c2, c3, c4), legend)
    plt.show()
    print("Done.")
    

def bc_value(features, predictions):
    
    clusters = max(predictions)+1
    bc = 0
    for k in range(clusters):
        cluster_features = features[predictions == k]
        features_different = features[predictions != k]
    
        for p in cluster_features:
            bc += np.sum((np.sqrt(np.sum((features_different - p) ** 2, axis=1))))
    bc = bc / 2
    return bc
        
def wc_value(features, predictions):
    clusters = max(predictions) + 1
    wc = 0
    for k in range(clusters):
        cluster_features = features[predictions == k]
   
        for point in cluster_features:
            wc += np.sum((np.sqrt(np.sum((cluster_features - point) ** 2, axis=1))))
    wc = wc / 2
    return wc

def plot_metric_by_linkages(metric, wb_metric):
    plot_dims = {
        'ward': -2 * 0.2 + 0.1,
        'average': -0.2 + 0.1,
        'complete': 0.2 + 0.1,
        'single': 0.1
    }
    clusters = np.array(wb_metric["no_of_clusters"])
    
    fig, hc_plot = plt.subplots()
    hc_plot.bar(clusters + plot_dims["ward"], wb_metric[metric]['ward'], 0.2, label='ward')
    hc_plot.bar(clusters + plot_dims["average"], wb_metric[metric]['average'], 0.2, label='average')
    hc_plot.bar(clusters + plot_dims["complete"], wb_metric[metric]['complete'], 0.2, label='complete')
    hc_plot.bar(clusters + plot_dims["single"], wb_metric[metric]['single'], 0.2, label='single')

    hc_plot.set_ylabel(str(metric).upper() + ' scores')
    hc_plot.set_xlabel('Number of clusters')
    hc_plot.set_title('Scores by linkage methods')
    hc_plot.legend()
    hc_plot.set_xticks(wb_metric["no_of_clusters"])
    plt.show()

print("Importing dataset...")
data = pd.read_csv("Crimes - 2001 to present (25th mai 2020).csv", dtype=object)
print("Done importing dataset.")

data.info()
data.head()

# Feature engineering
# 1. Drop unused tables: ID, Case Number, Description, Block, Location, Location Description as we have too much location information
data = data.drop(['ID', 'Case Number', 'X Coordinate', 'Y Coordinate', 'Block', 'Updated On', 'Location', 'Description', 'Location Description'], axis=1)

# We've eliminated 2020 to minimize the risk of possible anomalies happening in 2020 due to Covid-19
data['Year'] = pd.to_numeric(data['Year'])
data = data[(data.Year > 2014) & (data.Year < 2020)]

# See how many values are null before engineering
data_missing = data.isnull().sum()
print(data_missing)

perc_missing = round(100 * (data_missing / len(data)), 2)
print(perc_missing)

# Visualize how many values are null before engineering
plt.figure(figsize=(12, 12))
sns.heatmap(data.isnull(), cbar=True, cmap='Wistia')

# since the dataset is absolutely immense, we can easily drop the NaN rows. We will do so before sampling
data = data.dropna()

data['Arrest'] = pd.factorize(data['Arrest'])[0]

# types of crimes
plt.figure(figsize=(12, 12))
sns.countplot(data['Arrest'])
no, yes = data['Arrest'].value_counts()
print("Number of cases ending without arrests:", no)
print("Number of cases ending with arrests:", yes)

data['Arrest'].value_counts(normalize=True) * 100

# types of crimes
plt.figure(figsize=(12, 12))
sns.countplot(x='Year', hue='Arrest', data=data)

# Dataset is too huge and takes too long to train on all of it, we're going to sample 100.000. Also, we're going to duplicate the sampled data in order to apply
# supervised and unsupervised algorithms on the same sample
# Random sampling
data = data.sample(n=100000)

# Since we loaded the model with object as dtype (for faster loading), 
# we're going to specify all the types manually
data['DateTime'] = pd.to_datetime(data['Date'])
data['Year'] = data['DateTime'].dt.year
data['Month'] = data['DateTime'].dt.month
data['Day'] = data['DateTime'].dt.day
data['Hour'] = data['DateTime'].dt.hour

data = data.drop(['Date'], axis=1)
data = data.drop(['DateTime'], axis=1)

# Convert categorical attributes to Numerical
data['IUCR'] = pd.factorize(data['IUCR'])[0]
data['Primary Type'] = pd.factorize(data['Primary Type'])[0]
data['Domestic'] = pd.factorize(data['Domestic'])[0]
data['Beat'] = pd.factorize(data['Beat'])[0]
data['District'] = pd.factorize(data['District'])[0]
data['Ward'] = pd.factorize(data['Ward'])[0]
data['Community Area'] = pd.factorize(data['Community Area'])[0]
data['FBI Code'] = pd.factorize(data['FBI Code'])[0]
data['Latitude'] = pd.factorize(data['Latitude'])[0]
data['Longitude'] = pd.factorize(data['Longitude'])[0]

# Scaling the features
data_target = data['Arrest']
data_train = data.drop(['Arrest'], axis = 1)
scaled_features = StandardScaler().fit_transform(data_train.values)
data_scaled = pd.DataFrame(scaled_features, index=data_train.index, columns=data_train.columns)
data_scaled['Arrest'] = data_target

# Using Pearson correlation
plt.figure(figsize=(18, 10))
correlation = data.corr()
sns.heatmap(correlation, annot=True, cmap=plt.cm.Reds)
plt.show()

# SUPERVISED LEARNING
data.info()

X = data_scaled.drop(['Arrest'], axis = 1)
y = data_scaled['Arrest']

# spliting data into training: 50%, validation: 25% and testing: 25%
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size = 0.5, train_size = 0.5, random_state = 42)
X_validation, X_test, y_validation, y_test = train_test_split(X_validation, y_validation, test_size = 0.5, train_size = 0.5, random_state = 42)

# Baseline definition
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(X_train, y_train)
predicted = dummy_clf.predict(X_test)
acc = dummy_clf.score(X_test, y_test)

# cf_matrix = confusion_matrix(predicted, y_test)
# print(cf_matrix)
print(acc)
print(classification_report(y_test, predicted))
plot_confusion_matrix(dummy_clf, X_test, y_test, normalize='true')
plt.show()

# Hyperparameter tuning KNN
# GridSearchCV
grid_params_knn = {
    'weights': ['uniform', 'distance'],
    'algorithm': ['auto'],
    'n_neighbors': range(1, 50),
    'metric': ['euclidean', 'manhattan', 'chebyshev', 'minkowski', 'seuclidean', 'mahalanobis'],
    
}

grid_search_KNN = GridSearchCV(KNeighborsClassifier(), grid_params_knn, verbose=1, cv=5, n_jobs=-1)


grid_search_results_KNN = grid_search_KNN.fit(X_validation, y_validation)

print(grid_search_results_KNN.best_estimator_)
print(grid_search_results_KNN.best_score_)
print(grid_search_results_KNN.score)

# Ploting the results
results = grid_search_results_KNN.cv_results_['params']
scores = grid_search_results_KNN.cv_results_['split2_test_score']
dic = defaultdict(list)
for i in range(len(results)):
    dic[results[i]['metric']].append((results[i]['n_neighbors'], scores[i]))
    
colors = {
    'euclidean': 'r',
    'manhattan': 'b',
    'chebyshev': 'g',
    'minkowski': 'c',
    'seuclidean': 'm',
    'mahalanobis': 'k'
}

# plt.figure(figsize=(20, 20))
for key in dic:
    neighbors = [x[0] for x in dic[key]]
    score = [x[1] for x in dic[key]]
    plt.plot(neighbors, score, colors[key], label=key)

legend = ['euclidean', 'manhattan', 'chebyshev', 'minkowski', 'seuclidean', 'mahalanobis']
plt.legend(legend)
plt.xlabel('Neighbors')
plt.ylabel('Score')
plt.show()

knn = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='manhattan',
                     metric_params=None, n_jobs=None, n_neighbors=15, p=2,
                     weights='distance')
knn.fit(X_train, y_train)
knn_y_predict = knn.predict(X_test)

knn_acc = accuracy_score(y_test, knn_y_predict)
knn_cf_matrix = confusion_matrix(knn_y_predict, y_test)
knn_report = classification_report(y_test, knn_y_predict)

print(knn_cf_matrix)
print(knn_acc)
print(knn_report)
plot_confusion_matrix(knn, X_test, y_test, normalize='true')
plt.show()

# Hyperparameter tuning RF
# GridSearchCV
grid_params_rf = {
    'n_estimators': [50, 100, 200, 300],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [None, 4, 5, 6, 7, 8],
    'criterion' :['gini', 'entropy'],
    'bootstrap': ['False', 'True']
}

grid_search_rf = GridSearchCV(RandomForestClassifier(), grid_params_rf, verbose=1, cv=5, n_jobs=-1)

grid_search_rf_results = grid_search_rf.fit(X_validation, y_validation)

print(grid_search_rf_results.best_estimator_)
print(grid_search_rf_results.best_score_)

# Random Forest
rf = RandomForestClassifier(bootstrap='False', ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='log2',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=200,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)

rf.fit(X_train, y_train)
rf_y_predict = rf.predict(X_test)

rf_acc = accuracy_score(y_test, rf_y_predict)
rf_cf_matrix = confusion_matrix(rf_y_predict, y_test)
rf_report = classification_report(y_test, rf_y_predict)

print(rf_cf_matrix)
print(rf_acc)
print(rf_report)

plot_confusion_matrix(rf, X_test, y_test, normalize='true')
plt.show()

Xu = data_scaled.drop(['Arrest'], axis = 1)
yu = data_scaled['Arrest']
yu = pd.factorize(yu)[0]
# spliting data into training: 70% and testing: 30%
Xu_train, Xu_test, yu_train, yu_test = train_test_split(Xu, yu, test_size = 0.3, train_size = 0.7, random_state = 42)

pca_train = PCA(n_components=2).fit_transform(Xu_train)
pca_test = PCA(n_components=2).fit_transform(Xu_test)

tsne_train = TSNE(n_components=2).fit_transform(Xu_train)
tsne_test = TSNE(n_components=2).fit_transform(Xu_test)

pca_train_3D = PCA(n_components=3).fit_transform(Xu_train)
pca_test_3D = PCA(n_components=3).fit_transform(Xu_test)

tsne_train_3d = TSNE(n_components=3).fit_transform(Xu_train)
tsne_test_3d = TSNE(n_components=3).fit_transform(Xu_test)

legend = ['No Arrest', 'Arrest']
colors = ['b', 'r']
plot_in_2D(pca_train, yu_train, legend, colors)
plot_in_2D(pca_test, yu_test, legend, colors)

plot_in_2D(tsne_train, yu_train, legend, colors)
plot_in_2D(tsne_test, yu_test, legend, colors)

legend = ['No Arrest', 'Arrest']
colors = ['b', 'r']
plot_in_3D(pca_test_3D, yu_test, legend, colors)
plot_in_3D(pca_train_3D, yu_train, legend, colors)

plot_in_3D(tsne_test_3d, yu_test, legend, colors)
plot_in_3D(tsne_train_3d, yu_train, legend, colors)

# HC
# change to array for HC dendogram
Xua_train = np.array(Xu_train)
Xua_test = np.array(Xu_test)
yua_train = np.array(yu_train)
yua_test = np.array(yu_test)
Xa = np.array(X)

plt.figure(figsize=(5, 5))
plt.title("Ward")
dendogram_ward = shc.dendrogram(shc.linkage(Xua_train[:10000], method='ward'))

plt.figure(figsize=(5, 5))
plt.title("Average")
dendogram_average = shc.dendrogram(shc.linkage(Xua_train[:10000], method='average'))

plt.figure(figsize=(5, 5))
plt.title("Complete")
dendogram_complete = shc.dendrogram(shc.linkage(Xua_train[:10000], method='complete'))

plt.figure(figsize=(5, 5))
plt.title("Single")
dendogram_complete = shc.dendrogram(shc.linkage(Xua_train[:10000], method='single'))

# The clustering solution consists in maximizing B(C) or minimizing W(C)
# W(C) = The distance between points in the same cluster
# B(C) = The distance between points from different clusters

wb_metric = {
    'w': {
        'ward': [],
        'average': [],
        'complete': [],
        'single': []
    },
    'b': {
        'ward': [],
        'average': [],
        'complete': [],
        'single': []
    },
    'no_of_clusters': [2]
}

for linkage in wb_metric['w']:
    hc = AgglomerativeClustering(n_clusters=wb_metric['no_of_clusters'][0], affinity='euclidean', linkage=linkage)
    hc_y = hc.fit_predict(Xua_train[:1000])
    wb_metric['w'][linkage].append(wc_value(Xua_train[:1000], hc_y))

        
for linkage in wb_metric['b']:
    hc = AgglomerativeClustering(n_clusters=wb_metric['no_of_clusters'][0], affinity='euclidean', linkage=linkage)
    hc_y = hc.fit_predict(Xua_train[:1000])
    wb_metric['b'][linkage].append(bc_value(Xua_train[:1000], hc_y))
    

plot_metric_by_linkages("w", wb_metric)
plot_metric_by_linkages("b", wb_metric)

hc_ward = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
hc_ward_y = hc_ward.fit_predict(Xua_test)
hc_ward_acc = accuracy_score(yua_test, hc_ward_y)
print(hc_ward_acc)

hc_ward_acc = accuracy_score(yu_test, hc_ward_y)
hc_ward_cf_matrix = confusion_matrix(hc_ward_y, yu_test)
hc_ward_report = classification_report(yu_test, hc_ward_y)

print(hc_ward_cf_matrix)
print(hc_ward_acc)
print(hc_ward_report)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_3D_results(pca_test_3D, yu_test, hc_ward_y, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_3D_results(tsne_test_3d, yu_test, hc_ward_y, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_2D_results(pca_test, yu_test, hc_ward_y, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_2D_results(tsne_test, yu_test, hc_ward_y, legend, colors)

hc_complete = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='complete')
hc_complete_y = hc_complete.fit_predict(Xua_test)
hc_complete_acc = accuracy_score(yua_test, hc_complete_y)
print(hc_complete_acc)

hc_complete_acc = accuracy_score(yu_test, hc_complete_y)
hc_complete_cf_matrix = confusion_matrix(hc_complete_y, yu_test)
hc_complete_report = classification_report(yu_test, hc_complete_y)

print(hc_complete_cf_matrix)
print(hc_complete_acc)
print(hc_complete_report)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_3D_results(pca_test_3D, yu_test, hc_complete_y, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_3D_results(tsne_test_3d, yu_test, hc_complete_y, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_2D_results(tsne_test, yu_test, hc_complete_y, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_2D_results(pca_test, yu_test, hc_complete_y, legend, colors)

# Unsupervised learning
km = KMeans(n_clusters=2, random_state=0)
km.fit(Xu_test)
y_km = km.predict(Xu_test)

centers = km.cluster_centers_

accuracy_score(yu_test, y_km)

km_acc = accuracy_score(yu_test, y_km)
km_cf_matrix = confusion_matrix(y_km, yu_test)
km_report = classification_report(yu_test, y_km)

print(km_cf_matrix)
print(km_acc)
print(km_report)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_3D_results(pca_test_3D, yu_test, y_km, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_3D_results(tsne_test_3d, yu_test, y_km, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_2D_results(tsne_test, yu_test, y_km, legend, colors)

legend = ['No Arrest', 'Arrest', 'False Arrest', 'False No Arrest']
colors = ['b', 'r', 'y', 'c']
plot_in_2D_results(pca_test, yu_test, y_km, legend, colors)

