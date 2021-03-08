#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roll no.: 170122014


3. A gas-well reservoir (7000 psia and 190°F) produces, the gas mixture with following
compositions. Calculate the values of
Component
Mole Fraction
C 1 C 2 C 3 C 4 C 5 N 2 CO 2
0.82 0.08 0.028 0.009 0.02 0.03 0.013
3.1. Apparent molecular weight, Answer: 20
3.2. Specific gravity, Answer: 0.70
3.3. Pseudo-critical pressure, Answer: 660 psia
3.4. Pseudo-critical temperature, Answer: 395 °R
3.5. Viscosity of the gas at reservoir condition using Carr-Kobayashi- Burrows (CKB)
correlation,
Answer: 0.033 cp
3.6. Gas deviation factor (z-factor) at reservoir condition using Brill-Beggs (BB)
correlation,
Answer: 1.14
3.7. Gas deviation factor (z-factor) at reservoir condition using Hall-Yarborough (HY)
correlation, Answer: 1.17
3.8. Gas density at reservoir condition, Answer: 17 lb/ft 3
3.9.Pseudo-pressure m(p) at reservoir condition, psi 2 /cp at 7,000 psia and 190 o F
(Hint: Calculate gas viscosity using the correlation of Carr, Kobayashi, and Burrows, gas deviation
factor using the correlation of Brill and Beggs and perform numerical integration with trapezoidal
method) .
Answer: 20 x 10 8
"""
import pandas as pd
import numpy as np
import math


data={'Component': ['C1', 'C2', 'C3', 'C4', 'C5', 'N2', 'CO2'],
      'Mole fraction': [.82, .08, .028, .009, .02, .03, .013],
      'MWi': [16.04, 30.07, 44.10, 58.12, 72.15, 28.02, 44.01],
      'Pci (psia)': [673, 709, 618, 551, 485, 227, 1073],
      'Tci (degree R)': [344, 550, 666, 766, 847, 492, 548]
      }
frame=pd.DataFrame(data)
print(frame)

"""
Apparent Molecular Weight(MWa)

Mwa= E of {Yi*MWi},    where yi= molefraction of component i 

"""
MWa=frame['Mole fraction']*frame['MWi']
print(MWa)
print('3.1. Apparent molecular weight, MWa = {:.2f}'.format(MWa.sum()))




"""
Specific gravity, Yg = (apperent molecular Wt. of Natural gas) / (M.Wt. of air)

M.Wt. of air = 28.97
"""
Yg=MWa.sum()/28.97
print('3.2. Specific gravity, Yg = {:.2f}'.format(Yg))



"""
Pseudo-critical pressure, Ppc = E of {Yi*Pci}
Pci= critical pressure of composite
"""
Ppc=frame['Mole fraction']*frame['Pci (psia)']
print('3.3. Pseudo-critical pressure, Ppc = {:.2f} psia'.format(Ppc.sum()))


"""
Pseudo-critical temprature, Tpc = E of {Yi*Pci}
Pci= critical pressure of composite
"""
Tpc=frame['Mole fraction']*frame['Tci (degree R)']
print('3.3. Pseudo-critical temperature, Tpc = {:.2f} degree R'.format(Tpc.sum()))


"""
3.5. Viscosity of the gas at reservoir condition using Carr-Kobayashi- Burrows (CKB)
correlation,
Answer: 0.033 cp or centipoises


"""
T=190#degree F
T=649.67    #190°F + 459.67 = 649.67°R
uHC = 8.188*10**-3 - (6.15*10**-3)*math.log(Yg) + (1.709*10**-5 - 2.062*10**-6)*T
uN2= (9.59*10**-3 + (8.48*10**-3)*math.log(Yg))*0.03  #for YN2=0.03
uCO2 = (6.24*10**-3 + (9.08*10**-3)*math.log(Yg))*0.013 #YCO2 = .013

u = uHC + uN2 + uCO2
print('3.5. Viscosity of the gas at reservoir condition using Carr-Kobayashi- Burrows (CKB) correlation = {:.3f} cp'.format(u))



"""
3.6. Gas deviation factor (z-factor) at reservoir condition using Brill-Beggs (BB)
correlation,
Answer: 1.14



A = 1.39*(Tpr - 0.92)**2 - 0.36*Tpr-0.10
B=0.62 - 0.23*Tpr + Tpr -0.86
C= 0.132 - 0.321*math.log(Tpr)
F=  0.3106 - 0.49*Tpr + 0.824*Tpr
D=10*F
E=9*(Tpr - 1)

Z= A+B+C**Ppr
"""

#3.8. Gas density at reservoir condition, Answer: 17 lb/ft 3
P=7000  #psia
Z=1.17 #z-factor using Hall-Yarborough (HY)
ro=(2.7*Yg*P)/(Z*T)
print('3.8. Gas density at reservoir condition = {} lb/ft^3'.format(ro))







