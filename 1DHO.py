import math
import random
from matplotlib import pyplot as plt



NM = 10000 #Number of Moves
i = 0
list_Y = []
list_X = []
list_Err = []

for j in range(800, 1700, 15):
  E = 0
  while (i<NM):
    x = random.gauss(0,1)/math.sqrt(2)/(j/1000)
    LE = (j/1000)**2-(j/1000)**4*x**2-5*math.exp(-x**2)
    E = E+LE
    SE = E**2+LE**2 
    i = i+1
  i = 0 
  list_Y.append(E/NM)
  list_X.append(j/1000)
  list_Err.append(math.sqrt((SE/NM)-(E/NM)**2)/NM)


plt.errorbar(list_X, list_Y, yerr = list_Err, fmt='o', color= 'black')
plt.xlabel('alpha')
plt.ylabel('Mean Energy')
plt.title('Energy wrt alpha')
plt.show()

