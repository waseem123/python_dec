mydict = {
	"name":"Akhila", 
	"college":"SPM",
	"qualification":"Diploma",
	"mobileno":9373504783,
	"passedout":True,
	"percentage":77.88
	}

print(mydict)

mydict.pop("mobileno")
print(mydict)

mydict.popitem()
print(mydict)

del mydict['passedout']
print(mydict)

mydict.clear()
print(mydict)

del mydict
print(mydict)