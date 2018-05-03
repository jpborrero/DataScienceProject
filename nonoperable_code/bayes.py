import gaussian as gs


def getScore(scoring_feature, value):
	for category in scoring_feature:
		if float(value) >= scoring_feature[category]['lower'] and float(value) < scoring_feature[category]['upper']:
			return category
	print("shouldn't be here")

def trainNB(train_values, train_labels, classifier_index, scoring_feature, scoring_dict, cont_indexes, cont_features, gauss = False):
	
	print('start train...')
	
	features = {}
	
	#instantiate list of features by feature label
	for label in train_labels:
		features[label] = {}
		
	#iterate through labels in features and instantiate attributes with correct dictionary label 'scoring_dict'
	for key in features:
		if key != train_labels[classifier_index]:
			label_index = train_labels.index(key)
			if cont_indexes.count(train_labels[label_index]) == 0:
				vlength = len(train_values)
				for row_index in range(0, vlength):
					features[train_labels[label_index]][train_values[row_index][label_index]] = dict(scoring_dict)
			else:
				for key in cont_features[train_labels[label_index]]:
					features[train_labels[label_index]][key] = dict(scoring_dict)
				
	features[train_labels[classifier_index]] = dict(scoring_dict)
		
		
	bad_count = 0
		
	#iterate through values in training values  for training
	for value in train_values:
		
		#get category for present value classifier score
		category = getScore(scoring_feature, value[classifier_index])
		features[train_labels[classifier_index]][category] += 1

		
		#go through other value features and apply count of presence
		value_length = len(value)
		for index in range(0, value_length):
			if index != classifier_index:
				#if feature is discrete
				if cont_indexes.count(train_labels[index]) == 0:
					feature = value[index]
					
					features[train_labels[index]][feature][category] += 1
				#if attribute is continuous
				elif value[index] != '':
					feature = float(value[index])
					for key in cont_features[train_labels[index]]:	
						if feature > cont_features[train_labels[index]][key]['lower'] and feature <= cont_features[train_labels[index]][key]['upper']:
						
							features[train_labels[index]][key][category] += 1
				else:
					print('bad count: ', bad_count)
					print('bad row: ', value)
					print('bad element: ', '"'+str(value[index])+'"', ' at ', index)
					bad_count += 1
					
							
							
			
	return features

def classifyNB(features, test_value, test_labels, classifier_index, scoring_feature, scoring_dict, cont_indexes, cont_features, gauss = False, averagesList = None, variancesList = None):
	
	total_score = dict(scoring_dict)
	prob_score = dict(scoring_dict)
	total = 0
	
	for label in scoring_dict:
		total_score[label] = features[test_labels[classifier_index]][label]
		total += features[test_labels[classifier_index]][label]
	
	for label in scoring_dict:
		prob_score[label] = total_score[label] / total

	vlength = len(test_value)
	for index in range(0, vlength):
		if index != classifier_index:
		
			if cont_indexes.count(test_labels[index]) == 0:
				feature = test_value[index]
				
				for label in scoring_dict:
					prob_score[label] = prob_score[label] * ( features[test_labels[index]][feature][label] / total )
				
			
			elif test_value[index] != '':
				example_value = float(test_value[index])
				
				
				if gauss:
					for label in scoring_dict:
						score_label = label
						feature_label = test_labels[index]
						prob_score[label] = prob_score[label] * gs.normDistApp(example_value, averagesList[feature_label][score_label], variancesList[feature_label][score_label])
					
				else:
					for key in cont_features[test_labels[index]]:

						if example_value > cont_features[test_labels[index]][key]['lower'] and example_value <= cont_features[test_labels[index]][key]['upper']:
							
							for label in scoring_dict:
								prob_score[label] = prob_score[label] * ( features[test_labels[index]][key][label] / total )
			else:
				print('bad row: ', test_value)
				print('bad element: ', '"'+str(test_value[index])+'"', ' at ', index)
		
	return prob_score
	
def testNB(features, test_values, test_labels, classifier_index, scoring_feature, scoring_dict):

	results = []

	line_index = 1
	for test_value in test_values:
		result = classifyNB(features, test_value, test_labels, classifier_index, scoring_feature, scoring_dict, cont_indexes, cont_features)
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