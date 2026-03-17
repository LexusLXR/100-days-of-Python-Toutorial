import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if(timestamp <= '12:00:00'):
    print("Good moring")
elif(timestamp >= '12:00:00'):
    print("Good Afternoon")
elif(timestamp >= '18:00:00'):
    print("Good Evening")
elif(timestamp >= '22:00:00'):
    print("Good Night")
else:
    print("Invalid Time")

