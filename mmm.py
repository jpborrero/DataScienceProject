import numpy as np
import pandas as pd
from scipy import stats

#list of vars
#,adult,budget,genres,id,original_language,original_title,popularity,production_companies
#,production_countries,release_date,revenue,runtime,spoken_languages,vote_average,vote_count

file_name = 'cleanedData.csv'
column_name_select = 'popularity'
column_names_retrieved = [column_name_select]
filters = [column_name_select+' > -1']
df = pd.read_csv(file_name , usecols=column_names_retrieved)

#apply filters
df_f = df
for filter in filters:
	df_f = df_f.query(filter)

column = df_f[column_name_select]

column_mean = np.mean(column)
column_median = np.median(column)
column_mode_value = stats.mode(column)[0][0]
column_mode_count = stats.mode(column)[1][0]
mode_perc_of_pop = column_mode_count / len(column)

print(column_name_select)
print('mean: ', column_mean)
print('median: ', column_median)
print('mode value: ', column_mode_value)
print('mode count: ', column_mode_count)
print('perc of pop: ', mode_perc_of_pop)