from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

meta_filen = "metadata_cleaned.csv"

cols=['budget', 'revenue', 'popularity', 'vote_average', 'vote_count']
f_cols = ['budget', 'revenue', 'popularity', 'vote_count']
c_cols = ['vote_average']

meta = pd.read_csv(meta_filen, usecols=cols)
f_data = meta[f_cols].as_matrix()
c_data = np.ravel(meta[c_cols].as_matrix())


f_train, f_test, c_train, c_test = train_test_split(f_data, c_data)

print("running model...")
clf = RandomForestRegressor(n_estimators = 10)
clf = clf.fit(f_train, c_train)
print("most important:"+str(clf.feature_importances_))
predicted = clf.predict(f_test)
print("predicted values: "+str(len(predicted)))
accuracy = r2_score(predicted, c_test)
print("R2 : "+str(accuracy))
