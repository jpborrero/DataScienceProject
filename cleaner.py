#Cleaner function
import pandas as pd
import numpy as np
import json
import ast

file = 'movies_metadata.csv'  #CHANGE PATH
metadata = pd.read_csv(file, dtype={'budget':str, 'revenue':str, 'runtime':str}, low_memory=False)


def clean_movie_data(data):

	data = data.drop(['belongs_to_collection','homepage', 'imdb_id', 'overview', 'poster_path', 'status', 'tagline', 'video', 'title'], axis=1)
	for  index, row in data.iterrows():

		try:										# ALL TYPES ARE STRING
			row['budget'] = float(row['budget'])
		except:
			row['budget'] = 0


		if row['adult'] != False and row['adult'] != True:			#ALL TYPES BOOLEAN
			row['adult'] = False


		if type(row['original_language']) != str:			# SOME TYPES ARE FLOAT == NAN
			row['original_language'] = ''


		if type(row['popularity']) != float or row['popularity'] == None:    #ALL TYPES FLOAT
			row['popularity'] = 0


		if type(row['revenue']) == float:			#SOME TYPES FLOAT == NAN
			row['revenue'] = 0

		try:
			row['revenue'] = float(row['revenue'])
		except:
			row['revenue'] = 0


		if type(row['runtime']) == float:		#SOME TYPES FLOAT == NAN
			row['runtime'] = 0

		try:
			row['runtime'] = float(row['runtime'])
		except:
			row['runtime'] = 0


		if type(row['vote_average']) != float or row['vote_average'] == None:    #ALL TYPES FLOAT
			row['vote_average'] = 0

		jsonStr = ast.literal_eval(row['genres'])   #GENRE IS IN JSON FORMAT,
		json_data = json.dumps(jsonStr)
		genres = json.loads(json_data)

		try:
			row['genres'] = genres[0]['name']
			#print genres[0]['name']   #here it changes
		except:
			row['genres'] = 'No genre'

	#print data
	return data

meta = clean_movie_data(metadata)
#print meta
meta.to_csv('cleanedData.csv')

# class Cleaner:
# 	def clean_movie_data(self, data):
#  		# return movie data, but without columns we don't need
#  		return data[['adult', 'budget', 'genres', 'id', 'imdb_id', 'production_companies', 'production_countries', 'revenue', 'runtime', 'spoken_languages', 'title']]
