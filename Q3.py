#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roll no.: 170122014

Question 3:
    
"""
import pandas as pd
import numpy as np
import math

T=190	#degree F
P=7000	#in psia

data={'Component': ['C1', 'C2', 'C3', 'C4', 'C5', 'N2', 'CO2'],
      'Mole fraction': [.82, .08, .028, .009, .02, .03, .013],
      'MWi': [16.04, 30.07, 44.10, 58.12, 72.15, 28.02, 44.01],
      'Pci (psia)': [673, 709, 618, 551, 485, 227, 1073],
      'Tci (degree R)': [344, 550, 666, 766, 847, 492, 548]
      }
frame=pd.DataFrame(data)
#print(frame)
print()
"""
Apparent Molecular Weight(MWa)
Mwa= E of {Yi*MWi},    where yi= molefraction of component i 
"""
MWa=frame['Mole fraction']*frame['MWi']
#print(MWa)
print('3.1. Apparent molecular weight, MWa = {:.2f}'.format(MWa.sum()))
print()


"""
Specific gravity, Yg = (apperent molecular Wt. of Natural gas) / (M.Wt. of air)
M.Wt. of air = 28.97
"""
Yg=MWa.sum()/28.97
print('3.2. Specific gravity, Yg = {:.2f}'.format(Yg))
print()

"""
Pseudo-critical pressure, Ppc = E of {Yi*Pci}
Pci= critical pressure of composite
"""
Ppc=frame['Mole fraction']*frame['Pci (psia)']
Ppc=Ppc.sum()
print('3.3. Pseudo-critical pressure, Ppc = {:.2f} psia'.format(Ppc))
print()

"""
Pseudo-critical temprature, Tpc = E of {Yi*Pci}
Pci= critical pressure of composite
"""
Tpc=frame['Mole fraction']*frame['Tci (degree R)']
Tpc=Tpc.sum()
print('3.4 Pseudo-critical temperature, Tpc = {:.2f} degree R'.format(Tpc))
print()


"""
3.5. Viscosity of the gas at reservoir condition using Carr-Kobayashi- Burrows (CKB) correlation
"""
uHC = 8.188*10**-3 - (6.15*10**-3)*math.log(Yg) + (1.709*10**-5 - 2.062*10**-6)*(T+460)
uN2= (9.59*10**-3 + (8.48*10**-3)*math.log(Yg))*0.03  #for YN2=0.03
uCO2 = (6.24*10**-3 + (9.08*10**-3)*math.log(Yg))*0.013 #YCO2 = .013

u = uHC + uN2 + uCO2
print('3.5. Viscosity of the gas using Carr-Kobayashi- Burrows (CKB) correlation = {:.3f} cp'.format(u))
print()


"""
3.6. Gas deviation factor (z-factor) at reservoir condition using Brill-Beggs (BB)
correlation,
"""
Tpr=(T+460)/Tpc
Ppr= P/Ppc
A = 1.39*(Tpr-0.92)**2-0.36*Tpr-0.10
B=0.62 - 0.23*Tpr + Tpr-0.86
C= 0.132 - 0.321*math.log(Tpr)
F=  0.3106 - 0.49*Tpr + 0.824*Tpr
D=10*F
E=9*(Tpr - 1)
#print(A, B, C, Ppr)
Z= (A+B+C)**Ppr
print("3.6. Gas deviation factor (z-factor) using Brill-Beggs (BB) correlation = {:.2f}".format(Z))
print()


"""
3.7. Gas deviation factor (z-factor) at reservoir condition using Hall-Yarborough (HY)
correlation, Answer: 1.17
"""
Tpr=(T+460)/Tpc
Ppr= P/Ppc
t=1/Tpr

A=0.06125*t*math.exp(-1.2*(1-t)**2)
B=t*(14.76-9.76*t+4.58*t**2)
C=t*(90.7-242.2*t+42.4*t**2)
D=2.18+2.82*t

def func(y): 
	return ((y+y**2+y**3-y**4)/((1-y)**3))-A*Ppr-B*y**2+C*y**D

# Derivative of this function  
def derivFunc(y): 
	return (((1-y)**3*(1+2*y+3*y**2-4*y**3)+(y+y**2+y**3-y**4)*3*(1-y)**2)/((1-y)**6))-B*2*y+C*D*y**(D-1)

# Function to find the root 
def newtonRaphson(y):
	h = func(y) / derivFunc(y) 
	while abs(h) >= 0.0001: 
		h = func(y)/derivFunc(y)
		# x(i+1) = x(i) - f(x) / f'(x) 
		y=y-h 
	return y
	
y0 = 0 # Initial Guess (can be derive from rough graph)
y1=newtonRaphson(y0)

z= (A*Ppr)/y1

print("3.7. Gas deviation factor (z-factor) using Hall-Yarborough (HY) correlation = {:.2f}".format(z))
print()


#3.8. Gas density at reservoir condition, Answer: 17 lb/ft 3
P=7000  #psia
Z=1.17 #z-factor using Hall-Yarborough (HY)
ro=(2.7*Yg*P)/(Z*(T+460))
print('3.8. Gas density at reservoir condition = {:.2f} lb/ft^3'.format(ro))
print()


"""
Q3.9

"""
import math
#Trapezoidal Rule
n = 100   
a = 14.7   #lower limit in psia
b = 7000   #upper limit =1
h = (b-a)/n

def f(x):
    return 2*x/0.033*1.17

sum = 0
for i in range(1, n):
    sum = sum + f(a+i*h)
    #print('sum = ',sum)

term = ((h/2)*(f(a) + f(b) + (2*sum))) 
print('3.9 Pseudo-pressure m(p) at reservoir condition =  {:.3E} psi^2/cp (approx.)'.format(term))



