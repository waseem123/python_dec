N = int(input())
arr=[]

for i in range(N):
	data = int(input())
	arr.append(data)
	# arr.insert(i,data)

s = 0
for i in arr:
	if i%2==0:
		s+=(i*2)
	else:
		s+=(i*3)
print(s)