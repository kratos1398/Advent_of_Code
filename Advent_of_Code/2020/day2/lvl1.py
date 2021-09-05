# a password looks like this 1-11 s: sbssswsqsssssrlss
# the password must have at least 1 s and at most 11 s. If it doesnt follow this range
# then the password doesnt follow the policy

password_file = open("password.txt","r")
total_valid_password_count = 0
password_list = password_file.readlines()
my_list = []
for password in password_list:
	my_list.append(password.split(" ")) # space is delimiter, one line is 3 elements
	


for password in my_list:
	password[1] = password[1].replace(':','')
	password[2] = password[2].replace('\n','')
	
for password in my_list:
	range_list = password[0].split("-") # dash is delimiter, first range is one element in list, and last range is 2nd element
	count = 0
	for c in password[2]: # iterates through string
		if c == password[1]:  #checks if each character in string matches the letter of the policy.
			count+=1
	if count >= int(range_list[0]) and count <= int(range_list[1]): # checks if count is within range.
		total_valid_password_count+=1
	
		
print("The amount of valid passwords are {}".format(total_valid_password_count))
