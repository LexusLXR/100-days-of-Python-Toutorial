tup = (1,2,76,342,32,"Green",True)
print(type(tup), tup)
print(len(tup))

print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[2])

if 76 in tup:
    print("Yes 76 is present in this tuple")

tup2 = tup[1:4]
print(tup2)