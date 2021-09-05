treeline_file = open("treeline.txt","r")
treeline_list = treeline_file.readlines()
my_list = []
duplicated_list = []
duplicate_count = 0
index_x = 0
index_y = 0
tree_counter = 0
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
	tree+tree 
	duplicated_list.append(tree) # this is simply duplicating a row many time to the right. The point of this is to make sure the program reaches the last row of the file. Basically having more columns than rows will help with this. 

try:
	while(duplicated_list[index_x] != None):
		if duplicated_list[index_x+1][index_y+3] == '#':
			tree_counter+=1
			#print("{} {} x_index: {} y_index:{}".format(tree_counter,duplicated_list[index_x+1][index_y+3], index_x+1,index_y+3))
		index_x+=1
		index_y+=3
except IndexError:
	pass


print("Based on the input file, the amount of tree's hit ('#') based on the slope right 3 and down 1 is {}".format(tree_counter))
print(duplicated_list[1][3])
treeline_file.close()
