import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

file_name = "cleanedData.csv"

##VARIABLES TO MODIFY
labelOne = 'budget'
labelTwo = 'revenue'
classDet = 'vote_average'
classPar = 6.0
#####################

cols=[labelOne, labelTwo, classDet]

meta = pd.read_csv(file_name, usecols=cols)

meta = meta.query(labelOne+' > 0')
meta = meta.query(labelTwo+' > 0')

meta = meta.sample(frac=1.0)

classOneX = []
classOneY = []

classTwoX = []
classTwoY = []

for index, row in meta.iterrows():
	if row[classDet] >= classPar:
		classOneX.append(row[labelOne])
		classOneY.append(row[labelTwo])
	else:
		classTwoX.append(row[labelOne])
		classTwoY.append(row[labelTwo])
print("done")

msize = 1.0
plt.plot(classOneX, classOneY, 'rp', classTwoX, classTwoY, 'bp', markersize=msize)
plt.title('red >='+str(classPar)+' :: blue <'+str(classPar))
plt.xlabel(labelOne)
plt.ylabel(labelTwo)
plt.show()