import os
import numpy as np
import matplotlib.pyplot as plt

number_of_processors = [1,2,4,8,12,16,20]

plt.figure(figsize = (12,8))
plt.title("Scalability Curve")
plt.xlabel("Number of Nodes")
plt.ylabel("Scalability")

plt.text(17.5,13,'touch by all',fontsize = 10)
plt.text(17.5,15,'optional',fontsize = 10)

file_list = ["optional.txt","06_touch_by_all_output.txt"]
 
for file in file_list:  
    
    f = open(file, "r")
    proc = 0
    elapsed_list = []
    for i in f.readlines():
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
    plt.plot(number_of_processors,elapsed_list[0]/np.array(elapsed_list))
    print("Speed up:",elapsed_list[0]/np.array(elapsed_list))
    
    #plt.savefig('exercise_0_optional.png')
plt.show()
   
