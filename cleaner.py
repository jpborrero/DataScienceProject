#Cleaner function
from __future__ import division
import pandas as pd
import numpy as np
import os
import json
import ast
import csv
import sys
import scipy.stats as st
import math
import os.path

file = 'movies_metadata.csv'  #CHANGE PATH
metadata = pd.read_csv(file, dtype={'budget':str, 'revenue':str, 'runtime':str}, low_memory=False)
data = metadata.drop(['belongs_to_collection','homepage', 'imdb_id', 'overview', 'poster_path', 'status', 'tagline', 'video', 'title', 'release_date', 'spoken_languages', 'adult'], axis=1)

#--------------------------
# FUNCTIONS
#--------------------------
# 1. GET AVERAGE FUNCTION TO FILL IN EMPTY CELLS
def get_average(col):
    average = 0
    sum = 0
    count = 0
    with open('tempData.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[col] != '-1':
                sum += float(row[col])
                count += 1
    average = sum/count
    return average

# 2. CREATE DICTIONARY WITH COUNT FOR PRODUCTION COMPANY OR PRODUCTION COUNTRY
def get_dictionary(data, col):
	Dict = {}
	for  index, row in data.iterrows():
		try:
			Str = unicode(row[col], errors='ignore')   #PRODUCTION COMPANY IS IN JSON FORMAT
			jsonStr = ast.literal_eval(Str)
			json_data = json.dumps(jsonStr)
			val = json.loads(json_data)
			if val != []:
				if val[0]['name'] in Dict:
					Dict[val[0]['name']] += 1
				else:
					Dict[val[0]['name']] = 1
		except:
			continue
	return Dict

# 3. CREATE ID DICTIONARY FOR GENRE, ORIGINAL LANGUAGE, PRODUCTION COUNTRY OR PRODUCTION COMPANY
def get_id_dictionary(col):
    Dict = {}
    id = 1
    with open('cleanedData.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[col] in Dict:
                continue
            else:
                Dict[row[col]] = id
                id += 1
	return Dict

# 4. CLEANING FUNCTION
def clean_movie_data(data, prodCompDict, prodCountryDict):
    with open('tempData.csv', 'w') as csvfile:
        fieldnames = ['budget', 'genres', 'movieId', 'original_language', 'original_title','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_average', 'vote_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for  index, row in data.iterrows():
            #BUDGET CLEANING
            try:										# ALL TYPES ARE STRING
                row['budget'] = float(row['budget'])
                if row['budget'] == 0:
                    row['budget'] = -1
            except:
                row['budget'] = -1

    		#ORIGINAL LANGUAGE CLEANING
            if type(row['original_language']) != str:			# SOME TYPES ARE FLOAT == NAN
                row['original_language'] = ''

    		#POPULARITY CLEANING
            if type(row['popularity']) != float or row['popularity'] == None:    #ALL TYPES FLOAT
                row['popularity'] = -1
            if row['popularity'] == 0:
                row['popularity'] = -1

    		#GENRE CLEANING
            jsonStr = ast.literal_eval(row['genres'])   #GENRE IS IN JSON FORMAT
            json_data = json.dumps(jsonStr)
            genres = json.loads(json_data)
            try:
                row['genres'] = genres[0]['name']
            except:
                row['genres'] = ''

    		#PRODUCTION COMPANY CLEANING
            try:
                prodCompStr = unicode(row['production_companies'], errors='ignore')   #PRODUCTION COMPANY IS IN JSON FORMAT
                jsonStr = ast.literal_eval(prodCompStr)
                json_data = json.dumps(jsonStr)
                prodComp = json.loads(json_data)
                try:
                    if prodCompDict[prodComp[0]['name']] >= 50:
                        row['production_companies'] = prodComp[0]['name']
                    else:
                        row['production_companies'] = 'Other'
                except:
                    row['production_companies'] = ''
            except:
                row['production_companies']=''

    		#PRODUCTION COUNTRY CLEANING
            try:
                prodCountryStr = unicode(row['production_countries'], errors='ignore')    #PRODUCTION COUNTRY IS IN JSON FORMAT
                jsonStr = ast.literal_eval(prodCountryStr)
                json_data = json.dumps(jsonStr)
                prodCountry = json.loads(json_data)
                try:
                    if prodCountryDict[prodCountry[0]['name']] >= 30:
                        row['production_countries'] = prodCountry[0]['name']
                    else:
                        row['production_countries'] = 'Other'
                except:
                    row['production_countries'] = ''
            except:
                row['production_countries'] = ''

    		#REVENUE CLEANING
            if type(row['revenue']) == float:			#SOME TYPES FLOAT == NAN
                row['revenue'] = -1
            try:
                row['revenue'] = float(row['revenue'])
            except:
                row['revenue'] = -1
            if row['revenue'] == 0:
                row['revenue'] = -1

            #RUNTIME CLEANING
            if type(row['runtime']) == float:            #SOME TYPES FLOAT == NAN
                row['runtime'] = -1
            try:
                row['runtime'] = float(row['runtime'])
            except:
                row['runtime'] = -1
            if row['runtime'] == 0:
                row['runtime'] = -1

            if row['vote_average'] == None:
                row['vote_average'] = 0

            writer.writerow({'budget':row['budget'], 'genres':row['genres'], 'movieId':row['movieId'], 'original_language':row['original_language'], 'original_title':row['original_title'], 'popularity':row['popularity'], 'production_companies':row['production_companies'], 'production_countries':row['production_countries'], 'revenue':row['revenue'], 'runtime':row['runtime'], 'vote_average':row['vote_average'], 'vote_count':row['vote_count']})

# 5. REPLACE EMPTY VALUES WITH AVERAGES, CLEAN AND SAVE FILE
def fill_empty_cells():
    averageBudget = get_average('budget')
    averagePop = get_average('popularity')
    averageRevenue = get_average('revenue')
    averageRuntime = get_average('runtime')
    with open('tempData.csv', 'rb') as infile, open('cleanedData.csv', 'wb') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['budget', 'genres', 'movieId', 'original_language', 'original_title','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_average', 'vote_count']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            new_row = row
            if row['budget'] == '-1':
                new_row['budget'] = averageBudget      # Fill missing data with averages
            if row['popularity'] == '-1':
                new_row['popularity'] = averagePop
            if row['revenue'] == '-1':
                new_row['revenue'] = averageRevenue
            if row['runtime'] == '-1':
                new_row['runtime'] = averageRuntime

            if new_row['vote_count'] != '0' or new_row['vote_average'] != '0':  #WE DONT WANT MOVIES WITH NO RATINGS WHATSOEVER
                writer.writerow({'budget':new_row['budget'], 'genres':new_row['genres'], 'movieId':new_row['movieId'], 'original_language':new_row['original_language'], 'original_title':new_row['original_title'], 'popularity':new_row['popularity'], 'production_companies':new_row['production_companies'], 'production_countries':new_row['production_countries'], 'revenue':new_row['revenue'], 'runtime':new_row['runtime'], 'vote_average':new_row['vote_average'], 'vote_count':new_row['vote_count']})

    os.remove('tempData.csv')


# 6. CHANGE STRING VARIABLES WITH CORRESPONDING INT IDS
def only_float_data(prodCompDict, prodCountryDict, genreDict, originalLanDict):
    with open('cleanedData.csv', 'rb') as infile, open('OnlyFloatsData.csv', 'wb') as outfile:
        reader = csv.DictReader(infile)
        # did not include header, movieid and original_title
        fieldnames = ['budget', 'genres', 'original_language','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_count', 'vote_average']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        #writer.writeheader()
        for row in reader:
            new_row = row
            new_row['genres'] = genreDict[row['genres']]
            new_row['original_language'] = originalLanDict[row['original_language']]
            new_row['production_countries'] = prodCountryDict[row['production_countries']]
            new_row['production_companies'] = prodCompDict[row['production_companies']]

            if new_row['vote_count'] != '0' or new_row['vote_average'] != '0':  #WE DONT WANT MOVIES WITH NO RATINGS WHATSOEVER
                writer.writerow({'budget':new_row['budget'], 'genres':new_row['genres'], 'original_language':new_row['original_language'], 'popularity':new_row['popularity'], 'production_companies':new_row['production_companies'], 'production_countries':new_row['production_countries'], 'revenue':new_row['revenue'], 'runtime':new_row['runtime'], 'vote_count':new_row['vote_count'], 'vote_average':new_row['vote_average']})

    os.remove('cleanedData.csv')  # Delete previous file

# 7. DISCRETIZE DATA (k bins)
def discrete_data(k, restriction):
    inc = 10/k
    res = ''
    if restriction == 1:
        res ='Res'

    with open('OnlyFloatsData.csv', 'rb') as infile, open('discreteData'+ str(k) +'bins'+res+'.csv', 'wb') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            new_row = row
            vote_average = float(row[9])
            for i in range(1,k+1):
                if vote_average > ((i-1)*inc) and vote_average <= (i*inc):
                    new_row[9] = i-1                    # ASSIGN TO BIN - BETTER THAN VOTE AVERAGE AS THERE IS NO OVERLAP WHEN ONLY CONSIDERING INTS
                    # new_row[9] = (i*inc) - inc/2      # ASSIGN VOTE AVERAGE SCORE
                    # new_row[9] = int(new_row[9])
                    break
                else:
                    continue

            if new_row[8] != '0' or new_row[9] != 0:  #WE DONT WANT MOVIES WITH NO RATINGS WHATSOEVER
                if restriction == 1:
                    vote_count = float(new_row[8])
                    if vote_count > 10:
                        writer.writerow(new_row)
                else:
                    writer.writerow(new_row)

# 8. DISCRETE DATA WITH HEADERS
def discrete_data_headers(k,restriction):
    res = ''
    if restriction == 1:
        res ='Res'

    with open('discreteData'+str(k)+'bins'+res+'.csv', 'rb') as infile, open('discreteDataHeaders'+ str(k) +'bins'+res+'.csv', 'wb') as outfile:
        reader = csv.reader(infile)
        fieldnames = ['budget', 'genres', 'original_language','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_count', 'vote_average']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow({'budget':row[0], 'genres':row[1], 'original_language':row[2], 'popularity':row[3], 'production_companies':row[4], 'production_countries':row[5], 'revenue':row[6], 'runtime':row[7], 'vote_count':row[8], 'vote_average':row[9]})



#------------------------
# MAIN FUNCTION THAT CALLS OTHER FUNCTIONS
#------------------------
def main(data):
    restriction = input("Restriction vote count greater than 10? Yes=1, No=0: ")
    print restriction
    print type(restriction)
    if os.path.isfile('OnlyFloatsData.csv') == True:
        # Discretize data, create bins for vote average
        for bins in range(2,11):
            #bins = input("Enter number of bins for vote average: ")
            discrete_data(bins,restriction)
            # Create a data file with header (necessary for some models we ran)
            discrete_data_headers(bins, restriction)

    else:
        # Create Production Company and Production COuntries Dictionaries
        prodCompDict = get_dictionary(data, 'production_companies')
        prodCountryDict = get_dictionary(data, 'production_countries')
        # Clean missing data, read json variables
        clean_movie_data(data, prodCompDict, prodCountryDict)
        # Fill empty variables, delete data points that do not have vote average and vote count
        fill_empty_cells()
        # Create ID dictionaries to replace strings with ids later
        genreIdDict = get_id_dictionary('genres')
        originalLanIdDict = get_id_dictionary('original_language')
        prodCompIdDict = get_id_dictionary('production_companies')
        prodCountryIdDict = get_id_dictionary('production_countries')
        # Replace string variables for ints (ids)
        only_float_data(prodCompIdDict, prodCountryIdDict, genreIdDict, originalLanIdDict)
        # Discretize data, create bins for vote average
        for bins in range(2,11):
            discrete_data(bins, restriction)
            # Create a data file with header (necessary for some models we ran)
            discrete_data_headers(bins, restriction)

# RUN MAIN FUNCT
main(data)
