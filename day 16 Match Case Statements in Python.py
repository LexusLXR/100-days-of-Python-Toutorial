# Match case statement
x = 99
match x:
    case 1:
        print("x is one")
    case 60:
        print("x is sixty")
    case _ if x<10:
        print("x is smaller than 10")
    case _:
        print(x)

