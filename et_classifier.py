# EXTRA TREES CLASSIFIER - EXTREMELY RANDOMIZED TREES

# Extra Trees Classification
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import ExtraTreesClassifier

file = 'cleanedData2.csv'
#names = ['budget','popularity', 'revenue', 'runtime', 'vote_average', 'vote_count']
names = ['budget', 'genres', 'original_language','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_count', 'vote_average'] #movie id and original title not here
dataframe = pd.read_csv(file, names=names)
array = dataframe.values
X = array[:,0:9]
X = np.asarray(X)
Y = array[:9]
print X.shape
X = X.reshape(45460, 9)
seed = 8
num_trees = 100
max_features = 8
kfold = model_selection.KFold(n_splits=10, random_state=seed)
model = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features)
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())



# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.metrics import r2_score
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import StratifiedKFold
# import pandas as pd
# import numpy as np
#
# #'id', 'budget', 'revenue', 'popularity', 'adult', 'original_language', 'genres',
# #'production_companies', 'production_countries', 'vote_average', 'vote_count'
#
#
# meta_filen = "metadata_cleaned_discretized.csv"
#
# cols=['adult', 'original_language', 'vote_average', 'vote_count']
# f_cols = ['adult', 'original_language']
# c_cols = ['vote_average']
#
# meta = pd.read_csv(meta_filen, usecols=cols)
# f_data = meta[f_cols].as_matrix()
# c_data = np.ravel(meta[c_cols].as_matrix())
#
# x_data = pd.read_csv(meta_filen, usecols=f_cols)
# x = x_data.as_matrix()
# y_data = pd.read_csv(meta_filen, usecols=c_cols)
# y = np.ravel(y_data.as_matrix())
#
#
# f_train, f_test, c_train, c_test = train_test_split(f_data, c_data)
#
# print("running model...")
# clf = ExtraTreesClassifier(n_estimators = 10)
# clf = clf.fit(f_train, c_train)
# print("most important:"+str(clf.feature_importances_))
# predicted = clf.predict(f_test)
# print("predicted values: "+str(len(predicted)))
# accuracy = r2_score(predicted, c_test)
# print("R2 : "+str(accuracy))
#
# '''
# print("beginning testing...")
#
# total = 10
#
# skf = StratifiedKFold(n_splits=total)
#
# stotal = 0.0
#
# print(skf)
#
# for train_index, test_index in skf.split(x, y):
# 	x_train, x_test = x[train_index], x[test_index]
# 	y_train, y_test = y[train_index], y[test_index]
# 	clf = ExtraTreesClassifier(n_estimators = 10)
# 	clf.fit(x_train, y_train)
# 	score = clf.score(x_test, y_test)
# 	print("Error: ", score)
# 	stotal = stotal + score
#
# print("Average Error: ", stotal/total )
# '''
