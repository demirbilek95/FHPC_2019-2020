import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,16,20]

f = open("section4_output_strong_scalability_naive.txt", "r")

liste = []
for i in f.readlines():
    if i.startswith(" # walltime"):
        #print(i)
        liste.append(float(i[i.index(":")+2:-2]))
        
max_runTimes = []
for i in range(len(number_of_processors)):
    if liste[2**i-1:2**(i+1)-1] != []:
        print(number_of_processors[i], "cores has maximum run time: " ,max(liste[2**i-1:2**(i+1)-1]))
        max_runTimes.append(max(liste[2**i-1:2**(i+1)-1]))
        
plt.figure(figsize = (12,8))
plt.title("Run Time vs # of Nodes")
plt.xlabel("Number of Nodes")
plt.ylabel("Run Time")
plt.plot(number_of_processors,max_runTimes)
        

plt.figure(figsize = (12,8))
plt.title("Scalability Curve")
plt.xlabel("Number of Nodes")
plt.ylabel("Scalability")
plt.plot(number_of_processors,max_runTimes[0]/np.array(max_runTimes))

plt.show()


