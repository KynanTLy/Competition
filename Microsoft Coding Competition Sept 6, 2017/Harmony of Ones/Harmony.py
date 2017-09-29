path = './Harmony-of-Ones_InputForSubmission_1.txt'
from collections import Counter
#This find where the file is located
import re


def compareBIT(longString, shortString):
	maxcount = 0
	for index in range(len(shortString)):
		
		if(shortString[index] == longString[index] and shortString[index] == '1'):
			maxcount += 1
	return maxcount

with open(path) as f:
	next(f)
	for line in f:
		integers_list = line.replace(",", " ").split()
		for i in range(len(integers_list)):

			integers_list[i] = (bin(int(integers_list[i]))[2:])[::-1]

		
		maxValue = 0
		if len(integers_list[0]) >= len(integers_list[1]):
			maxValue = compareBIT(integers_list[0], integers_list[1])	
		else:
			maxValue = compareBIT(integers_list[1], integers_list[0])	
		
		with open("answer.txt", 'a') as out:
			out.write(str(maxValue) + '\n')
    #bin(6)[2:]  
