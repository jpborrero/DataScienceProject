import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def makeHisto(dataFile, attrX, attrOther, numFilters, catFilters, ranges, bin_num):
	columns = [attrX]
	for attr in attrOther:
		columns.append(attr)

	df = pd.read_csv(dataFile, usecols=columns)
	
	#apply filters
	df_f = df
	for filter in numFilters:
		df_f = df_f.query(filter)
	
	for filter in catFilters:
		feature = filter
		attribute = catFilters[feature]
		df_f = df_f[df_f[feature] == attribute]
	
	X = df_f[attrX]
	
	plt.figure()
	
	if ranges is None:
		X.plot.hist(alpha=0.5)
	else:
		X.plot.hist(range=ranges, alpha=0.5, bins=bin_num)

	"""
	if ranges is None:
		plt.savefig('histogram_fig_missing_values/'+attrX+'-unbound.png')
	else:
		plt.savefig('histogram_fig_missing_values/'+attrX+'-bounds_'+str(ranges[0])+'_'+str(ranges[1])+'-bins_'+str(bin_num)+'.png')
	"""
	plt.show()
	
#list of vars
#,adult,budget,genres,id,original_language,original_title,popularity,production_companies
#,production_countries,release_date,revenue,runtime,spoken_languages,vote_count,vote_count

#budget, popularity,revenue,runtime,vote_count,vote_count

#PAY ATTENTION TO THESE COMMENTS
#change this to the feature name you want to look at
attrX = 'runtime'
#change this to the upper and lower bounds of hist, otherwise ranges = None for unbounded
ranges = (0, 200)
#number of bins
bin_num = 1000
other = ['genres']
numericals = [attrX+' > -1']
categoricals = {'genres':'Adventure'}
makeHisto('cleanedData.csv', attrX, ['genres'], numericals, categoricals, ranges, bin_num)