#Function argument and return statement
# def average(a, b):
#     print('The average is', (a + b)/2)

# average(9 , 1)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print('The average value is', sum/len(numbers))

average(5 , 6, 7)