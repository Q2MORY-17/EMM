# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Wed Mar  4 19:34:03 2020
@author: kent1
This is a temporary script file.
"""
import numpy as np
from matplotlib import pyplot as plt
from math import log, exp

def sum_list(l):
    '''Here you can write docstrings, what the function takes as
    arguments and what the function does. very helpful when 
    using the help function on your programs
    
    for example:
    takes in one int/float argument 
    return the sum of each iteration
    '''
    sum = 0
    for x in l:
        sum += x
    return sum

def sumsquare(x):
    '''Here you can write docstrings, what the function takes as
    arguments and what the function does. very helpful when 
    using the help function on your programs
    '''
    total = 0
    for ele in range(0, len(x)): 
        total = total + x[ele]*x[ele]
        # total += x[ele]**2
    return total

def sumln(x):
    '''Here you can write docstrings, what the function takes as
    arguments and what the function does. very helpful when 
    using the help function on your programs
    '''
    total = 0
    for ele in range(0, len(x)): 
        total = total + log(x[ele])
    return total

def sumlnxi(x,y):
    '''Here you can write docstrings, what the function takes as
    arguments and what the function does. very helpful when 
    using the help function on your programs
    '''
    total = 0
    for ele in range(0, len(x)): 
        total = total + (log(x[ele]))*(y[ele])
    return total

def subroom(x):
    '''Here you can write docstrings, what the function takes as
    arguments and what the function does. very helpful when 
    using the help function on your programs
    '''
    total = 0
    for ele in range(0, len(x)): 
        total = total + (log(x[ele]))*(y[ele])
    return total

with open("lab4.txt", "r") as fo:
    time = fo.read().split()[0::2] # What does this line of code mean?? is it read column 0 to the end every 2 entries?
    for i in range(0, len(time)): 
        time[i] = float(time[i]) 

with open("lab4.txt", "r") as fo:
    temperature = fo.read().split()[1::2] # What does this line of code mean?? is it read column 1 to the end every 2 entries?
    
    temp = np.ndarray((len(temperature),),float)
    for i in range(0, len(temperature)):
        temp[i] = temperature[i].replace(',', '.')
        temp[i] = float(temp[i])

for x in range(0, len(temperature)):
    temp[x] -= 30.68674

r = len(time)
xi = sum_list(time)
xisq = sumsquare(time)
lnyi = sumln(temp)
xilnyi = sumlnxi(temp,time)
A = np.array([[r, xi],[xi, xisq]])
Ainv = np.linalg.inv(A)
B = np.array([lnyi , xilnyi])
C = np.matmul(Ainv,B)
d = C[0]
D = exp(d)
print("The Startvalue is :",D)
print("The timeconstant for pt100 is :",C[1])
print("The exponential funiton is :f(x)=",D,"e^",C[1],"t + 30.68674")

y = [D * exp(C[1]*z) for z in time]

plt.plot(time, temp, linewidth = 1, alpha = 0.5,linestyle = '--', color = "black", label='raw data')
plt.plot(time, y, linewidth = 2, alpha = 1, color = "#c92791", label="fitted curve")
plt.legend()
plt.ylabel("Temperature $(^{o}C)$")
plt.xlabel("Time (s)")
plt.title("THIS MORE LIKE?")
plt.grid(True)
plt.show()
