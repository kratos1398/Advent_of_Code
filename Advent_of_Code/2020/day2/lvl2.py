# 1-11 s: sbssswsqsssssrlss is policy and password
# for this challenge, the 1 or 11 means a 's' has to be in the 1st position or 11th not both. 


password_file = open("password.txt","r")
total_valid_password_count = 0
password_list = password_file.readlines()
my_list = []
count = 0
for password in password_list:
	my_list.append(password.split(" "))
	


for password in my_list:
	password[1] = password[1].replace(':','')
	password[2] = password[2].replace('\n','')
	
for password in my_list:
	range_list = password[0].split("-")
	range_list[0] = int(range_list[0]) - 1 # the subtraction is go according with range. technically range 1 means index 0, so we need to subtract
	range_list[1] = int(range_list[1]) - 1
	if len(password[2]) > (int(range_list[1])): # need to make sure string is bigger than range, otherwise a index out of range error will happen
		if (password[2][int(range_list[0])] == password[1] and password[2][int(range_list[1])] != password[1]) or (password[2][int(range_list[0])] != password[1] and password[2][int(range_list[1])] == password[1]): # this is to make sure policy is correct
			count+=1
	else:
		if password[2][int(range_list[0])] == password[1]: # if the last range is bigger than string, then there is no need to check last range against string
			count+=1
			

print("The amount of valid password are {}".format(count))


