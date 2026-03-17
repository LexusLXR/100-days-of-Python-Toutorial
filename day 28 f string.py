letter = "My Name is {} and i am from {}"
country = "India"
name = "Piyush"

print(letter.format(name, country))
print(f"Hey my name is {name} and i am from {country}")


price = 49.09999
txt = f"for only {price:.2f}"
print(txt)

print(f"{2*30}")
print(f"We use fString like this: Hey my name is {{name}} and i am from {{country}}")