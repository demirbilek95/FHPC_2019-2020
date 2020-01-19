import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,12,16,20]

plt.figure(figsize = (12,8))
plt.title("Speed up (wall-clock time) vs # of Threads")
plt.xlabel("Number of Threads")
plt.ylabel("Speed up")

plt.text(16.5,15.5,'Balanced',fontsize = 10)
plt.text(17.5,5,'Straightforward',fontsize = 10)

file_list = ["output_balanced.txt", "output_straight.txt"]

for i in file_list:
    
    f = open(i, "r")
    liste = []
    for i in f.readlines():
        if i.startswith("Process"):
            #print(i[i.index("took")+5:i.index("of")])
            liste.append(float(i[i.index("took")+5:i.index("of")]))

    plt.plot(number_of_processors,liste[0] / np.array(liste)) 

    print(f.name,"speed up:",liste[0] / np.array(liste))

plt.show()

    
