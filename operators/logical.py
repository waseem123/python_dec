x = 100
y = 200
z = 50

# AND operation - denoted by 'and' keyword
print(x>y and x>z)
print(x<y and x>z)
print(x<y and x<z)
print(x>y and x<z)
print("____________________________")

# OR operation - denoted by 'or' keyword
print(x>y or x>z)
print(x>y or x<z)
print(x<y or x>z)
print(x<y or x<z)

# NOT operation - denoted by 'not' keyword
print("____________________________")
p = True
print(not(p))
print(not(False))
print(not(not(p)))
x = 100
y = 200
z = 50
print(not(x>y or x>z))
print(not(x>y) or x>z)
print(x<y and not(x<z))

