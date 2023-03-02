mydict = {
	"name":"Akhila", 
	"college":"SPM",
	"qualification":"Diploma",
	"mobileno":9373504783,
	"passedout":True,
	"percentage":77.88
	}

print(mydict)

print("__________ONLY KEYS__________")
for i in mydict:
	print(i)

print("__________ONLY VALUES__________")
for i in mydict:
	print(f"{i}->{mydict[i]}")

print("__________ KEY LIST __________")
keys = mydict.keys()
print(list(keys))

print("__________ VALUES LIST __________")
values = mydict.values()
print(list(values))

print("__________ ITEMS LIST __________")
items = mydict.items()
print(list(items))

print("__________ ITEMS __________")
for i in mydict.items():
	print(i)

print("__________ ITEMS __________")
for i,j in mydict.items():
	print(f"{i}->{j}")	