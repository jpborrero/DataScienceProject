#Cleaner function
import pandas as pd
import numpy as np


file = '/Users/jpborrero/Desktop/Data Science/Group Project/Data/movies_metadata.csv'  #CHANGE PATH
metadata = pd.read_csv(file, dtype={'budget':str, 'revenue':str, 'runtime':str}, low_memory=False)

#print metadata


def clean_movie_data(data):

	data = data.drop(['belongs_to_collection','homepage', 'imdb_id', 'overview', 'poster_path', 'status', 'tagline', 'video', 'title'], axis=1)
	for  index, row in data.iterrows():

		try:										# ALL TYPES ARE STRING
			row['budget'] = float(row['budget'])
		except:
			row['budget'] = 0
			#print row['original_title'], row['budget'], 'Fixed budget'


		if row['adult'] != False and row['adult'] != True:			#ALL TYPES BOOLEAN
			row['adult'] = False
			#print 'Fixed adult'


		if type(row['original_language']) != str:			# SOME TYPES ARE FLOAT == NAN
			row['original_language'] = ''
		#	print 'Fixed language', row['original_language']


		if type(row['popularity']) != float or row['popularity'] == None:    #ALL TYPES FLOAT
			row['popularity'] = 0
			#print row['original_title'], row['popularity'], 'Fixed popularity'


		if type(row['revenue']) == float:			#SOME TYPES FLOAT == NAN
			row['revenue'] = 0

		try:
			row['revenue'] = float(row['budget'])
		except:
			row['revenue'] = 0
			#print row['original_title'], row['revenue'], 'Fixed revenue'


		if type(row['runtime']) == float:		#SOME TYPES FLOAT == NAN
			row['runtime'] = 0

		try:
			row['runtime'] = float(row['runtime'])
		except:
			row['runtime'] = 0


		if type(row['vote_average']) != float or row['vote_average'] == None:    #ALL TYPES FLOAT
			row['vote_average] = 0


def merge(data1,data2):
	finaldf = pd.merge(movies_metadata)

1
2
3
4
result = pd.merge(user_usage,
                 user_device[['use_id', 'platform', 'device']],
                 on='use_id')
result.head()

clean_movie_data(metadata)

# class Cleaner:
# 	def clean_movie_data(self, data):
#  		# return movie data, but without columns we don't need
#  		return data[['adult', 'budget', 'genres', 'id', 'imdb_id', 'production_companies', 'production_countries', 'revenue', 'runtime', 'spoken_languages', 'title']]
