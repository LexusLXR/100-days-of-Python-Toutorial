#Introduction to list in python

list1 = [1,2,3,4,5,6,7]
list2 = ["red","green","blue"]
print(list1)
print(list2)

#index accessing list in python

list3 = ["green", "yellow", "blue", "red"]

print(list3[2])

#negative indexing

print(list3[-4])

#checking items in list

if "yellow" in list3:
    print("yellow is present")
else:
    print("yellow is absent ")

#range in index
#list name[start:end:jump index]

print(list3[0:4:2])

#list comprihension 

colorwith_o = [item for item in list3 if "o" in item]
print(colorwith_o)