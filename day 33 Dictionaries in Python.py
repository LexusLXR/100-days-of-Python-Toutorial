dict = {
    "Kage" : "A Progammer and a Gamer",
    "Piyush" : "A Normmal person"
}

print(dict["Kage"])


info = {
    "name":'Karan',
    "age" : 19 , 
    "eligible" : True
}

print(info)
print(info["name"])
print(info.get("name"))
print(info.keys())
print(info.values())


for keys in info.keys():
    print(f"The Value of the corresponding values of the {keys} is {info[keys]}")

print(info.items())
for key , value in info.items():
    print(f"The Value of the corresponding values of the {keys} is {value}")
