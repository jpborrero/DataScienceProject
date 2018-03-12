
p = 'pos'
n = 'neg'

def trainNB(train_values, train_labels, classifier_index, pos_value, neg_value, cont_indexes, cont_features):
	
	global p
	global n
	
	features = {}
	
	for label in train_labels:
		features[label] = {}
		
	for key in features:
		if key != train_labels[classifier_index]:
			label_index = train_labels.index(key)
			if cont_indexes.count(train_labels[label_index]) == 0:
				vlength = len(train_values)
				for row_index in range(0, vlength):
					features[train_labels[label_index]][train_values[row_index][label_index]] = {p:0.0, n:0.0}
			else:
				for key in cont_features[train_labels[label_index]]:
					features[train_labels[label_index]][key] = {p:0.0, n:0.0}
				
	features[train_labels[classifier_index]] = {p:0.0, n:0.0}
		
	for value in train_values:
		
		pos = 0.0
		neg = 0.0
		
		if float(value[classifier_index]) > pos_value:
			pos = 1.0
		if float(value[classifier_index]) <= neg_value:
			neg = 1.0
			
		features[train_labels[classifier_index]][p] += pos
		features[train_labels[classifier_index]][n] += neg

		value_length = len(value)
		for index in range(0, value_length):
			if index != classifier_index:
				if cont_indexes.count(train_labels[index]) == 0:
					feature = value[index]
					features[train_labels[index]][feature][p] += pos
					features[train_labels[index]][feature][n] += neg
				elif (value[index] is float):
					feature = float(value[index])
					for key in cont_features[train_labels[index]]:	
						if feature > cont_features[train_labels[index]][key]['lower'] and feature <= cont_features[train_labels[index]][key]['upper']:
							features[train_labels[index]][key][p] += pos
							features[train_labels[index]][key][n] += neg
							
							
			
	return features

def classifyNB(features, test_value, test_labels, classifier_index, pos_value, neg_value, cont_indexes, cont_features):
	
	global p
	global n
	
	total_pos = features[test_labels[classifier_index]][p]
	total_neg = features[test_labels[classifier_index]][n]
	total = total_pos + total_neg
	
	pos_prob = total_pos / total
	neg_prob = total_neg / total

	vlength = len(test_value)
	for index in range(0, vlength):
		if index != classifier_index:
			if cont_indexes.count(test_labels[index]) == 0:
				feature = test_value[index]
				pos_prob = pos_prob * ( features[test_labels[index]][feature][p] / total )
				neg_prob = neg_prob * ( features[test_labels[index]][feature][n] / total )
			elif (test_value[index] is float):
				feature = float(test_value[index])
				for key in cont_features[test_labels[index]]:
					if feature > cont_features[test_labels[index]][key]['lower'] and feature <= cont_features[test_labels[index]][key]['upper']:
						pos_prob = pos_prob * ( features[test_labels[index]][key][p] / total )
						neg_prob = neg_prob * ( features[test_labels[index]][key][n] / total )
		
	return (pos_prob, neg_prob)
	
def testNB(features, test_values, test_labels, classifier_index, pos_value, neg_value):

	results = []

	line_index = 1
	for test_value in test_values:
		result = classifyNB(features, test_value, test_labels, classifier_index, pos_value, neg_value, cont_indexes, cont_features)
		results.append([line_index, result[0], result[1]])
		line_index += 1
		
	return results

'''
	
train_values = []
with open("simple_train.txt", 'r') as train:
	train_line = train.readline()
	while train_line != '':
		train_values.append(train_line.replace('\n', '').split(','))
		train_line = train.readline()

train_labels = ['1','2','3','4']
classify_index = len(train_labels) - 1
pos_value = 'y'
neg_value = 'n'

features = trainNB(train_values, train_labels, classify_index, pos_value, neg_value)
		
print(testNB(features, train_values, train_labels, classify_index, pos_value, neg_value))

'''