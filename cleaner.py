import pandas as pd
import numpy as np

class Cleaner:
	def clean_movie_data(self, data):
		# return movie data, but without columns we don't need
		return data[['adult', 'budget', 'genres', 'id', 'imdb_id', 'production_companies', 'production_countries', 'revenue', 'runtime', 'spoken_languages', 'title']]
