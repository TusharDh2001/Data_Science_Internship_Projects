'''There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet
in 1313 miles.'''

f=5280
m=1313
ans=f*m
print("Total feet n 1313 miles is: ",ans)

'''
Write a Python statement that calculates and prints the number of seconds in 77 hours, 2121 minutes
and 3737 seconds.
'''
h=77
m=2121
sec=3737
tmin=(h*60)+m
tsec=(tmin*60)+sec
print("Total seconds : ",tsec)

'''The distance between two points (x0,y0) and (x1,y1) is √ (x0−x1) 2 +(y0−y1)22. Write a Python
statement that calculates and prints the distance between the points (2, 2) and (5, 6).'''

x0=2
y0=2
x1=5
y1=6
n=int(((x0-x1)**2+(y0-y1)**2)**0.5)
print("Distance between 2 points :",n)

'''
Write a single Python statement that combines the three strings "My name
is","first_name",”last_name" (plus a couple of other small strings) into one larger string “My name
is first_name last_name” and prints the result. (Hint: Experiment with adding two strings in Python
using the + operator.)
'''

a="My name is"
b=" Tushar"
c=" Dhoundhiyal"
print("Single python statement is: ",a+b+c)

'''Create a list and give values of different data types like string,integer and float.'''

a=[1,'typ',4.8,"string",]
print("list printed is: ",a)

'''If a = [1,2,12,1,64,87,9.6,3,6,54], create a sub lists of list a-
sublist1=[12,1,64]
sublist2=[1,1,9.6,54]
sublist3=[54,6,3]'''

q = [1,2,12,1,64,87,9.6,3,6,54]
print("sublist1: ",q[2:5:1])
print("sublist2: ",q[0:10:3])
print("sublist3: ",q[-1:-4:-1])









