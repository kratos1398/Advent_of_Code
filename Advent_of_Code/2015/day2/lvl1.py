

def elf_math(n):
	n = [int(x) for x in n] # this was the most important line ever. This changes every value in list from string to int. 
	surface_area = 2*n[0]*n[1] + 2*n[1]*n[2] + 2*n[2]*n[0]
	n.sort()
	total = surface_area + (n[0] * n[1])
	return total	
	
	
elf_file = open("elves.txt","r")

elf_list = elf_file.readlines()
big_total = 0
big_list = []

for elf in elf_list:
	big_list.append(elf.split("x")) # 'x' is treated like the delimiter. 
	
for l in big_list:
	big_total += elf_math(list(l)) # here we are adding the value of this function to big_total. since we are using for loop, we need to convert to list since it is string when thru a for loop
	

	
list_t = [10,9,8]
list_t.sort()
print("The total amount of square feet of wrapping paper we need is: {}".format(big_total))

elf_file.close()
