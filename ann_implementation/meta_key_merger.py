import numpy as np
import pandas as pd
import math
from extraparsers import *
import time

discretized = True

meta_filen = "movies_metadata.csv"
keyw_filen = "keywords.csv"

#'id', 'budget', 'revenue', 'popularity', 'adult', 'original_language', 'genres', 
#'production_companies', 'production_countries', 'vote_average', 'vote_count'

#cols_0 = ['id', 'vote_average', 'genres', 'production_companies']
cols_0 = ['id', 'vote_average', 'genres']
cols_1 = ['id', 'keywords']

#cont_cols = ['budget', 'revenue', 'popularity']

if discretized:
	#meta = pd.read_csv(meta_filen, usecols=cols_0, converters={'vote_average':BinParser, 'genres':JSONParser, 'production_companies':alternateJSONParser})
	meta = pd.read_csv(meta_filen, usecols=cols_0, converters={'vote_average':BinParser, 'genres':JSONParser})
else:
	meta = pd.read_csv(meta_filen, usecols=cols_0, converters={'vote_average':RegParser, 'genres':JSONParser})
keyw = pd.read_csv(keyw_filen, usecols=cols_1, converters={'keywords':JSONParser})

merged = meta.merge(keyw, on='id')

meta['id'] = meta['id'].apply(pd.to_numeric, errors='coerce', downcast='signed')
keyw['id'] = keyw['id'].apply(pd.to_numeric, errors='coerce', downcast='signed')
#meta[cont_cols] = meta[cont_cols].apply(pd.to_numeric, errors='coerce')

meta = meta[meta['vote_average'] != -1]
meta = meta[meta['genres'] != -1]
keyw = keyw[keyw['keywords'] != -1]

#meta[cont_cols] = meta[cont_cols].replace(0, np.nan)

#meta[cont_cols] = meta[cont_cols].interpolate(method='values')

merged = meta.merge(keyw, on='id')

#print(merged)

bins = ""

out_filen = "merged_metakey_cont.csv"
if discretized:
	out_filen = "merged_metakey_discBin"+bins+".csv"
merged.to_csv(out_filen, index=False)