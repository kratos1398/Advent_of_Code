

number_file = open("numbers.txt","r")

number_list = number_file.readlines()

for number in number_list:
	for number2 in number_list:
		for number3 in number_list:
			if int(number) + int(number2) + int(number3) == 2020:
				answer = int(number) * int(number2) * int(number3)
				print("{} + {} + {} = 2020 and thus, multiplied gets {}".format(number,number2,number3,answer))

number_file.close()
