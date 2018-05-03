import math


def average(train_values, train_labels, feature_label, classifier_index, scoring_feature, score_label):
	
	summ = 0
	total = 0
	
	for value in train_values:
	
		cvalue_label = float(value[classifier_index])
		
		if cvalue_label >= scoring_feature[score_label]['lower'] and cvalue_label < scoring_feature[score_label]['upper']:
			index = train_labels.index(feature_label)
			if value[index] != '':
				summ = summ + float(value[index])
				total += 1
			
	ave = summ / total
	return ave

def averagesList(train_values, train_labels, feature_labels, classifier_index, scoring_feature, scoring_labels):
	
	averageList = {}

	for feature_label in feature_labels:
		averageList[feature_label] = {}
		for score_label in scoring_labels:
			averageList[feature_label][score_label] = average(train_values, train_labels, feature_label, classifier_index, scoring_feature, score_label)
			
	return averageList
	
def variance(train_values, train_labels, feature_label, classifier_index, scoring_feature, score_label, pres_ave=None):

	ave = pres_ave
	if pres_ave == None:
		ave = average(train_values, train_labels, feature_label, classifier_index, scoring_feature, score_label)

	summ = 0
	total = 0

	for value in train_values:
	
		cvalue_label = float(value[classifier_index])
		
		if cvalue_label >= scoring_feature[score_label]['lower'] and cvalue_label < scoring_feature[score_label]['upper']:
			index = train_labels.index(feature_label)
			if value[index] != '':
				summ = summ + (float(value[index]) - ave)**2
				total += 1
		
	varian = summ / total
	
	#stddev = math.sqrt(varian)
	return varian
	
def variancesList(train_values, train_labels, feature_labels, classifier_index, scoring_feature, scoring_labels):
	
	variancesList = {}

	for feature_label in feature_labels:
		variancesList[feature_label] = {}
		for score_label in scoring_labels:
			variancesList[feature_label][score_label] = variance(train_values, train_labels, feature_label, classifier_index, scoring_feature, score_label)
			
	return variancesList
	
def normDistApp(example_value, ave, varian):

	termone = ( 1 / (math.sqrt(2*math.pi*varian)))
	termtwo = math.exp(-(((example_value - ave)**2) / (2*varian)))
	prob = termone * termtwo
	
	return prob
	
	
	
	
	
	
	
	
	
	
	
	
	
	