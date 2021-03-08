#Python3 code:
"""
Roll no.: 170122014

1. Solve using Newton Raphson method (upto 5 decimal places)

f(x)= x*x + 2x - 1, for -1<x<=1

Answer: 0.41421
"""
 
def func(x): 
	return x*x + 2*x - 1

# Derivative of this function  
def derivFunc(x): 
	return 2*x + 2 

# Function to find the root 
def newtonRaphson(x):
	h = func(x) / derivFunc(x) 
	while abs(h) >= 0.0001: 
		h = func(x)/derivFunc(x)
		# x(i+1) = x(i) - f(x) / f'(x) 
		x=x-h 
	
	print("The value of the root for the given function is : ", "%.5f"% x) 




########################################### 
x0 = 0 # Initial Guess (can be derive from rough graph)
newtonRaphson(x0)
