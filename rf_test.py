from sklearn.ensemble import RandomForestRegressor
import numpy as np
import csv

train_labels = []
train_values = []
train_class = []

test_values = []
test_class = []

meta = open("cleanedData_cp.csv", "r", encoding = "latin 1")
data_meta = csv.reader(meta)

#used_col = [0,1,3,5,6,7,8,10]
used_col = [0,5,8,10]
class_col = 9

genre_dict = {}
lang_dict = {}
pcomp_dict = {}
pcoun_dict = {}

#0:budget,1:genres,2:movieId,3:original_language,4:original_title,5:popularity,6:production_companies,
#7:production_countries,8:revenue,9:vote_average,10:vote_count

"""
for row in data_meta:
	genre_dict[row[1]] = 0
	lang_dict[[3]] = 0
	pcomp_dict[[6]] = 0
	pcoun_dict[[7]] = 0
"""

print('searching data...')

parter = 20
parter_count = 0
stop = 10
start = True
for row in data_meta:

	#used_col = [0,5,8,10]
	if start:
		for i in range(0, len(used_col)):
			train_labels.append(row[used_col[i]])
			start = False
	else:
		try:
			if np.isnan(float(row[5])):
				print('nan: ', row[5])
		except ValueError:
				print('verror: ', row[5])
		if parter_count%parter == 0:
			test_entry = []
			for i in range(0, len(used_col)):
				input_value = float(row[used_col[i]])
				test_entry.append(input_value)
			test_values.append(test_entry)
			test_class.append(float(row[class_col]))
			parter_count+=1
		else:
			train_entry = []
			for i in range(0, len(used_col)):
				input_value = float(row[used_col[i]])
				train_entry.append(input_value)
			train_values.append(train_entry)
			train_class.append(float(row[class_col]))
			parter_count+=1

			
#print('length test',len(test_values),'length train',len(train_values))



print('train values is not nan: ', not np.any(np.isnan(train_values)))
print('train values is finite: ', np.all(np.isfinite(train_values)))
print('train class is not nan: ', not np.any(np.isnan(train_class)))
print('train class is finite: ', np.all(np.isfinite(train_class)))
print('test values is not nan: ', not np.any(np.isnan(test_values)))
print('test values is finite: ', np.all(np.isfinite(test_values)))
print('test class is not nan: ', not np.any(np.isnan(test_class)))
print('test class is finite: ', np.all(np.isfinite(test_class)))

#exit()

X= train_values
Y= train_class
clf = RandomForestRegressor(n_estimators = 10)
clf = clf.fit(X, Y)
print(clf.feature_importances_)
print(clf.predict(test_values))
