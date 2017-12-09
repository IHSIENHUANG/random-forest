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
counter = 0
for row in dataset:
	#print("first line of dataset %s" %row) #use %variable means %s = %variable
	counter=counter+1
for num in range(100):
	print("test %s" %dataset[num])
print("total line is %d" %counter)
total_feature = int((len(dataset[0])-1))
print("total feature is %d" %  total_feature)

n_feature = 10 #number of feature in each random forest tree 


