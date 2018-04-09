from sklearn.neural_network import MLPClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import pandas as pd
import numpy as np

import bagger as bg

meta_filen = "merged_metakey_discretized.csv"

cols=['genres', 'keywords', 'vote_average']
f_cols = ['genres', 'keywords']
c_cols = ['vote_average']

x_data = pd.read_csv(meta_filen, usecols=f_cols)
y = pd.read_csv(meta_filen, usecols=c_cols)
y = np.ravel(y.as_matrix())

full_doc = bg.getDoc(x_data, 'genres')
vectorizer = bg.vectorizeDoc(full_doc)
x = bg.getVectors(full_doc, vectorizer)

'''
full_doc_genres = bg.getDoc(x_data, 'genres')
full_doc_keywords = bg.getDoc(x_data, 'keywords')
vectorizer1 = bg.vectorizeDoc(full_doc_genres)
vectorizer2 = bg.vectorizeDoc(full_doc_keywords)
x1 = bg.getVectors(full_doc_genres, vectorizer1)
x2 = bg.getVectors(full_doc_keywords, vectorizer2)

x=[]
for x1_inst, x2_inst in x1, x2:
	new_row = x1_inst.extend(x2_inst)
	x = x.append(new_row)
'''

print("beginning testing...")

total = 10

skf = StratifiedKFold(n_splits=total)

stotal = 0.0

print(skf)

for train_index, test_index in skf.split(x, y):
	x_train, x_test = x[train_index], x[test_index]
	y_train, y_test = y[train_index], y[test_index]
	clf = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
	clf.fit(x_train, y_train)
	score = clf.score(x_test, y_test)
	print("Accuracy: ", score)
	stotal = stotal + score

print("Average Accuracy: ", stotal/total )