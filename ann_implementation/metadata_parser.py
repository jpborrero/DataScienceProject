import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from extraparsers import BinParser, JSONParser

discretized = True

meta_filen = "movies_metadata.csv"

cols=['id', 'budget', 'revenue', 'popularity', 'adult', 'original_language', 'genres', 'production_companies', 'production_countries', 'vote_average', 'vote_count']
if discretized:
	meta = pd.read_csv(meta_filen, usecols=cols, converters={'vote_average':BinParser})
else:
	meta = pd.read_csv(meta_filen, usecols=cols)
cont_cols = ['budget', 'revenue', 'popularity', 'vote_count']
meta[cont_cols] = meta[cont_cols].apply(pd.to_numeric, errors='coerce')

meta = meta[meta['vote_average'] != -1]

meta = meta.replace(0, np.nan)

print('interpolation replacement...')

meta = meta.interpolate(method='values')

#print(meta)

out_file = "metadata_cleaned.csv"
if discretized:
	out_file = "metadata_cleaned_discretized.csv"
meta.to_csv(out_file, index=False)