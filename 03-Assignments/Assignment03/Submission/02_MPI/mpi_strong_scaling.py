import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,16,20]


plt.figure(figsize = (12,8))
plt.title("Scalability Curve")
plt.xlabel("Number of Cores")
plt.ylabel("Scalability")

    
f = open("output_mpi.txt", "r")

elapsed_list = []
for i in f.readlines():
    if "elapsed" in i:
        if i[i.index("elapsed")-7:i.index("elapsed")-6] == "0": # ensuring elapsed time is not in minutes
            #print(i)
            elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]))
            #print(i[i.index("elapsed")-5:i.index("elapsed")])
        else:
            #print(i)
            min_to_sec = float(i[i.index("elapsed")-7:i.index("elapsed")-6]) * 60
            #print(float(i[i.index("elapsed")-7:i.index("elapsed")-6]) * 60)
            elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
            #print(float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
            
print(elapsed_list[0]/np.array(elapsed_list))
plt.plot(number_of_processors,elapsed_list[0]/np.array(elapsed_list))
        
plt.show()      
