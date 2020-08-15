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
plt.title("Run Time vs # of Nodes")
plt.xlabel("Number of Nodes")
plt.ylabel("Run Time")
plt.plot(number_of_processors,max_runTimes)

plt.show()
