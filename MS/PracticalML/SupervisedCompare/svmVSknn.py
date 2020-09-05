# since I'm learning, I'll comment a lot to make sure i understand and remember it 
import numpy as np # linear algebra
import pandas as pd # data processing for the CSV file
import matplotlib.pyplot as plt # used for plotting the graph 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
############################# function define zone ###################################
# cancer is complicated. This dataset is more suited for probabilistic and exploratory data analysis
# a patient has cancer FOR SURE only if those 4 tests come positive so we assign 25% to each test
def detect_cervical_cancer(data):
    # return (data['Hinselmann'] + data['Schiller'] + data['Citology'] + data['Biopsy']) / 4
    if (data['Hinselmann'] == 1 and data['Schiller'] == 1 and data['Citology'] == 1 and data['Biopsy'] == 1):
        return 1
    return 0
######################################################################################

print("Project starting...")
print("Hello, world!")

data = pd.read_csv("kag_risk_factors_cervical_cancer.csv")

data = data.replace('?', np.nan)

# too few data available
data = data.drop(['STDs: Time since first diagnosis', 'STDs: Time since last diagnosis'], axis = 1)

# convert all data to numeric type for computation
data = data.convert_objects(convert_numeric=True)

# replace the data with the mean
data['Number of sexual partners'] = data['Number of sexual partners'].fillna(data['Number of sexual partners'].median())
data['First sexual intercourse'] = data['First sexual intercourse'].fillna(data['First sexual intercourse'].median())
data['Num of pregnancies'] = data['Num of pregnancies'].fillna(data['Num of pregnancies'].median())
data['Smokes'] = data['Smokes'].fillna(1)
data['Smokes (years)'] = data['Smokes (years)'].fillna(data['Smokes (years)'].median())
data['Smokes (packs/year)'] = data['Smokes (packs/year)'].fillna(data['Smokes (packs/year)'].median())
data['Hormonal Contraceptives'] = data['Hormonal Contraceptives'].fillna(1)
data['Hormonal Contraceptives (years)'] = data['Hormonal Contraceptives (years)'].fillna(data['Hormonal Contraceptives (years)'].median())
data['IUD'] = data['IUD'].fillna(0) # Under suggestion
data['IUD (years)'] = data['IUD (years)'].fillna(0) #Under suggestion
data['STDs'] = data['STDs'].fillna(1)
data['STDs (number)'] = data['STDs (number)'].fillna(data['STDs (number)'].median())
data['STDs:condylomatosis'] = data['STDs:condylomatosis'].fillna(data['STDs:condylomatosis'].median())
data['STDs:cervical condylomatosis'] = data['STDs:cervical condylomatosis'].fillna(data['STDs:cervical condylomatosis'].median())
data['STDs:vaginal condylomatosis'] = data['STDs:vaginal condylomatosis'].fillna(data['STDs:vaginal condylomatosis'].median())
data['STDs:vulvo-perineal condylomatosis'] = data['STDs:vulvo-perineal condylomatosis'].fillna(data['STDs:vulvo-perineal condylomatosis'].median())
data['STDs:syphilis'] = data['STDs:syphilis'].fillna(data['STDs:syphilis'].median())
data['STDs:pelvic inflammatory disease'] = data['STDs:pelvic inflammatory disease'].fillna(data['STDs:pelvic inflammatory disease'].median())
data['STDs:genital herpes'] = data['STDs:genital herpes'].fillna(data['STDs:genital herpes'].median())
data['STDs:molluscum contagiosum'] = data['STDs:molluscum contagiosum'].fillna(data['STDs:molluscum contagiosum'].median())
data['STDs:AIDS'] = data['STDs:AIDS'].fillna(data['STDs:AIDS'].median())
data['STDs:HIV'] = data['STDs:HIV'].fillna(data['STDs:HIV'].median())
data['STDs:Hepatitis B'] = data['STDs:Hepatitis B'].fillna(data['STDs:Hepatitis B'].median())
data['STDs:HPV'] = data['STDs:HPV'].fillna(data['STDs:HPV'].median())

# adding the target variable column
# data['CervicalCancer'] = data.apply(lambda row: detect_cervical_cancer(row), axis = 1)

# separate labels and features
# x_data = data.drop(['Hinselmann', 'Schiller', 'Citology', 'Biopsy', 'CervicalCancer'], axis = 1)
# y_data = data[['Hinselmann','Schiller', 'Citology', 'Biopsy', 'CervicalCancer']]
x_data = data.drop(['Schiller'], axis = 1)
y_data = data['Biopsy']

# x_data = data.drop(['Hinselmann', 'Schiller', 'Citology', 'Biopsy'], axis = 1)
# y_data = data[['Hinselmann','Schiller', 'Citology', 'Biopsy']]

# some plots to visualize the data
# sns.countplot(x='CervicalCancer', data=data, palette='bwr')
# plt.show()

# spliting data into training: 50%, validation: 25% and testing: 25%
x_training_data, x_validation_data, y_training_data, y_validation_data = train_test_split(x_data, y_data, test_size = 0.5, train_size = 0.5, random_state = 10)
x_validation_data, x_test_data, y_validation_data, y_test_data = train_test_split(x_validation_data, y_validation_data, test_size = 0.5, train_size = 0.5, random_state = 10)

# print (x_training_data)
# print (y_training_data)

# print (x_validation_data)
# print (y_validation_data)

# print (x_test_data)
# print (y_test_data)

# print(y_training_data['CervicalCancer'].value_counts())
# print(y_validation_data['CervicalCancer'].value_counts())
# print(y_test_data['CervicalCancer'].value_counts())

# df = data.DataFrame({'0': list('01')})
# df.groupby('0').count()

# print(data.groupby('Hinselmann').count())
# print(data.groupby('Schiller').count())
# print(data.groupby('Citology').count())
# print(data.groupby('Biopsy').count())
# print(data.groupby('CervicalCancer').count())

################################### KNN time #######################################

neighborsScore = []
for k in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors = k, metric='euclidean')
    knn.fit(x_training_data, y_training_data)

    y_predict = knn.predict(x_validation_data)
    neighborsScore.append(knn.score(x_validation_data, y_validation_data))
    print(confusion_matrix(y_validation_data, y_predict))

print (neighborsScore)
plt.plot(neighborsScore)

# # data['CervicalCancer'] = data.apply(lambda row: detect_cervical_cancer(row), axis = 1)
#     print (y_predict)

# sns.countplot(x='Hinselmann', data=data, palette='bwr')

# sns.scatterplot(
#     x='Hinselmann',
#     y='Schiller',
#     hue='Citology',
#     data=x_validation_data.join(y_validation_data, how='outer')a
# )

# plt.show()
# print(confusion_matrix(y_validation_data.values.argmax(axis=1), y_predict.argmax(axis=1)))
print(confusion_matrix(y_validation_data, y_predict))

# print(knn.score(x_validation_data, y_validation_data))

plt.show()