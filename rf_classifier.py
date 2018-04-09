from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import pandas as pd
import numpy as np

#'id', 'budget', 'revenue', 'popularity', 'adult', 'original_language', 'genres', 
#'production_companies', 'production_countries', 'vote_average', 'vote_count'


meta_filen = "metadata_cleaned_discretized.csv"

cols=['adult', 'original_language', 'vote_average', 'vote_count']
f_cols = ['adult', 'original_language']
c_cols = ['vote_average']

meta = pd.read_csv(meta_filen, usecols=cols)
f_data = meta[f_cols].as_matrix()
c_data = np.ravel(meta[c_cols].as_matrix())

x_data = pd.read_csv(meta_filen, usecols=f_cols)
x = x_data.as_matrix()
y_data = pd.read_csv(meta_filen, usecols=c_cols)
y = np.ravel(y_data.as_matrix())


f_train, f_test, c_train, c_test = train_test_split(f_data, c_data)

print("running model...")
clf = RandomForestClassifier(n_estimators = 10)
clf = clf.fit(f_train, c_train)
print("most important:"+str(clf.feature_importances_))
predicted = clf.predict(f_test)
print("predicted values: "+str(len(predicted)))
accuracy = r2_score(predicted, c_test)
print("R2 : "+str(accuracy))

'''
print("beginning testing...")

total = 10

skf = StratifiedKFold(n_splits=total)

stotal = 0.0

print(skf)

for train_index, test_index in skf.split(x, y):
	x_train, x_test = x[train_index], x[test_index]
	y_train, y_test = y[train_index], y[test_index]
	clf = RandomForestClassifier(n_estimators = 10)
	clf.fit(x_train, y_train)
	score = clf.score(x_test, y_test)
	print("Error: ", score)
	stotal = stotal + score

print("Average Error: ", stotal/total )
'''