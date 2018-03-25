
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
def scatterPlotTwoFeatures(dataFile, attrX, attrY, attrOther, filters):

	# load csv with columns
	columns = [attrX, attrY]
	for attr in attrOther:
		columns.append(attr)
		
	df = pd.read_csv(dataFile, usecols=columns)
	

	
	#apply filters
	df_f = df
	for filter in filters:
		df_f = df_f.query(filter)
	
	Y = df_f[attrY]
	X = df_f[attrX]

	X=X.values.reshape(len(X),1)
	Y=Y.values.reshape(len(Y),1)

	#split
	lendf = int((len(df_f.index))*(1/2))
	X_train = X[:-lendf]
	X_test = X[-lendf:]
	Y_train = Y[:-lendf]
	Y_test = Y[-lendf:]
	
	#plot
	plt.scatter(X_test, Y_test, color='black', marker='.')
	p1 = [0, 0]
	p2 = [0, 10]
	newline(p1,p2)
	plt.suptitle(str(attrX)+' v. '+str(attrY))
	plt.title(str(filters))
	plt.xlabel(attrX)
	plt.ylabel(attrY)

	
	# Create linear regression 
	regr = linear_model.LinearRegression()
	regr.fit(X_train, Y_train)
	plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
	
	plt.show()
	
	#make prediction with model
	#print( str(round(regr.predict(3.7*(10^8)))))
	
	

#list of vars
#,adult,budget,genres,id,original_language,original_title,popularity,production_companies
#,production_countries,release_date,revenue,runtime,spoken_languages,vote_average,vote_count


#scatterPlotTwoFeatures('cleanedData.csv', 'budget', 'revenue', ['budget>0', 'revenue>0'])

#first var is data file, second var is independent var, third var is dependent var, fourth is list of filters
scatterPlotTwoFeatures('cleanedData.csv', 'budget', 'revenue', [], ['budget >= 0', 'revenue >= 0'])










