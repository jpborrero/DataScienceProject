import numpy as np
import pandas as pd
from scipy import stats

file_name = 'cleanedData.csv'

##MODIFY THIS VARIABLE
attrX = 'vote_average'
######################

column_names_retrieved = [attrX]
filters = [attrX+' > -1']
df = pd.read_csv(file_name , usecols=column_names_retrieved)

#apply filters
df_f = df
for filter in filters:
	df_f = df_f.query(filter)

column = df_f[attrX]

column_mean = np.mean(column)
column_std = np.std(column)
column_median = np.median(column)
column_mode_value = stats.mode(column)[0][0]
column_mode_count = stats.mode(column)[1][0]
mode_perc_of_pop = column_mode_count / len(column)

print(attrX)
print('mean: ', column_mean)
print('std: ', column_std)
print('median: ', column_median)
print('mode value: ', column_mode_value)
print('mode count: ', column_mode_count)
print('perc of pop: ', mode_perc_of_pop)