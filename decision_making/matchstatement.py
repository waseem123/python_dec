print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print()
choice = int(input("ENTER YOUR CHOCIE - "))

match choice:
	case 1:
		x = 10
		y = 20
		print(f"Addition of {x} and {y} is {x+y}")

	case 2:
		x = 100
		y = 20
		print(f"Subtraction of {x} and {y} is {x-y}")


	case 3:
		x = 10
		y = 20
		print(f"Multiplication of {x} and {y} is {x*y}")


	case 4:
		x = 100
		y = 20
		print(f"Division of {x} and {y} is {x/y}")

	case _:
		print("INVALID CHOICE.")