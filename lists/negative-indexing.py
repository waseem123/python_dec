mylist = ["Waseem","Miran","Naved","Akhila","Tom","Jerry","Micky","Donald","Bhim","Motu"]

print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[-4])
print(mylist[-5])
print(mylist[-6])
print(mylist[-10])

print("____________________")

for i in range(1,len(mylist)+1):
	print(mylist[-i])
print("____________________")

i = 1
while(i<=len(mylist)):
	print(mylist[-i])
	i+=1