import os
import numpy as np

number_of_processors = [1,2,4,8,16,20]

output_files = [i for i in os.listdir() if i.endswith("elapsedtime.txt")]

for j in output_files:
    N = j[8:13] 
    print("\nFor N =",N,"you can find elapsed times for different processors below" )
    
    f = open(j, "r")
    
    proc = 0
    elapsed_list = []
    for i in f.readlines():
        if "elapsed" in i:
            if i[i.index("elapsed")-7:i.index("elapsed")-6] == "0": # ensuring elapsed time is not in minutes
                elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]))
                #print(i[i.index("elapsed")-5:i.index("elapsed")])
                print(number_of_processors[proc], "cores run has elpased time: "
                      ,float(i[i.index("elapsed")-5:i.index("elapsed")]))
                proc+=1
                
            else:
                min_to_sec = float(i[i.index("elapsed")-7:i.index("elapsed")-6]) * 60
                elapsed_list.append(float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
                print(number_of_processors[proc], "cores run has elapsed time: "
                      ,float(i[i.index("elapsed")-5:i.index("elapsed")]) + min_to_sec)
                proc+=1
    overhead = []
    for i in range(len(elapsed_list)):
        overhead.append(elapsed_list[i]-elapsed_list[0]/number_of_processors[i])
        #print(elapsed_list[i]-elapsed_list[0]/number_of_processors[i])
    print("\nOverhead for N",N,overhead)
