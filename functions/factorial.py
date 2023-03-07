def getFactorial(number):
	fact = 1
	for i in range(2,(number+1)):
		fact *= i
	return fact

num = int(input("ENTER A NUMBER - "))
print(f"FACTORIAL OF {num} IS {getFactorial(num)}")