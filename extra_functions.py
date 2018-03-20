import pandas as pd

def formColumn

def filter(df, filters):

	df_f = df
	for filter in filters:
		df_f = df_f.query(filter)
		
