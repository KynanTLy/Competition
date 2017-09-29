path = '/home/kynan/Desktop/Microsoft/Calendar-confusion_InputForSubmission_1.txt'
from collections import Counter
#This find where the file is located
import re


text_file = open(path,'r')

while True:
    line = text_file.readline()
    if not line: 
        break
    new_string = line.split()
  
    new_string[0] = re.sub('[^a-zA-Z0-9\n]', ' ', new_string[0]).split()
    new_string[1] = re.sub('[^a-zA-Z0-9\n]', ' ', new_string[1]).split()
    

    for i in range(0, 3):
   		new_string[2] = new_string[2].replace(str(new_string[1][i]) , str(new_string[0][i]))
   		
    with open("answer.txt", 'a') as out:
    	out.write(new_string[2] + '\n')