import sys

santa_floors = open("santa.txt","r")
count = 0
total_count = 0
lines = santa_floors.readlines()
for line in lines:
	for subline in line:
		if subline == "(":
			count = count+1
			total_count = total_count + 1
		if subline == ")":
			count = count-1
			total_count = total_count + 1
		if count == -1:
			print("Santa went to basement at position {}".format(total_count))
print(count)
santa_floors.close()


