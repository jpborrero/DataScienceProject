from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np

import bagger as bg

meta_filen = "merged_metakey.csv"

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
vectorizer1 = bg.vectorizeDoc(full_doc_genres)
vectorizer2 = bg.hashDoc(full_doc_keywords)
x1 = bg.getVectors(full_doc_genres, vectorizer1)
x2 = bg.getVectors(full_doc_keywords, vectorizer2)

x=[]
for i in range(len(x1)):
	new_row = np.append(x1[i], x2[i])
	x.append(new_row)
x = np.array(x)

print("beginning testing...")


x_train, x_test, y_train, y_test = train_test_split(x, y)


active = "tanh"
solve = 'lbfgs'
learning_r = 'constant'
layer_size=(80, 50, 10)

print("running model "+str(layer_size)+"...")
clf = MLPRegressor(activation=active, solver=solve, learning_rate=learning_r, hidden_layer_sizes=layer_size, random_state=1)
clf = clf.fit(x_train, y_train)
predicted = clf.predict(x_test)
accuracy = r2_score(predicted, y_test)
print("R2 : "+str(accuracy))

'''

layer_sizes = [(5, 3, 1), (10, 5, 3), (20, 10, 5), (50, 20, 10), (100, 50, 20)]

for layer_size in layer_sizes:

	print("running model "+str(layer_size)+"...")
	clf = MLPRegressor(activation=active, solver=solve, learning_rate=learning_r, hidden_layer_sizes=layer_size, random_state=1)
	clf = clf.fit(x_train, y_train)
	predicted = clf.predict(x_test)
	accuracy = r2_score(predicted, y_test)
	print("R2 : "+str(accuracy))

'''
