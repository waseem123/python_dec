mylist = [20,40,60,80,100]
print(mylist)

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])


print("USING FOR LOOP")
# Using For Loop
for x in mylist:
	print(x,end=" ")
print("++++++++")
students = ["Alex","Peter","John","Steve","Bill"]
for s in students:
	print(s)
print("________________")

for x in range(0,len(students)):
	print(f"{x}->{students[x]}")

# Using While Loop
miran = 0
while miran<len(students):
	print(students[miran])
	miran=miran+1