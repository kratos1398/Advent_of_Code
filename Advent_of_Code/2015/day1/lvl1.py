import sys

santa_floors = open("santa.txt","r")
count = 0
lines = santa_floors.readlines() # this puts entire file into list. each line is a element
for line in lines: # reads list as string. Reads one line at a time
	for subline in line: # its a for loop within a for loop causes to read one character at a time
		if subline == "(":
			count = count+1
		if subline == ")":
			count = count-1
print(count)
santa_floors.close()

