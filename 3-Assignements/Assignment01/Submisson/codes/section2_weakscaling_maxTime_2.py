import os
import matplotlib.pyplot as plt
import numpy as np

number_of_processors = [1,2,4,8,16,20]

f_weak = open("output_weakscaling.txt", "r")

liste = []
for i in f_weak.readlines():
    if i.startswith(" # walltime"):
        #print(i)
        liste.append(float(i[i.index(":")+2:-2]))
        
max_runTimes = []
for i in range(len(number_of_processors)):
    if liste[2**i-1:2**(i+1)-1] != []:
        print(number_of_processors[i], "cores run has maximum run time: " ,max(liste[2**i-1:2**(i+1)-1]))
        max_runTimes.append(max(liste[2**i-1:2**(i+1)-1]))
        
plt.figure(figsize = (12,8))
plt.title("Efficiency of Weak Scalability")
plt.xlabel("Number of Nodes")
plt.ylabel("Efficiency")
plt.plot(number_of_processors,max_runTimes[0]/np.array(max_runTimes)*100)

plt.show()
