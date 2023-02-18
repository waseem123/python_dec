# direct way to create a tuple
miran = (1,2,3,4,5)
print(miran)
print(type(miran))
print(len(miran))

# creating tuple using "tuple" constructor/function
x = tuple(("AKHILA","NAVID","MIRAN","WASEEM"))
print(x)
print(type(x))
print(len(x))

for i in x:
	print (i)
print("____________________")
for i in range(len(x)):
	print(f"{i} -> {x[i]}")
print("____________________")
i = 0
while i<len(x):
	print(f"{i} -> {x[i]}")
	i+=1