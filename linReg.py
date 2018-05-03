
#https://pythonspot.com/linear-regression/
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

#https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib
def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l

#filters apply data filters, reference pandas .query()
def scatterPlotTwoFeatures(dataFile, attrX, attrY, attrOther, numFilters, catFilters):

	# load csv with columns
	columns = [attrX, attrY]
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
		
	df_f = df_f.sample(frac=1)
	
	print("rows used:", len(df_f), "rows")
	
	Y = df_f[attrY]
	X = df_f[attrX]

	X=X.values.reshape(len(X),1)
	Y=Y.values.reshape(len(Y),1)

	#split
	split_value = 1/10
	lendf = int((len(df_f.index))*(split_value))
	X_train = X[:-lendf]
	X_test = X[-lendf:]
	Y_train = Y[:-lendf]
	Y_test = Y[-lendf:]
	
	print("train used:", len(X_train), "rows")
	print("test used:", len(Y_test), "rows")
	
	#plot
	plt.scatter(X_test, Y_test, color='black', marker='.')
	p1 = [0, 0]
	p2 = [0, 10]
	newline(p1,p2)
	plt.suptitle(str(attrX)+' v. '+str(attrY))
	plt.title(str(numFilters)+str(catFilters))
	plt.xlabel(attrX)
	plt.ylabel(attrY)

	
	# Create linear regression 
	regr = linear_model.LinearRegression()
	regr.fit(X_train, Y_train)
	score = regr.score(X_test, Y_test)
	print('score:', score)
	plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
	
	#optionally save graph immediately using line below, uncomment
	#plt.savefig('linReg_fig_missing_values/'+attrX+'_'+attrY+'.png')
	
	plt.show()
	
	
	
#viable features to use with linear regression below
#budget,popularity,revenue,runtime,vote_count,vote_average

#first var is data file, second var is independent var, third var is dependent var, fourth is list of filters




##MODIFY 'attrX' TO CHANGE INDEPENDT VARIABLE OF LINEAR REGRESSION
attrX = 'budget'
##################################################################
##MODIFY 'attrX' TO CHANGE INDEPENDT VARIABLE OF LINEAR REGRESSION
attrY = 'vote_average'
##################################################################


upper_bounds = 10
other = ['genres']
numericals = [attrX+' > -1', attrY+' > -1']
categoricals = {}
scatterPlotTwoFeatures('cleanedData.csv', attrX, attrY, other, numericals, categoricals)





