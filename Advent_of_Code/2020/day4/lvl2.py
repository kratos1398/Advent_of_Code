passport_file = open("passport.txt","r")

my_list = []
mystr = ""
for p in passport_file:
	my_list.append(p)
		
# the goal of all these list creations is to acheive an ideal formatting. We are given a batch file with many new lines, spaces, etc. The goal I want
# is to create a list of lists, and each list is a passport. To acheive this, we need to do alot of transformations.

my_list2 = []


for i in my_list:
	my_list2.append(i.split(" ")) # now its a list of list, each element is acheived by delimiter of a space, but there are new lines in batch file
					# so we have single elements in their own lists which we dont want. 

my_list3 = []
for i in my_list2:
	for k in i:
		my_list3.append(k)	# here we do a for loop within a for loop to iterate through every single element in my_list2
					# now we have a list (not a list of lists) that every single component of batch file is element. 
my_list4 = []				# ex; ["cid:rere","ein:ecefe","pass:dsdsd"]
for i in my_list3:
	if i == "\n":
		my_list4.append(i.replace("\n","@")) # replacing all blank elements with @
	else:
		my_list4.append(i) # this is all added to my_list4

my_list5 = ""		
for i in my_list4:
	my_list5+=i
	my_list5+=" "  # created a string and simply concatentated every element of my_list4 to my_list5 (which is a string)
	
my_list6 = []
my_list7 = []
my_list8 = []
my_list9 = []
my_list6 = my_list5.split("@") # we use @ as a delimiter, so list will look like ["cin:dsdsdsd ein:wdsdd fid:dwdwd "] 
for i in my_list6:
	my_list7.append(i.replace("\n","")) # get rid of all newlines and replace it with nothing
	
for i in my_list7:
	my_list8.append(i.split("\n")) # now we have acheived a list of lists by using the split for every newline.
					#so list is [["cin:dsdsdsd ein:wdsdd fid:dwdwd "],["cin:dsdsd ed:dddw dd:dede"]]
	 
for i in my_list8:
	for k in i:
		my_list9.append(k.split(" ")) # finally, we do a for loop within a for loop beacuse we are dealing with a list of lists
						# we use space as a delimiter which makes each string sepecrated by space into a element
						# in the list of lists
						# we offically got the lists of lists that we wanted.
x_axis = 0
y_axis = 0

try:
	for i in my_list9:
		for k in i:
			if k == '':
				del my_list9[x_axis][y_axis] # Here I am deleting all blank elements
			y_axis+=1
		y_axis = 0
		x_axis+=1
except IndexError:
	pass

valid_passport_counter = 0


for i in my_list9:
	if len(i) >= 7:
		valid_passport_counter+=1 # here simply counting any list with a length of 7 or more a valid passport
		
for i in my_list9:
	if len(i) == 7:
		for k in i:
			if 'cid:' in k:
				valid_passport_counter-=1 # here, I check for lists of length 7, then I see if there is any element
							  # that includes the string 'cid'. If it does, then its not valid and I decrement the counter

print("There are a total of {} valid passports in this batch file.".format(valid_passport_counter))

my_dict = {}
my_list10 = []
for i in my_list9:
	for k in i:
		k.split(":")

print(my_list9)


passport_file.close()
