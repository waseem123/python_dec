num = int(input("ENTER NUMBER - "))
# 5*4*3*2*1 = 120
# 1*2*3*4*5 = 120

# n! = n*(n-1)*(n-2)*(n-3)*....*(n-(n-1))
# n! = 1*2*3*4*5*....n

fact = 1
for i in range(1,num+1):
	fact *= i
print(fact)