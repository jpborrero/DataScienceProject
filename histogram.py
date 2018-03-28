import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def makeHisto(dataFile, attrX, attrOther, filters, ranges):
	columns = [attrX]
	for attr in attrOther:
		columns.append(attr)

	df = pd.read_csv(dataFile, usecols=columns)
	
	#apply filters
	df_f = df
	for filter in filters:
		df_f = df_f.query(filter)
	
	X = df_f[attrX]
	
	plt.figure()
	
	if ranges is None:
		X.plot.hist(alpha=0.5)
	else:
		X.plot.hist(range=ranges, alpha=0.5)
	
	plt.show()
	
#list of vars
#,adult,budget,genres,id,original_language,original_title,popularity,production_companies
#,production_countries,release_date,revenue,runtime,spoken_languages,vote_average,vote_count
	
makeHisto('cleanedData.csv', 'vote_average', [], ['vote_average >= 0'], None)