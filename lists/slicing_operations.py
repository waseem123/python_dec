mylist = [20,40,60,80,100,120,140,160,180,200]
print(mylist)
print(mylist[0:1])
mylist.insert(0,mylist[0:1])
print(mylist)

mylist[0:5] = [1000,2000,3000,4000,5000,6000]
print(mylist)

del mylist[0:2]
print(mylist)