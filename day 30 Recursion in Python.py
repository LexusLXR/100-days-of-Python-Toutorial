def factorial(n):
    if(n==0 or n==1):
        return 1
    else: 
        return n * factorial(n-1)
    
print(factorial(3))

# 5* factorial(4)
# 5* 4 * factorial(3)
# 5* 4 * 3 * factorial(2)
# 5* 4 * 3 * 2 * factorial(1)
# 5* 4 * 3 * 2 * 1

# Quick quize: Write a program to print the Fibonnacci sequence 

def finonachi(n):
       if n == 0:
            return 0
       elif n == 1:
            return 1
       else:
            return finonachi(n-1) + finonachi(n-2)
       
num = 7

for i in range(num):
     print(finonachi(i))