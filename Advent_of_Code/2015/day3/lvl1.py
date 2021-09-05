direction = open("direction.txt","r")

big_list = []

elf_direction = direction.readlines()

for elf in elf_direction:
	for k in elf:
		big_list.append(k)
		
total_calc = {0:[0,0]}	
house_count = 2
ns = 0 # THese are treated as coordinates. If two entries have same coordinates, then we know its the same house. 
ew = 0
house_number = 1
for i in big_list:
	if i == '^':
		ns = ns+1
		total_calc[house_number] = [ns,ew]
		house_number = house_number+1
	if i == 'v':
		ns = ns-1
		total_calc[house_number] = [ns,ew]
		house_number = house_number+1
	if i == '>':
		ew = ew+1
		total_calc[house_number] = [ns,ew]
		house_number = house_number+1
	if i == '<':
		ew = ew-1
		total_calc[house_number] = [ns,ew]
		house_number = house_number+1


def remove_duplicates(input_dict): # this was important, we create a function that takes dict. If the value is not in this new dictionary, then we add to it. If the value is, then we simply dont do anything. This gets rid of all duplicates. 
	output_dict = {} 
	for key,value in input_dict.items(): 
		if value not in output_dict.values(): 
			output_dict[key] = value 
	return output_dict


result = remove_duplicates(total_calc)
print("{} houses received at least one present.".format(len(result.keys())))

direction.close()

