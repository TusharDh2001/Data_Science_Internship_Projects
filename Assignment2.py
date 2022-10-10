"""
Q1 answer>>

for i in range(0,4):
    for j in range(i,5):
        print("&",end=" ")
    print()
"""
"""
Q2 answer>>

str = "My Name Is Python"
for i in range(0,len(str)):
    if i%2 == 0:
        print(str[i],end="")
"""
"""
Q3 answer>>

list = [15, 10, 56, 9, 40, 3, 6, 75, 8, 30]
for i in list:
    if i%5==0:
        print(i,end=" ")
"""
"""
Q4 answer>>

word=input("Input :")
n=len(word)
w1=word[0:n:]
w2=word[::-1]
if w1==w2:
    print("It is a palindrome")
else:
    print("Not a palindrome")
"""
"""
Q5 answer>>

def remo_wood(num):
    if num%3 == 0 & num%5 == 0:
        return "remo_wood"
    elif num%3==0:
        return "remo"
    elif num%5 == 0:
        return "wood"
    else:
        return num

n=int(input("Enter the number : "))
answer = remo_wood(n)
print(answer)
"""
"""
Q6 answer>>
a=[5,6,2,9,4]
b=[]
for i in a:
    c=i**2
    b.append(c)
print(b)
"""
"""
Q7 answer>>
import random

papers = ['A','B','C']

q_list = [random.choice(papers) for i in range(4)]
print(q_list)