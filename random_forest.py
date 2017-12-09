#random Forest Algorithm on mushrooms classfication(poison or non-poison)
from random import seed
from random import randrange
from csv import reader
from math import sqrt



def load_csv(filename):
	dataset = list()
	#read the data inside
	with open(filename,'r') as file:
		csv_reader = reader(file)	
		for row in csv_reader:
			if not row:
				continue
		dataset.append(row)
	return dataset

seed(2)
filename = "mushrooms.csv"
dataset = load_csv(filename)
print("first line of dataset %s" %dataset[0]) #use %variable means %s = %variable
print("first element of dataset %c" %dataset[0][0])
total_feature = int((len(dataset[0])-1))
print("total feature is %d" %  total_feature)

