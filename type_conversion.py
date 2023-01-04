num1 = input("ENTER FIRST NUMBER - ")
num2 = input("ENTER SECOND NUMBER - ")

print("BEFORE TYPE CONVERSION")
print(type(num1))
print(type(num2))

num1 = int(num1)
num2 = int(num2)

print("AFTER TYPE CONVERSION")
print(type(num1))
print(type(num2))

print(num1+num2)