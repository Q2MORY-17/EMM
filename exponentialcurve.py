import numpy as np
import math

def sum_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum


with open("lab4.txt", "r") as fo:
    time = fo.read().split()[0::2]
    for i in range(0, len(time)): 
        time[i] = int(time[i]) 
    #print(time)
    print(len(time))
with open("lab4.txt", "r") as fo:
    temperature = fo.read().split()[1::2]
    temp = temperature.replace(',','.')
    print(temperature)
    #temperature = np.array(temperature).astype(np.float)
    #for i in range(0, len(temperature)): 
     #   time[i] = float(temperature[i]) 
    print(len(temperature))
    #print(temperature)
    #print(temperature[0])

#print(sum_list(time))
r = sum_list(time)
#print(temperature[2])
A = np.array([[r, 0],[0, 0]])
print(A[0,0])
#B = np.array([0 , 0])
#print(B[0,:])
#Ainv = np.linalg.inv(A)
#print("this is inverse of A", Ainv)
#C = np.matmul(Ainv,B)
#print("This is Ainv*B",C)
#d = C[0]
#D = math.exp(d)
#print("This is e to the mult",D)