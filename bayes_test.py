from bayes import *
import gaussian as gs
import time
import csv

#'adult', 'budget', 'original_language', 'popularity', 'revenue', 'runtime', 'vote_average'

budget_c = {'1<>21604277':{'lower':1.0, 'upper':21604277.0}, 
'21604277<>380000000':{'lower':21604277.0, 'upper':380000000.0}}

popularity_c = {'0<>2.92':{'lower':0.0, 'upper':2.92},
'2.92<>547.49':{'lower':2.92, 'upper':547.49}}

revenue_c = {'1<>68787390':{'lower':1.0, 'upper':68787390.0}, 
'68787390<>2787965087':{'lower':68787390.0, 'upper':2787965087.0}}

runtime_c = {'1<>97':{'lower':1.0, 'upper':97.0}, 
'97<>1256':{'lower':97.0, 'upper':1256.0}}


scoring_feature = {'0.0<>1.0':{'lower':0.0, 'upper':1.0}, '1.0<>2.0':{'lower':1.0, 'upper':2.0}, '2.0<>3.0':{'lower':2.0, 'upper':3.0}, 
'3.0<>4.0':{'lower':3.0, 'upper':4.0}, '4.0<>5.0':{'lower':4.0, 'upper':5.0}, '5.0<>6.0':{'lower':5.0, 'upper':6.0}, 
'6.0<>7.0':{'lower':6.0, 'upper':7.0}, '7.0<>8.0':{'lower':7.0, 'upper':8.0}, '8.0<>9.0':{'lower':8.0, 'upper':9.0},
'9.0<>10.0':{'lower':9.0, 'upper':11.0}}

scoring_dict = {'0.0<>1.0':0.0, '1.0<>2.0':0.0, '2.0<>3.0':0.0, 
'3.0<>4.0':0.0, '4.0<>5.0':0.0, '5.0<>6.0':0.0, 
'6.0<>7.0':0.0, '7.0<>8.0':0.0, '8.0<>9.0':0.0,
'9.0<>10.0':0.0}

print('getting data...')

meta = open("movies_metadata.csv", "r", encoding="utf8")
data_meta = csv.reader(meta)

train_labels = []
train_values = []

test_values = []

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
		train_labels = [row[0],row[2],row[7],row[10],row[15],row[16],row[22]]
		#print(train_labels)
	else:
		if len(row) > 22:
			if parter_count%parter == 0:
				test_values.append([row[0],row[2],row[7],row[10],row[15],row[16],row[22]])
				parter_count+=1
			else:
				train_values.append([row[0],row[2],row[7],row[10],row[15],row[16],row[22]])
				parter_count+=1
	count += 1

print('length test',len(test_values),'length train',len(train_values))
	
classifier_index = 6
cont_indexes = ['budget', 'popularity', 'revenue', 'runtime']
cont_features = {'budget':budget_c, 'popularity':popularity_c, 'revenue':revenue_c, 'runtime':runtime_c}
print(train_labels)

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









