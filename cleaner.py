#Cleaner function
import pandas as pd
import numpy as np
import json
import ast
import csv

file = 'movies_metadata.csv'  #CHANGE PATH
metadata = pd.read_csv(file, dtype={'budget':str, 'revenue':str, 'runtime':str}, low_memory=False)


def count_prod_comp(data):
	data = data.drop(['belongs_to_collection','homepage', 'imdb_id', 'overview', 'poster_path', 'status', 'tagline', 'video', 'title', 'release_date', 'spoken_languages', 'runtime', 'adult'], axis=1)
	prodCompDict = {}
	for  index, row in data.iterrows():
		try:
			prodCompStr = unicode(row['production_companies'], errors='ignore')   #PRODUCTION COMPANY IS IN JSON FORMAT
			jsonStr = ast.literal_eval(prodCompStr)
			json_data = json.dumps(jsonStr)
			prodComp = json.loads(json_data)
			if prodComp != []:
				if prodComp[0]['name'] in prodCompDict:
					prodCompDict[prodComp[0]['name']] += 1
				else:
					prodCompDict[prodComp[0]['name']] = 1
		except:
			continue

	return prodCompDict

def clean_movie_data(data, prodCompDict):
	data = data.drop(['belongs_to_collection','homepage', 'imdb_id', 'overview', 'poster_path', 'status', 'tagline', 'video', 'title', 'release_date', 'spoken_languages', 'runtime', 'adult'], axis=1)
	with open('cleanedData.csv', 'w') as csvfile:
		fieldnames = ['budget', 'genres', 'movieId', 'original_language', 'original_title','popularity', 'production_companies', 'production_countries', 'revenue', 'vote_average', 'vote_count']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for  index, row in data.iterrows():
			#BUDGET CLEANING
			try:										# ALL TYPES ARE STRING
				row['budget'] = float(row['budget'])
				if row['budget'] == 0:
					row['budget'] = -1
			except:
				row['budget'] = -1

			#ORIGINAL LANGUAGE CLEANING
			if type(row['original_language']) != str:			# SOME TYPES ARE FLOAT == NAN
				row['original_language'] = ''

			#POPULARITY CLEANING
			if type(row['popularity']) != float or row['popularity'] == None:    #ALL TYPES FLOAT
				row['popularity'] = -1
			if row['popularity'] == 0:
				row['popularity'] = -1

			#GENRE CLEANING
			jsonStr = ast.literal_eval(row['genres'])   #GENRE IS IN JSON FORMAT
			json_data = json.dumps(jsonStr)
			genres = json.loads(json_data)
			try:
				row['genres'] = genres[0]['name']
			except:
				row['genres'] = ''

			#PRODUCTION COMPANY CLEANING
			try:
				prodCompStr = unicode(row['production_companies'], errors='ignore')   #PRODUCTION COMPANY IS IN JSON FORMAT
				jsonStr = ast.literal_eval(prodCompStr)
				json_data = json.dumps(jsonStr)
				prodComp = json.loads(json_data)
				try:
					if prodCompDict[prodComp[0]['name']] >= 50:
						row['production_companies'] = prodComp[0]['name']
					else:
						row['production_companies'] = 'Other'
				except:
					row['production_companies'] = ''
			except:
				row['production_companies']=''

			#PRODUCTION COUNTRY CLEANING
			try:
				prodCountryStr = unicode(row['production_countries'], errors='ignore')    #PRODUCTION COUNTRY IS IN JSON FORMAT
				jsonStr = ast.literal_eval(prodCountryStr)
				json_data = json.dumps(jsonStr)
				prodCountry = json.loads(json_data)
				try:
					row['production_countries'] = prodCountry[0]['name']
				except:
					row['production_countries'] = ''
			except:
				row['production_countries'] = ''

			#REVENUE CLEANING
			if type(row['revenue']) == float:			#SOME TYPES FLOAT == NAN
				row['revenue'] = -1
			try:
				row['revenue'] = float(row['revenue'])
			except:
				row['revenue'] = -1
			if row['revenue'] == 0:
				row['revenue'] = -1

			#VOTE AVERAGE CLEANING
			if type(row['vote_average']) != float or row['vote_average'] == None:    #ALL TYPES FLOAT
				row['vote_average'] = -1
			if row['vote_average'] == 0:
				row['vote_average']=-1

			#VOTE COUNT CLEANING
			if type(row['vote_count']) != float or row['vote_count'] == None:    #ALL TYPES FLOAT
				row['vote_count'] = -1
			if row['vote_count'] == 0:
				row['vote_count']=-1

			writer.writerow({'budget':row['budget'], 'genres':row['genres'], 'movieId':row['movieId'], 'original_language':row['original_language'], 'original_title':row['original_title'], 'popularity':row['popularity'], 'production_companies':row['production_companies'], 'production_countries':row['production_countries'], 'revenue':row['revenue'], 'vote_average':row['vote_average'], 'vote_count':row['vote_count']})

prodCompDict = count_prod_comp(metadata)
clean_movie_data(metadata, prodCompDict)
