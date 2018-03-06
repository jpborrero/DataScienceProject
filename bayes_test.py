from bayes import *
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


score_c = {'0.0<>1.0':{'lower':0.0, 'upper':1.0}, '1.0<>2.0':{'lower':1.0, 'upper':2.0}, '2.0<>3.0':{'lower':2.0, 'upper':3.0}, 
'3.0<>4.0':{'lower':3.0, 'upper':4.0}, '4.0<>5.0':{'lower':4.0, 'upper':5.0}, '5.0<>6.0':{'lower':5.0, 'upper':6.0}, 
'6.0<>7.0':{'lower':6.0, 'upper':7.0}, '7.0<>8.0':{'lower':7.0, 'upper':8.0}, '8.0<>9.0':{'lower':8.0, 'upper':9.0},
'9.0<>10.0':{'lower':9.0, 'upper':10.0}}

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
pos_value = 5.0
neg_value = 5.0
cont_indexes = ['budget', 'popularity', 'revenue', 'runtime']
cont_features = {'budget':budget_c, 'popularity':popularity_c, 'revenue':revenue_c, 'runtime':runtime_c}
#print(train_labels)
features = trainNB(train_values, train_labels, classifier_index, pos_value, neg_value, cont_indexes, cont_features)

#print(train_features)

def resultClass(results):
	if results[0] > results[1]:
		return 'pos'
	else:
		return 'neg'

correct = 0
total = len(test_values)

for i in range(0, total):
	results = classifyNB(features, test_values[i], train_labels, classifier_index, pos_value, neg_value, cont_indexes, cont_features)
	'''
	print('finished...')
	print(train_values[i])
	print('above five likelyhood', results[0]/(results[0]+results[1]),'below five likelyhood', results[1]/(results[0]+results[1]))
	print(resultClass(results), float(results[0]))
	print('class: ', train_values[i][classifier_index])
	'''
	if resultClass(results) == 'pos' and float(test_values[i][classifier_index]) > 5.0:
		correct += 1
	if resultClass(results) == 'neg' and float(test_values[i][classifier_index]) <= 5.0:
		correct += 1
print('accuracy:', correct/total)
'''
row_num = 16
counter = 0
total = 0
maxy = 0
miny = 99999999999


count = 1
for row in data_meta:

	if count != 1:
		#print(row[2])
		if len(row) > 22:
			try:
				if float(row[row_num]) > 0.0:
					if float(row[row_num]) > maxy:
						maxy = float(row[row_num])
					if float(row[row_num]) < miny:
						miny = float(row[row_num])
					counter += 1
					total += float(row[row_num])
			except (ValueError):
				print(row)
	count += 1


print('max', maxy)
print('min', miny)
print('total', counter)
print('average', total / counter)
'''