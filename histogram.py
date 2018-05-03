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

	plt.show()
	
#viable features to use with linear regression below
#budget, popularity,revenue,runtime,vote_count,vote_count




##MODIFY 'attrX' TO CHANGE INDEPENDT VARIABLE OF LINEAR REGRESSION
attrX = 'budget'
##################################################################

#change this to the upper and lower bounds of hist, otherwise ranges = None for unbounded
ranges = None #set a tuple with two integer values, both none negative with first less than second, example (0, 500)
#number of bins
bin_num = 20
other = ['genres']
numericals = [attrX+' > -1']
categoricals = {}
makeHisto('cleanedData.csv', attrX, ['genres'], numericals, categoricals, ranges, bin_num)