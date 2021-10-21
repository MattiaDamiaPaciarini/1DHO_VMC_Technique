import math
import random
from matplotlib import pyplot as plt


NM = 10000 #Number of Moves

i = 0
beta = 0.8 # Parameter near the minimum of alpha
list_x = [] # Positions
list_Y = [] 
list_X = []
list_Err = []

# Collecting the positions

while (i<NM): 
    x = random.gauss(0,1)/math.sqrt(2)/beta
    list_x.append(x)
    i = i+1

# Energy Computation

for j in range(800, 1700, 15):
  E = 0
  D = 0 
  for l in range(0,NM):
    LE = ((j/1000)**2-(j/1000)**4*list_x[l]**2-5*math.exp(-list_x[l]**2))*math.exp((-(j/1000)**2+beta**2)*list_x[l]**2)
    LD = math.exp((-(j/1000)**2+beta**2)*list_x[l]**2)
    E = E+LE
    D = D+LD
    SE = E**2+(LE)**2 
    
  list_Y.append(E/D)
  list_X.append(j/1000)
  list_Err.append(math.sqrt((SE/NM)-(E/NM)**2)/NM)

# Plotting the results

plt.errorbar(list_X, list_Y, yerr = list_Err, fmt='o', color= 'black')
plt.xlabel('alpha')
plt.ylabel('Mean Energy')
plt.title('Energy wrt alpha (correlated samplings) ')
plt.show()
