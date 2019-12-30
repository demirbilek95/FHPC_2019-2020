import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (12,8))
plt.title("Overhead (wall-clock time) vs # of Threads (N = 10^9)")
plt.xlabel("Number of Threads")
plt.ylabel("Overhead")

plt.text(16,3.5,'01_array_sum',fontsize = 10)
plt.text(17.5,0.70,'06_touch_by_all',fontsize = 10)

output_files = [i for i in os.listdir() if i[0]=='0']

number_of_processors = [1,2,4,8,12,16,20]

for j in output_files:
    
    f = open(j, "r")

    liste = []
    for i in f.readlines():
        if i.startswith("Sum"):
            #print(i[i.index("took")+5:i.index("of")])
            liste.append(float(i[i.index("took")+5:i.index("of")]))

    Ts = liste[0]
    Tp = np.array(liste)
    p = number_of_processors
    To = p * Tp - Ts
    print("Overhead of",f.name,":",To)    

    plt.plot(p,To)
    
plt.show()
