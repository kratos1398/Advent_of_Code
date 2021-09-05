treeline_file = open("treeline.txt","r")
treeline_list = treeline_file.readlines()
my_list = []
duplicated_list = []
duplicate_count = 0
for tree in treeline_list:
	my_list.append(tree.replace('\n',''))

for tree in my_list:
	tree+= tree
	tree+=tree
	tree+=tree
	tree+=tree
	tree+=tree
	tree+=tree
	tree+=tree
	tree+=tree
	tree+=tree
	duplicated_list.append(tree) # this is simply duplicating a row many time to the right. The point of this is to make sure the program reaches the last row of the file. Basically having more columns than rows will help with this. 

def airplane_tree_hit_fun(x,y):
	try:
		index_x = 0
		index_y = 0
		tree_counter = 0
		while(duplicated_list[index_x] != None):
			if duplicated_list[index_x+x][index_y+y] == '#':
				tree_counter+=1
			index_x+=x
			index_y+=y
	except IndexError:
		pass
	return tree_counter
# a function that takes in the slope as the paramter. 

total = airplane_tree_hit_fun(1,1) * airplane_tree_hit_fun(1,3) * airplane_tree_hit_fun(1,5) * airplane_tree_hit_fun(1,7) * airplane_tree_hit_fun(2,1)
print("Based on the input file, the amount of tree's hit ('#') based on the slope 1,1 1,3 1,5 1,7 and 2,1 and multiplied all together is {}".format(total))


treeline_file.close()
