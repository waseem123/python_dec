mytuple = ("Akhila","Miran","Navid","Waseem")

print(mytuple)
# mytuple.append("Prem")
# mytuple.insert(2,"Prem")

lst = list(mytuple)
print(lst)
lst.append("Prem")
lst.insert(78,"Mr. Bean")
mytuple = tuple(lst)
print(mytuple)