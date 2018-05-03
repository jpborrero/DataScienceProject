# DataScienceProject
## Project members
JP Borrero
Brandon Hansen
Mason Prosser

## Objective
Determine the features of movies that are most highly correlated to ratings, and create a classifier to predict movie ratings based on these features.

## Methods

## Dataset
Our data comes from a collection called "The Movies Dataset", available on Kaggle at the following link:
https://www.kaggle.com/rounakbanik/the-movies-dataset


## Code Use

Some of the scripts require different versions of Python to be run.
The Python version is specified in each instance.

#Histograms

Python Version 3.6.4

In order to reproduce the histograms generated in the project, please see the file 'histograms.py'.
The script may be readily run with the command: 
	python histograms.py

In order to generate seperate histograms of instances, modify the 'attrX' independent variable at the bottom of the file.
This variable can be found on line 40, viable features include: 
	budget, popularity, revenue, runtime, vote_count, vote_average

Optionally change 'bins' variable on line 46 to any range of positive integer values greater than 1.
If bins is modified to anything other then 10, then the variable range on line 44 must be set to a tuple (see code for details), otherwise should be set None.


#Linear Regression

Python Version 3.6.4

In order to reproduce the linear regressions generated in the project, please see the file 'linReg.py'.
The script may be readily run with the command: 
	python linReg.py
	
In order to generate seperate linear regression instances, modify the 'attrX' independent variable at the bottom of the file.
This variable can be found on line 100, viable features include: 
	budget, popularity, revenue, runtime, vote_count, vote_average

Optionally change 'attrY' dependent variable on line 103 to any of the above features to modify linear regression.

#Mean, Median, Mode

Python Version 3.6.4

In order to reproduce the mean, median, and mode generated in the project, please see the file 'mmm.py'.
The script may be readily run with the command: 
	python mmm.py

In order to generate seperate linear regression instances, modify the 'attrX' independent variable at the bottom of the file.
This variable can be found on line 8, viable features include: 
	budget, popularity, revenue, runtime, vote_count, vote_average
	
#Preliminary Clustering

Python Version 3.6.4

In order to reproduce the cluster generated in the project, please see the file 'basicCluster.py'.
The script may be readily run with the command: 
	python basicCluster.py
	
In order to generate seperate clusters of instances, modify the 'labelOne' and 'labelTwo' independent variables at the top of the file.
This variable can be found on line 9 and 10, viable features include: 
	budget, popularity, revenue, runtime, vote_count, vote_average
	
Optionally change 'classDet' variable on line 11 to any of the above features to modify cluster.
Optionally change 'classPar' variable on line 12 to any decimal value to modify cluster.


#MLP Classifier Using Genres and Keywords

Python Version 3.6.4

In order to reproduce the MLP keyword and genres results generated in the project, move to the folder 'ann_implementation'.
In this folder, please see the file 'ann_classifier.py'.
The script may be readily run with the command: 
	python ann_classifier.py
	
In order to generate results on different bin numbers, modify the variable 'bin_num' at the top of the file.
This variable can be found on line 20, viable values include: 
	2, 3, 4, 5, 10
