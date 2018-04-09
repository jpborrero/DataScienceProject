import numpy as np
import pandas as pd
import math
from extraparsers import BinParser, JSONParser
import time

discretized = True

meta_filen = "movies_metadata.csv"
keyw_filen = "keywords.csv"

cols_0 = ['id', 'vote_average', 'genres']
cols_1 = ['id', 'keywords']


if discretized:
	meta = pd.read_csv(meta_filen, usecols=cols_0, converters={'vote_average':BinParser, 'genres':JSONParser})
else:
	meta = pd.read_csv(meta_filen, usecols=cols, converters={'genres':JSONParser})
keyw = pd.read_csv(keyw_filen, usecols=cols_1, converters={'keywords':JSONParser})

merged = meta.merge(keyw, on='id')

meta['id'] = meta['id'].apply(pd.to_numeric, errors='coerce', downcast='signed')
keyw['id'] = keyw['id'].apply(pd.to_numeric, errors='coerce', downcast='signed')

meta = meta[meta['vote_average'] != -1]
meta = meta[meta['genres'] != -1]
keyw = keyw[keyw['keywords'] != -1]

merged = meta.merge(keyw, on='id')

#print(merged)

out_filen = "merged_metakey.csv"
if discretized:
	out_filen = "merged_metakey_discretized.csv"
merged.to_csv(out_filen, index=False)