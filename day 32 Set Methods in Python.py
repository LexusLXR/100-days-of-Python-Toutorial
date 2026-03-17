# union methods

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

# Intersection Methods
s3 = {1,2,5,6}
s4 = {3,6,7}
print(s3.intersection(s4))
s3.intersection_update(s4)
print(s3, s4)

# symmetric difference 

cities1 = {"Tokyo", "Kolkata", "Delhi", "London"}
cities2 = {"Tokyo", "Newyork", "Paris", "Mumbai"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

#IsDisjoint():

cities1 = {"Tokyo", "Kolkata", "Delhi", "London"}
cities2 = {"Tokyo", "Newyork", "Paris", "Mumbai"}

print(cities1.isdisjoint(cities2))

#IsSuperSet():

cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}
cities2 = {"Tokyo", "Mumbai"}
print(cities1.issuperset(cities2))

#IsSubset():

cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}
cities2 = {"Tokyo", "Mumbai"}
print(cities2.issubset(cities1))


#Remove()
cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}
cities1.remove("Tokyo")
print(cities1)

#pop()

cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}
item = cities1.pop()
print(cities1)
print(item)

#del
cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}

del cities1

# print(cities1)

#clear()
cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}
cities1.clear()
print(cities1)

#if-else
cities1 = {"Tokyo", "Kolkata", "Delhi", "Mumbai"}

if "Tokyo" in cities1:
    print("Tokyo is present")
else:
    print("Tokyo is absent")





