# 1 2 3 4 5
# 6 7 5 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
n=10
s = 1
for i in range(n):
	for j in range(n):
		print(f"{s}",end=" ")
		s+=1
	print()