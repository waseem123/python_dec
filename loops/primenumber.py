num = 1999999
end = num//2
print(end)
flag = True
for i in range(2,end):
	if num%i==0:
		flag = False
		break

if flag==True:
	print("Number is PRIME")
else:
	print("Not a prime number")
	