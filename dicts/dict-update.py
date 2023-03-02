mydict = {
	"name":"Akhila", 
	"college":"SPM",
	"qualification":"Diploma",
	"mobileno":9373504783,
	"passedout":True,
	"percentage":77.88
	}

print(mydict)

mydict["college"] = "WIT"
print(mydict)
mydict.update({"qualification":"BE","percentage":90})
print(mydict)
