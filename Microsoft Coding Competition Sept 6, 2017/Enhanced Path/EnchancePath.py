path = './dummy2.txt'
from collections import Counter
#This find where the file is located
import re

def checkWord(inputString):
	if(pathline[index][0:1] == "."):
		for i in range(len(inputString)):
			if(inputString[i] != inputString[0]):

				return False
		return True
	elif(len(pathline[index]) == 1 and pathline[index][0] == "*"):
		return True
	return False

with open(path) as f:
	for line in f:
		pathline = line.replace("\n", "").split('\\')[1:]
		#print(pathline)
		shortcut = ""
		index = 0
		while index < len(pathline):
			indexDel = []
			if checkWord(pathline[index]):
				if (pathline[index] == '*'):
					if(index == len(pathline) - 1):
						pathline = []
					else:
					#print(pathline)
						pathline = pathline[index+1:]
					#print(pathline)
				else:
					for i in range(len(pathline[index])):
						if index - i >= 0 and (index - i) not in indexDel:
							indexDel.append(index - i)
					if len(indexDel) != 0:
						#indexDel = sorted(indexDel, reverse=True)
						#print(indexDel)
						for element in indexDel:
							pathline.pop(element)
							index -= 1
			index += 1
		#print(pathline)
		#print(indexDel) 
		if not pathline or (len(pathline) == 1 and pathline[0] == ''):
			shortcut = "\\"
		else:
			for element in pathline:
				if(element != ''):
					shortcut +=  ("\\" + element)

		#print(pathline)
		print(shortcut)
		#print("=======")
		with open("answer.txt", 'a') as out:
			out.write(shortcut + '\n')