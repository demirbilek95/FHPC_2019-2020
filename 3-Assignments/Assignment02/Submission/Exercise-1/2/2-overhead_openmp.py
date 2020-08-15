import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,12,16,20]

plt.figure(figsize = (12,8))
plt.title("Overhead (Elapsed Time) vs # of Threads (N = 10^9)")
plt.xlabel("Number of Threads")
plt.ylabel("Overhead (Elapsed Time)")


f = open("strong_scaling_output.txt", "r")

proc = 0
elapsed_list = []
for i in f.readlines():
    if "elapsed" in i:
        if i[i.index("elapsed")-7:i.index("elapsed")-6] == "0": # ensuring elapsed time is not in minutes
            elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]))
            #print(i[i.index("elapsed")-5:i.index("elapsed")])
            #print(number_of_processors[proc], "threads run has elapsed time: "
                  #,float(i[i.index("elapsed")-5:i.index("elapsed")]))
            proc+=1
        else:
            min_to_sec = float(i[i.index("elapsed")-7:i.index("elapsed")-6]) * 60
            elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
            #print(number_of_processors[proc], "threads run has elapsed time: "
                  #,float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
            proc+=1

Ts = elapsed_list[0]
Tp = np.array(elapsed_list)
p = number_of_processors
To = p * Tp - Ts
print("Overhead for",f.name,":", To)
plt.plot(p,To)

plt.show()

