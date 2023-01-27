# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
	for j in range(1,i+1):
		print(j,end=" ")
	print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6):
	for j in range(1,i+1):
		print(i,end=" ")
	print()

for i in range(1,6):
	for j in range(1,i+1):
		print(i+j,end=" ")
	print()

for i in range(1,6):
	for j in range(1,i+1):
		print(i*j,end=" ")
	print()