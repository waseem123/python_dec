def myinfo(name, age, percentage, passed):
	return f"""My name is {name}. I am {age} years old.
I got {percentage}% in exam. 
Passing status - {passed}"""

print(myinfo("Alex",20,85.90,True))