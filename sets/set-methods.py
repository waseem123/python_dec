a = {1,2,3,4,5,6,7,8,9,10}
b = {2,4,6,8,10}
c = {1,3,5,7,9}

print(a.issuperset(b))
print(c.issubset(a))
print(b.isdisjoint(c))