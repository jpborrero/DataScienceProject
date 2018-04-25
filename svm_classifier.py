from sklearn import svm
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

print "setting up model..."
meta_filen = "discreteDataHeaders.csv"

cols=['budget', 'revenue', 'popularity', 'vote_average', 'vote_count']
f_cols = ['budget', 'revenue', 'popularity', 'vote_count']
c_cols = ['vote_average']

meta = pd.read_csv(meta_filen, usecols=cols)
f_data = meta[f_cols].as_matrix()
c_data = np.ravel(meta[c_cols].as_matrix())

# Test on discretized data
f_train, f_test, c_train, c_test = train_test_split(f_data, c_data)

print "running model with no binning..."
clf = svm.SVC()
clf = clf.fit(f_train, c_train)
predicted = clf.predict(f_test)
accuracy = r2_score(c_test, predicted)
print "R2 :", accuracy
print

# Test on data sorted into 4 bins
d4_meta = meta
for val in d4_meta[c_cols]:
	if val < 2.5:
		val = 0.0
	elif val < 5.0:
		val = 2.5
	elif val < 7.5:
		val = 5.0
	else:
		val = 7.5
d4_c_data = np.ravel(d4_meta[c_cols].as_matrix())
d4_f_train, d4_f_test, d4_c_train, d4_c_test = train_test_split(f_data, d4_c_data)

print "running model with 4 bins..."
clf = svm.SVC()
clf = clf.fit(d4_f_train, d4_c_train)
predicted = clf.predict(d4_f_test)
accuracy = r2_score(d4_c_test, predicted)
print "R2 :", accuracy
print

# Test on data sorted into 5 bins
d5_meta = meta
for val in d5_meta[c_cols]:
	if val < 2.0:
		val = 0.0
	elif val < 4.0:
		val = 2.0
	elif val < 6.0:
		val = 4.0
	elif val < 8.0:
		val = 6.0
	else:
		val = 8.0
d5_c_data = np.ravel(d5_meta[c_cols].as_matrix())
d5_f_train, d5_f_test, d5_c_train, d5_f_test = train_test_split(f_data, d5_c_data)

print "running model with 5 bins..."
clf = svm.SVC()
clf = clf.fit(d5_f_train, d5_c_train)
predicted = clf.predict(d5_f_test)
accuracy = r2_score(d5_c_test, predicted)
print "R2 :", accuracy
