# We can add the data in the list in two diffrent ways
# 1. Append -
# 	append() method adds the data in the end of the list
# 	name_of_list.append(actual_value)
# 2. Insert
# 	insert() method adds the data on any given index of the list
# 	it can add the data on any location within a list
# 	name_of_list.insert(index,actual_value)

mylist = [10,20,30,40,50,60]
print(mylist)

mylist.append(70)
mylist.append(80)
mylist.append(90)
mylist.append(100)
print(mylist)

mylist.insert(4,45)
print(mylist)

mylist.insert(0,5)
print(mylist)

mylist.insert(3,25)
print(mylist)

print(mylist.index(45))