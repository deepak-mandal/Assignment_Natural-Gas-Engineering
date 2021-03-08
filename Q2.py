#Python3 code
"""
Roll no.: 170122014

2. Solve using trapezoidal rule (upto 4 decimal places)

f(x)=sqrt(x*x+1)
n=5
lower limit of integration = 0
upper limit of integration=1

Answer: 1.1501
"""
import math
#Trapezoidal Rule
n = 5   #given, n=5
a = 0   #lower limit = 0
b = 1   #upper limit =1
h = (b-a)/n

def f(x):
    return math.sqrt((pow(x, 2) + 1))

sum = 0
for i in range(1, n):
    sum = sum + f(a+i*h)
    #print('sum = ',sum)

term = ((h/2)*(f(a) + f(b) + (2*sum))) 
print('Using Trapeziodal Rule the integral value, I =  {:.4f}'.format(term))
#print("f(a)= ", f(a), "f(b)= ", f(b), "h= ", h)
