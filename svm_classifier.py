from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

print "setting up model..."
meta_filen = "discreteDataHeaders10binsRes.csv"

cols=['budget', 'revenue', 'popularity', 'vote_average', 'vote_count']
f_cols = ['budget', 'revenue', 'popularity', 'vote_count']
c_cols = ['vote_average']

meta = pd.read_csv(meta_filen, usecols=cols)
f_data = meta[f_cols].as_matrix()
c_data = np.ravel(meta[c_cols].as_matrix())

c_values = [0.1, 1.0, 10.0]

# Test on discretized data
f_train, f_test, c_train, c_test = train_test_split(f_data, c_data)
print "running model with 10 bins..."
for c in c_values:
	out = ""
	out += "C = " + str(c)
	clf = svm.SVC(C=c)
	clf = clf.fit(f_train, c_train)
	predicted = clf.predict(f_test)
	accuracy = accuracy_score(c_test, predicted)
	out += "; Acc = " + str(accuracy)
	print out
print

# Test on data sorted into 8 bins
d8_meta = meta
for val in d8_meta[c_cols]:
	if val < 1.25:
		val = 0.0
	elif val < 2.5:
		val = 1.25
	elif val < 3.75:
		val = 2.5
	elif val < 5.0:
		val = 3.75
	elif val < 6.25:
		val = 5.0
	elif val < 7.5:
		val = 6.25
	elif val < 8.75:
		val = 7.5
	else:
		val = 8.75

d8_c_data = np.ravel(d8_meta[c_cols].as_matrix())
d8_f_train, d8_f_test, d8_c_train, d8_c_test = train_test_split(f_data, d8_c_data)
print "running model with 8 bins..."
for c in c_values:
	out = ""
	out += "C = " + str(c)
	clf = svm.SVC(C=c)
	clf = clf.fit(d8_f_train, d8_c_train)
	predicted = clf.predict(d8_f_test)
	accuracy = accuracy_score(d8_c_test, predicted)
	out += "; Acc = " + str(accuracy)
	print out
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
for c in c_values:
	out = ""
	out += "C = " + str(c)
	clf = svm.SVC(C=c)
	clf = clf.fit(d4_f_train, d4_c_train)
	predicted = clf.predict(d4_f_test)
	accuracy = accuracy_score(d4_c_test, predicted)
	out += "; Acc = " + str(accuracy)
	print out
 
# Test on data sorted into 2 bins
# d2_meta = meta
# for val in d2_meta[c_cols]:
# 	if val < 5.0:
# 		val = 0.0
# 	else:
# 		val = 10.0
# d2_c_data = np.ravel(d2_meta[c_cols].as_matrix())
# d2_f_train, d2_f_test, d2_c_train, d2_f_test = train_test_split(f_data, d2_c_data)

# print "running model with 2 bins..."
# clf = svm.SVC()
# clf = clf.fit(d2_f_train, d2_c_train)
# predicted = clf.predict(d2_f_test)
# accuracy = r2_score(d2_c_test, predicted)
# print "R2 :", accuracy
