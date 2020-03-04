import numpy as np
import math

def sum_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum
def sumsquare(x):
    total = 0
    for ele in range(0, len(x)): 
        total = total + x[ele]*x[ele]
    return total

def sumln(x):
    total = 0
    for ele in range(0, len(x)): 
        total = total + math.log(x[ele])
    return total

def sumlnxi(x,y):
    total = 0
    for ele in range(0, len(x)): 
        total = total + (math.log(x[ele]))*(y[ele])
    return total

def subroom(x):
    total = 0
    for ele in range(0, len(x)): 
        total = total + (math.log(x[ele]))*(y[ele])
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
D = math.exp(d)
print("The Startvalue is :",D)
print("The timeconstant for pt100 is :",C[1])
print("The exponential funiton is :f(x)=",D,"e^",C[1],"t + 30.68674")
