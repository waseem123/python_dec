n=int(input())
mylist=[]
for i in range(n):
	data =int(input())
	mylist.append(data)
print(mylist)
llist=[]
for i in mylist:
	r=i%10
	llist.append(r)
num=int("".join(map(str,llist)))
print(f"{num} is the number formed")
if num>1:
	for i in range(2,(num//2)+1):
		if (num%i)==0:
			print("IS NOT A MAGICAL ARRAY")
			break
	else:
		print("IS A MAGICAL ARRAY")
else:
	print("NOT A MAGICAL ARRAY")

