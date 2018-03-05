import math

class Tree(object):
	def __init__(self, labels):
		self.feature = None
		self.value = None
		self.children = []
		self.indices = [x for x in range(0, len(labels))]
		self.prediction = None

	def find_gain_ratio(self, labels, feature):
		return (self.find_ig(labels, feature) / self.find_split_info(feature))

	def find_split_info(self, feature):
		result = 0.0
		tot = len(feature)
		for val in set(feature):
			val_count = 0.0
			for i in range(0, len(feature)):
				if (feature[i] == val):
					val_count = val_count + 1
			result = result - (val_count/tot * math.log(val_count/tot, 2))
		return result

	def find_ig(self, labels, feature):
		return (self.find_entropy(labels) - self.find_cond_entropy(labels, feature))

	def find_entropy(self, labels):
		lbl_dict = dict(set(labels), [0 for x in range(0, len(set(labels)))])
		tot = len(self.indices)
		for i in self.indices:
			lbl_dict[labels[i]] = lbl_dict[labels[i]] + 1

		result = 0.0
		for k, v in lbl_dict:
			if (v > 0):
				result = result + (-v/tot) * math.log(v/tot, 2)

	def find_cond_entropy(self, labels, feature):
		lbl_dict = dict(set(labels), [0 for x in range(0, len(set(labels)))])
		tot = len(self.indices)
		for i in self.indices:
			lbl_dict[labels[i]] = lbl_dict[labels[i]] + 1

		feat_vals = set(feature)
		result = 0.0
		for val in feat_vals:
			f_lbl_dict = dict(set(labels), [0 for x in range(0, len(set(labels)))])
			for i in self.indices:
				if (feature[i] == val):
					f_lbl_dict[labels[i]] = f_lbl_dict[labels[i]] + 1

			f_tot = 0
			for k, v in f_lbl_dict:
				f_tot = f_tot + v

			if (f_tot == 0):
				continue

			sub_result = 0.0
			for k, v in f_lbl_dict:
				if (v > 0):
					sub_result = sub_result - v/f_tot * math.log(v/f_tot, 2)
			result = result + f_tot/tot * sub_result

		return result

	def assign_prediction(self, labels):
		lbl_dict = dict(set(labels), [0 for x in range(0, len(set(labels)))])

		for i in self.indices:
			lbl_dict[labels[i]] = lbl_dict[labels[i]] + 1

		max_k = None
		max_v = 0
		for k, v in lbl_dict:
			if (v > max_v):
				max_k = k
				max_v = v

		self.prediction = max_k

	def predict(self, features, index):
		node = self
		while True:
			if (node.prediction != None or len(node.children) == 0):
				return node.prediction

			curr_feature = None
			for x in range(0, len(features)):
				if (node.feature == features[x].name):
					curr_feature = features[x]
			for child in node.children:
				if (child.value == curr_feature[index]):
					node = child

	def test(self, t_labels, t_features):
		predictions = []
		for i in range(0, len(t_labels)):
			predictions.append(self.predict(t_features, i))
		return predictions
