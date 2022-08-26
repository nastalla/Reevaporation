import math
import csv
import pandas as pd
import matplotlib.pyplot as plt

N = 30 # полное число испарившихся частиц

L = 900 # ML - длина НП
dL_count = 20 # число разбиений всей длины НП
dL = L/dL_count # длина одного фрагмента длины НП

a = 70 # а.м. - расстояние между НП
dx_count = 70 # число разбиений расстояния между НП - количество источников на подложке
dx = a/dx_count # длина одного фрагмента расстояния между НП

n = N/dx_count # скорость испарения из точечного источника

N_dL1 = 0

for i in range (1, dx_count+1):
    N_dL1 = N_dL1 + n/math.pi * math.atan(dL/(i*dx))

X = [dL] # Абсцисса для построения графика осажденная доза(высота)
N_dL = [N_dL1] # набор осажденных доз на каждый фрагмент dL

N_dL_element = 0
summ = N_dL1
for j in range (1, dL_count):
    for i in range (1, dx_count+1):
        #N_dL_element = N_dL_element + 2*n/math.pi * math.asin(dL/(2*math.sqrt(j*j*dL*dL + i*i*dx*dx)))
        N_dL_element = N_dL_element + n/math.pi*(math.pi - math.acos((dL*dL - 2*i*i*dx*dx - j*j*dL*dL - pow((j+1)*dL, 2))/(2*math.sqrt(j*j*dL*dL+i*i*dx*dx)*math.sqrt(pow((j+1)*dL, 2)+i*i*dx*dx))))        
    summ = summ + N_dL_element

    X.append((j+1)*dL)
    N_dL.append(N_dL_element)
    N_dL_element = 0
    
print(summ)
print(N_dL)

plt.plot(X, N_dL, ':o')
plt.grid()
plt.xlabel('Высота, МС')
plt.ylabel('Осажденная доза, ат.')

plt.show()




