from bayes import *
import gaussian as gs
import time
import csv

#0:budget,1:genres,2:movieId,3:original_language,4:original_title,5:popularity,
#6:production_companies,7:production_countries,8:revenue,9:runtime,10:vote_average,11:vote_count

budget_c = {'1<>21810503':{'lower':1.0, 'upper':218105023.0}, 
'21604277<>380000000':{'lower':21604277.0, 'upper':380000000.0}}

popularity_c = {'0<>2.92':{'lower':0.0, 'upper':16.0},
'2.92<>547.49':{'lower':16.0, 'upper':548}}

revenue_c = {'1<>68787390':{'lower':1.0, 'upper':68787390.0}, 
'68787390<>2787965087':{'lower':68787390.0, 'upper':2787965087.0}}

runtime_c = {'1<>97':{'lower':1.0, 'upper':200.0}, 
'97<>1256':{'lower':200.0, 'upper':1256.0}}


scoring_feature = {'0.0<>1.0':{'lower':0.0, 'upper':1.0}, '1.0<>2.0':{'lower':1.0, 'upper':2.0}, '2.0<>3.0':{'lower':2.0, 'upper':3.0}, 
'3.0<>4.0':{'lower':3.0, 'upper':4.0}, '4.0<>5.0':{'lower':4.0, 'upper':5.0}, '5.0<>6.0':{'lower':5.0, 'upper':6.0}, 
'6.0<>7.0':{'lower':6.0, 'upper':7.0}, '7.0<>8.0':{'lower':7.0, 'upper':8.0}, '8.0<>9.0':{'lower':8.0, 'upper':9.0},
'9.0<>10.0':{'lower':9.0, 'upper':11.0}}

scoring_dict = {'0.0<>1.0':0.0, '1.0<>2.0':0.0, '2.0<>3.0':0.0, 
'3.0<>4.0':0.0, '4.0<>5.0':0.0, '5.0<>6.0':0.0, 
'6.0<>7.0':0.0, '7.0<>8.0':0.0, '8.0<>9.0':0.0,
'9.0<>10.0':0.0}

print('getting data...')

meta = open("cleanedData.csv", "r", encoding="latin 1")
data_meta = csv.reader(meta)

train_labels = []
train_values = []

test_values = []

#0:budget,1:genres,2:movieId,3:original_language,4:original_title,5:popularity,
#6:production_companies,7:production_countries,8:revenue,9:runtime,10:vote_average,11:vote_count

features = [0, 1, 3, 5, 6, 7, 8, 9, 10, 11]
num_indexes = [0, 5, 8, 9, 11]

cont_indexes = ['budget', 'popularity', 'revenue', 'runtime']
cont_features = {'budget':budget_c, 'popularity':popularity_c, 'revenue':revenue_c, 'runtime':runtime_c}

print('searching data...')
parter = 20
parter_count = 0
stop = 10
count = 1
for row in data_meta:

	if count == stop:
		#break
		pass

	if count == 1:
		#train_labels = [row[0],row[2],row[7],row[10],row[15],row[16],row[22]]
		for index in features:
			train_labels.append(row[index])
	else:
		if '-1' not in row:
			entry = []
			for index in features:
				if index in num_indexes:
					entry.append(float(row[index]))
				else:
					entry.append(row[index])
			if parter_count%parter == 0:
				#test_values.append([row[0],row[2],row[7],row[10],row[15],row[16],row[22]])
				test_values.append(entry)
				parter_count+=1
			else:
				#train_values.append([row[0],row[2],row[7],row[10],row[15],row[16],row[22]])
				train_values.append(entry)
				parter_count+=1
	count += 1

print('length test',len(test_values),'length train',len(train_values))
	
classifier_index = 8
cont_indexes = ['budget', 'popularity', 'revenue', 'runtime']
cont_features = {'budget':budget_c, 'popularity':popularity_c, 'revenue':revenue_c, 'runtime':runtime_c}

features = trainNB(train_values, train_labels, classifier_index, scoring_feature, scoring_dict, cont_indexes, cont_features)

def resultClass(results, scoring_feature, actual):
	
	actual_label = ''
	predicted_label = ''
	greatest = 0.0
	for label in scoring_feature:
		if actual >= scoring_feature[label]['lower'] and actual < scoring_feature[label]['upper']:
			actual_label = label
		if results[label] > greatest:
			predicted_label = label
			greatest = results[label]
			
	if predicted_label == actual_label:
		return 1
	else:
		return 0

correct = 0
total = len(test_values)

print('testing...')

gauss = False
aveList = None
varList = None
if gauss:
	aveList = gs.averagesList(train_values, train_labels, cont_indexes, classifier_index, scoring_feature, scoring_dict)
	varList = gs.variancesList(train_values, train_labels, cont_indexes, classifier_index, scoring_feature, scoring_dict)

for i in range(0, total):
	results = classifyNB(features, test_values[i], train_labels, classifier_index, scoring_feature, scoring_dict, cont_indexes, cont_features, gauss, averagesList = aveList, variancesList = varList)

	add = resultClass(results, scoring_feature, float(test_values[i][classifier_index]))
	
	correct += add
print('accuracy:', correct/total)









