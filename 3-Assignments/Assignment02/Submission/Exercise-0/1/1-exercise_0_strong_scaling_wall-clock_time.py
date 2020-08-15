import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,12,16,20]

plt.figure(figsize = (12,8))
plt.title("Speed up (wall-clock time) vs # of Threads (N = 10^9)")
plt.xlabel("Number of Threads")
plt.ylabel("Speed up")

plt.text(17.5,8.5,'01_array_sum',fontsize = 10)
plt.text(13.5,14,'06_touch_by_all',fontsize = 10)
output_files = [i for i in os.listdir() if i[0]=='0']

for j in output_files:
    
    f = open(j, "r")
    liste = []
    for i in f.readlines():
        if i.startswith("Sum"):
            #print(i[i.index("took")+5:i.index("of")])
            liste.append(float(i[i.index("took")+5:i.index("of")]))
    plt.plot(number_of_processors,liste[0] / np.array(liste))
    print(f.name,"speed up:",liste[0] / np.array(liste))
plt.show()
