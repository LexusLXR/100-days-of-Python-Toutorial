countries = ("spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] ="Finland"
countries = tuple(temp)
print(countries) 


countries_1 = ("Pakistan", "Afganistan", "Bangladesh", "ShriLanka")

countries_2 = ("Vietnam", "India", "China")

southEastAsia = countries_1 + countries_2
print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 21, 3)
res = tuple1.count(3)
inx = tuple1.index(21)
inxsl = tuple1.index(3, 4, 8)

print('count of 3 in tuple1 is :', res)
print('index of 21 in tuple1 is :', inx)
print('index slicing of 3 in tuple1 is :', inxsl)
res = print(len(tuple1))