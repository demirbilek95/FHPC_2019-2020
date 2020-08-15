import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,16,20]

f_weak = open("output_weakscaling.txt", "r")

proc = 0
elapsed_list = []
for i in f_weak.readlines():
    if "elapsed" in i:
        if i[i.index("elapsed")-7:i.index("elapsed")-6] == "0": # ensuring elapsed time is not in minutes
            elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]))
            #print(i[i.index("elapsed")-5:i.index("elapsed")])
            print(number_of_processors[proc], "cores run has elapsed time: "
                  ,float(i[i.index("elapsed")-5:i.index("elapsed")]))
            proc+=1
            
        else:
            min_to_sec = float(i[i.index("elapsed")-7:i.index("elapsed")-6]) * 60
            elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
            print(number_of_processors[proc], "cores run has elapsed time: "
                  ,float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
            proc+=1


plt.figure(figsize = (12,8))
plt.title("Run Time vs # of Nodes")
plt.xlabel("Number of Nodes")
plt.ylabel("Run Time")
plt.plot(number_of_processors,elapsed_list)

plt.show()
