from sklearn.neural_network import MLPClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import pandas as pd
import numpy as np

import bagger as bg

meta_filen = "merged_metakey_discretized.csv"

cols=['genres', 'budget', 'revenue', 'popularity']
f_cols = ['genres', 'budget', 'revenue', 'popularity']
c_cols = ['vote_average']

x_data = pd.read_csv(meta_filen, usecols=f_cols)
y = pd.read_csv(meta_filen, usecols=c_cols)
y = np.ravel(y.as_matrix())

budget = x_data['budget'].as_matrix()
revenue = x_data['revenue'].as_matrix()
popularity = x_data['popularity'].as_matrix()

full_doc = bg.getDoc(x_data, 'genres')
vectorizer = bg.vectorizeDoc(full_doc)
text = bg.getVectors(full_doc, vectorizer)

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
full_doc_companies = bg.getDoc(x_data, 'production_companies')
vectorizer1 = bg.vectorizeDoc(full_doc_genres)
vectorizer2 = bg.hashDoc(full_doc_companies)
x1 = bg.getVectors(full_doc_genres, vectorizer1)
x2 = bg.getVectors(full_doc_companies, vectorizer2)

x=[]
for i in range(len(x1)):
	print(x1[i], x2[i])
	print()
	new_row = np.append(x1[i], x2[i])
	print(new_row)
	print()
	x = x.append(new_row)
	
exit()
'''
	
	
print("beginning testing...")

total = 10

skf = StratifiedKFold(n_splits=total)

stotal = 0.0

for train_index, test_index in skf.split(x, y):
	x_train, x_test = x[train_index], x[test_index]
	y_train, y_test = y[train_index], y[test_index]
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 4), random_state=1)
	clf.fit(x_train, y_train)
	score = clf.score(x_test, y_test)
	print("Accuracy: ", score)
	stotal = stotal + score

print("Average Accuracy: ", stotal/total )