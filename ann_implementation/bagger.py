from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import pandas as pd
import time

def getDoc(data, feature):
	full_doc = []
	for index, row in data.iterrows():
		text = row[feature].replace('id', '')
		full_doc.append(text)
	return full_doc

def vectorizeDoc(full_doc):
	vectorizer = CountVectorizer()
	vectorizer.fit(full_doc)
	return vectorizer

def hashDoc(full_doc):
	vectorizer = HashingVectorizer(n_features = 20)
	vectorizer.fit(full_doc)
	return vectorizer

def getVectors(full_doc, vectorizer):
	vector = vectorizer.transform(full_doc)
	return vector.toarray()