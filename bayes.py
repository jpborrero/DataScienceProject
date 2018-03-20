
def getScore(scoring_feature, value):
	for category in scoring_feature:
		if float(value) >= scoring_feature[category]['lower'] and float(value) < scoring_feature[category]['upper']:
			return category

def trainNB(train_values, train_labels, classifier_index, scoring_feature, scoring_label, cont_indexes, cont_features):
	
	features = {}
	
	for label in train_labels:
		features[label] = {}
		
	for key in features:
		if key != train_labels[classifier_index]:
			label_index = train_labels.index(key)
			if cont_indexes.count(train_labels[label_index]) == 0:
				vlength = len(train_values)
				for row_index in range(0, vlength):
					features[train_labels[label_index]][train_values[row_index][label_index]] = dict(scoring_label)
			else:
				for key in cont_features[train_labels[label_index]]:
					features[train_labels[label_index]][key] = dict(scoring_label)
				
	features[train_labels[classifier_index]] = dict(scoring_label)
		
	for value in train_values:
		
		category = getScore(scoring_feature, value[classifier_index])
		features[train_labels[classifier_index]][category] += 1

		value_length = len(value)
		for index in range(0, value_length):
			if index != classifier_index:
				if cont_indexes.count(train_labels[index]) == 0:
					feature = value[index]
					
					features[train_labels[index]][feature][category] += 1
					
				elif (value[index] is float):
					feature = float(value[index])
					for key in cont_features[train_labels[index]]:	
						if feature > cont_features[train_labels[index]][key]['lower'] and feature <= cont_features[train_labels[index]][key]['upper']:
						
							features[train_labels[index]][key][category] += 1
							
							
			
	return features

def classifyNB(features, test_value, test_labels, classifier_index, scoring_feature, scoring_label, cont_indexes, cont_features):
	
	total_score = dict(scoring_label)
	prob_score = dict(scoring_label)
	total = 0
	
	for label in scoring_label:
		total_score[label] = features[test_labels[classifier_index]][label]
		total += features[test_labels[classifier_index]][label]
		
	for label in scoring_label:
		prob_score[label] = total_score[label] / total

	vlength = len(test_value)
	for index in range(0, vlength):
		if index != classifier_index:
			if cont_indexes.count(test_labels[index]) == 0:
				feature = test_value[index]
				
				#pos_prob = pos_prob * ( features[test_labels[index]][feature][p] / total )
				#neg_prob = neg_prob * ( features[test_labels[index]][feature][n] / total )
				
				for label in scoring_label:
					prob_score[label] = prob_score[label] * ( features[test_labels[index]][feature][label] / total )
				
			elif (test_value[index] is float):
				feature = float(test_value[index])
				for key in cont_features[test_labels[index]]:
					if feature > cont_features[test_labels[index]][key]['lower'] and feature <= cont_features[test_labels[index]][key]['upper']:
					
						#pos_prob = pos_prob * ( features[test_labels[index]][key][p] / total )
						#neg_prob = neg_prob * ( features[test_labels[index]][key][n] / total )
						
						for label in scoring_label:
							prob_score[label] = prob_score[label] * ( features[test_labels[index]][key][label] / total )
		
	return prob_score
	
def testNB(features, test_values, test_labels, classifier_index, scoring_feature, scoring_label):

	results = []

	line_index = 1
	for test_value in test_values:
		result = classifyNB(features, test_value, test_labels, classifier_index, scoring_feature, scoring_label, cont_indexes, cont_features)
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