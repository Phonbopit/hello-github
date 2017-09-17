import random
import time
import calendar
num = [1,2,3,4,5]
num1 = random.randrange(101)
print ('Here is Calendar:\n')
print (calendar.month(2016,4))
print (time.strftime("%Y-%m-%d"))
print (time.strftime("%H:%M:%S"))
x = (180+400)*150
y = 180*150
z = 600*150
print (x,y,z,num1)
a = 8
b = 0
for i in range(1,6):
    print (" "*a+"*"*i+"*"*b)
    a -= 1
    b += 1
