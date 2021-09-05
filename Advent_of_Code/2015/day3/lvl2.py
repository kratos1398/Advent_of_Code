direction = open("direction.txt","r")

big_list = []

elf_direction = direction.readlines()

for elf in elf_direction:
	for k in elf:
		big_list.append(k)
		
human_santa = {0:[0,0]}
robot_santa = {0:[0,0]}	
santa_ns = 0 # THese are treated as coordinates. If two entries have same coordinates, then we know its the same house. 
santa_ew = 0
robot_ns = 0
robot_ew = 0
house_number1 = 1
#house_number2 = 1
#---Here, for odd numbers that will be for human_santa, for even numbers it will be robot_santa. They will have their own coordinates
# and dictionary. The issue I had was using if if rather than if/else. 
for i in big_list:
	if i == '^':
		if house_number1 % 2 == 0:
			robot_ns = robot_ns + 1
			robot_santa[house_number1] = [robot_ns,robot_ew]
			house_number1 = house_number1+1
		else:
			santa_ns = santa_ns + 1
			human_santa[house_number1] = [santa_ns,santa_ew]
			house_number1 = house_number1+1
	if i == 'v':
		if house_number1 % 2 == 0:
			robot_ns = robot_ns - 1
			robot_santa[house_number1] = [robot_ns,robot_ew]
			house_number1 = house_number1+1
		else:
			santa_ns = santa_ns - 1
			human_santa[house_number1] = [santa_ns,santa_ew]
			house_number1 = house_number1+1
	if i == '>':
		if house_number1 % 2 == 0:
			robot_ew = robot_ew + 1
			robot_santa[house_number1] = [robot_ns,robot_ew]
			house_number1 = house_number1+1
		else:
			santa_ew = santa_ew + 1
			human_santa[house_number1] = [santa_ns,santa_ew]
			house_number1 = house_number1+1
	if i == '<':
		if house_number1 % 2 == 0:
			robot_ew = robot_ew - 1
			robot_santa[house_number1] = [robot_ns,robot_ew]
			house_number1 = house_number1+1
		else:
			santa_ew = santa_ew - 1
			human_santa[house_number1] = [santa_ns,santa_ew]
			house_number1 = house_number1+1


def remove_duplicates(input_dict): # this was important, we create a function that takes dict. If the value is not in this new dictionary, then we add to it. If the value is, then we simply dont do anything. This gets rid of all duplicates. 
	output_dict = {} 
	for key,value in input_dict.items(): 
		if value not in output_dict.values(): 
			output_dict[key] = value 
	return output_dict


# -- Here we are merging the 2 dictionaries together. Then we will get rid of all duplicates
human_santa.update(robot_santa)
#print(result1)
result3 = remove_duplicates(human_santa)
print("Together,Human Santa and Robot Santa vistied a total of {} houses".format(len(result3.keys())))

direction.close()

