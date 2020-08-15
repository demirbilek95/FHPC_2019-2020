import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,16,20]

output_files = [i for i in os.listdir() if i.endswith("walltime.txt")]

plt.figure(figsize = (12,8))
plt.title("Run Time vs # of Nodes")
plt.xlabel("Number of Nodes")
plt.ylabel("Run Time")

plt.text(17.5,6.5,'N = 10^6',fontsize = 10)
plt.text(16,10,'N = 10^7',fontsize = 10)
plt.text(17,14,'N = 10^8',fontsize = 10)
plt.text(15,14.5,'N = 10^9',fontsize = 10)


for j in output_files:
    
    N = j[8:13] 
    print("\nFor N =",N,"you can find run times for different processors below" )
    
    f = open(j, "r")
    
    liste = []
    for i in f.readlines():
        if i.startswith(" # walltime"):
        #print(i)
            liste.append(float(i[i.index(":")+2:-2]))
            
    max_runTimes = []
    for i in range(len(number_of_processors)):
        if liste[2**i-1:2**(i+1)-1] != []:
            max_runTimes.append(max(liste[2**i-1:2**(i+1)-1]))
            print(number_of_processors[i], "cores run has maximum run time: " ,max(liste[2**i-1:2**(i+1)-1])
                 ,"scalability is",max_runTimes[0]/max(liste[2**i-1:2**(i+1)-1]))
    plt.plot(number_of_processors,max_runTimes[0]/np.array(max_runTimes))
    
plt.show()
