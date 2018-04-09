import math
import re
import json

#bins = {'<5.0>':5.0, '<10.0>':10.0}
#bins = {'<3.3>':3.3, '<6.6>':6.6, '<10.0>':10.0}
bins = {'<2.5>':2.5, '<5.0>':5.0, '<7.5>':7.5, '<10.0>':10.0}
#bins = {'<2>':2.0, '<4.0>':4.0, '<6.0>':6.0, '<8.0>':8.0, '<10.0>':10.0}
#bins = {'<1.0>':1.0, '<2>':2.0, '<3.0>':3.0, '<4.0>':4.0, '<5.0>':5.0, '<6.0>':6.0, '<7.0>':7.0, '<8.0>':8.0, '<9.0>':9.0, '<10.0>':10.0}


def AverageParser(data):
	if data == 0.0:
		return -1
	num = data
	try:
		num = float(num)
		r1 = int(math.ceil(num))
	except ValueError:
		r1 = -1
	return r1
	
def JSONParser(data):
	if data == '[]':
		return -1
	data = re.sub(r', \'name\': [^}]*', '', data)
	data = data.replace('\'', '"')
	j1 = json.loads(data)
	return j1
	
def getPrimary(data):
	pass

def binner(flt):

	global bins

	for bin in bins:
		if flt <= bins[bin]:
			return bin
	print("a bad happened!!!")
	
def BinParser(data):
	if data == 0.0:
		return -1
	num = data
	try:
		num = float(num)
		r1 = binner(num)
	except ValueError:
		r1 = -1
	return r1
	