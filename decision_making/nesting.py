age = int(input("ENTER AGE - "))

if age>=18:
	vcard=input("DO YOU HAVE V CARD? (y -YES | n -NO) - ")
	print("Your age is valid")
	if vcard=="y":
		print("You are eligible to caste the vote")
	else:
		print("You dont have vcard. Unable to vote.")
else:
	print("You are not eligible.")