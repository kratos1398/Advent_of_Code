
# everything is same as first lvl, only thing different is calcuationg of bow and ribbon


def elf_math(n):
	n = [int(x) for x in n] # this was the most important line ever. This changes every value in list from string to int. 
	bow = n[0] * n[1] * n[2] # the bow is simply the volume. if present is 2x4x3. Then bow length would be 24
	n.sort()
	ribbon = n[0] + n[0] + n[1] + n[1] # first we sort, then we take the perimiter of smallest side. For ex, if present is 2x4x3, then permiter is 2 + 2 + 3 + 3 = 10
	total = bow + ribbon
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
print("The total amount of square feet of ribbon we need is: {}".format(big_total))

elf_file.close()
