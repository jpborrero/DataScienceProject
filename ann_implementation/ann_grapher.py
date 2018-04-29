from sklearn.neural_network import MLPClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np

import bagger as bg

meta_filen = "merged_metakey_discBin4.csv"

cols=['genres', 'keywords']
f_cols = ['genres', 'keywords']
c_cols = ['vote_average']

x_data = pd.read_csv(meta_filen, usecols=f_cols)
y = pd.read_csv(meta_filen, usecols=c_cols)
y = np.ravel(y.as_matrix())

'''
budget = x_data['budget'].as_matrix()
revenue = x_data['revenue'].as_matrix()
popularity = x_data['popularity'].as_matrix()
'''
'''
full_doc = bg.getDoc(x_data, 'genres')
vectorizer = bg.vectorizeDoc(full_doc)
text = bg.getVectors(full_doc, vectorizer)
'''
'''
x_temp = []
for i in range(len(text)):
	new_row = text[i]
	new_row = np.append(new_row, budget[i])
	new_row = np.append(new_row, revenue[i])
	new_row = np.append(new_row, popularity[i])
	x_temp.append(new_row)
x = np.array(x_temp)
'''


full_doc_genres = bg.getDoc(x_data, 'genres')
full_doc_keywords = bg.getDoc(x_data, 'keywords')
vectorizer1 = bg.hashDoc(full_doc_genres)
vectorizer2 = bg.hashDoc(full_doc_keywords)
x1 = bg.getVectors(full_doc_genres, vectorizer1)
x2 = bg.getVectors(full_doc_keywords, vectorizer2)

x=[]
for i in range(len(x1)):
	new_row = np.append(x1[i], x2[i])
	x.append(new_row)
x = np.array(x)
	
print("beginning testing...")

total = 10

skf = StratifiedKFold(n_splits=total)

stotal = np.array([])
ftotal = np.array([])

classOneX = []
classOneY = []

classTwoX = []
classTwoY = []

for train_index, test_index in skf.split(x, y):
	x_train, x_test = x[train_index], x[test_index]
	y_train, y_test = y[train_index], y[test_index]
	clf = MLPClassifier(activation="tanh", solver='lbfgs', learning_rate='constant', hidden_layer_sizes=(5, 1))
	clf.fit(x_train, y_train)
	predicted = clf.predict(x_test)
	print(predicted)
	
	for cat in predicted:
		if cat == '<2.5>':
			classOneX.append(row[labelOne])
			classOneY.append(row[labelTwo])
	
	score = accuracy_score(y_test, predicted)
	print(score)
	stotal = np.append(stotal, score)
	fscore = f1_score(y_test, predicted, average='weighted')
	ftotal = np.append(ftotal, fscore)
	

print("Average Accuracy: ", stotal.mean(), "(+/-", stotal.std() * 2, ')')
print("Average Error: ", 1-stotal.mean(), "(+/-", stotal.std() * 2, ')')
print("Average F-Measure: ", ftotal.mean(), "(+/-", ftotal.std() * 2, ')')