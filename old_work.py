
"""
train_labels = []
train_features = []
train_class = []

test_features = []
test_class = []

in_file = "cleanedData.csv"

meta = open(in_file, "r", encoding = "latin 1")
data_meta = csv.reader(meta)

#0:budget,1:genres,2:movieId,3:original_language,4:original_title,5:popularity,6:production_companies
#,7:production_countries,8:revenue,9:runtime,10:vote_average,11:vote_count

#used_col = [0,1,3,5,6,7,8,10]
used_col = [0,5,8,9,11]
class_col = 10

genre_dict = {}
lang_dict = {}
pcomp_dict = {}
pcoun_dict = {}


for row in data_meta:
	genre_dict[row[1]] = 0
	lang_dict[[3]] = 0
	pcomp_dict[[6]] = 0
	pcoun_dict[[7]] = 0

print('searching data...')

parter = 20
parter_count = 0
stop = 10
start = True
for row in data_meta:

	#used_col = [0,5,8,10]
	if start:
		for i in range(0, len(used_col)):
			train_labels.append(row[used_col[i]])
			start = False
	else:
	
		flag = False
		for n in used_col:
			if row[n] == '-1':
				flag = True
				break
		if flag:
			continue
	
		if parter_count%parter == 0:
			test_entry = []
			for i in range(0, len(used_col)):
				input_value = float(row[used_col[i]])
				test_entry.append(input_value)
			test_features.append(test_entry)
			test_class.append(float(row[class_col]))
			parter_count+=1
		else:
			train_entry = []
			for i in range(0, len(used_col)):
				input_value = float(row[used_col[i]])
				train_entry.append(input_value)
			train_features.append(train_entry)
			train_class.append(float(row[class_col]))
			parter_count+=1

			
#print('length test',len(test_features),'length train',len(train_features))

def testCleanliness(train_features, train_class, test_features, test_class):
	print('train features is not nan: ', not np.any(np.isnan(train_features)))
	print('train features is finite: ', np.all(np.isfinite(train_features)))
	print('train class is not nan: ', not np.any(np.isnan(train_class)))
	print('train class is finite: ', np.all(np.isfinite(train_class)))
	print('test features is not nan: ', not np.any(np.isnan(test_features)))
	print('test features is finite: ', np.all(np.isfinite(test_features)))
	print('test class is not nan: ', not np.any(np.isnan(test_class)))
	print('test class is finite: ', np.all(np.isfinite(test_class)))

#exit()

#train_features = [[100000000,Adventure], [], []]
#train_class = [5.6, 7.8, 9.0, ...]
"""
