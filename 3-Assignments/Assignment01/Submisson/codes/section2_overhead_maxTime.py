import os
import numpy as np

output_files = [i for i in os.listdir() if i.endswith("walltime.txt")]

number_of_processors = [1,2,4,8,16,20]

for j in output_files:
    
    N = j[8:13] 
    print("\n*** For N =",N,"you can find run times and overheads for different processors below ***" )
    
    f = open(j, "r")
    
    liste = []
    for i in f.readlines():
        if i.startswith(" # walltime"):
        #print(i)
            liste.append(float(i[i.index(":")+2:-2]))
            
    max_runTimes = []
    for i in range(len(number_of_processors)):
        if liste[2**i-1:2**(i+1)-1] != []:
            print(number_of_processors[i], "cores run has maximum run time: " ,max(liste[2**i-1:2**(i+1)-1])
                 ,"overhead is",max(liste[2**i-1:2**(i+1)-1])-(liste[2**i-1:2**(i+1)-1][0]/number_of_processors[i]))
            max_runTimes.append(max(liste[2**i-1:2**(i+1)-1]))

