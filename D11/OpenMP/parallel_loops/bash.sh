#!/bin/bash 
for procs in 1 2 4 8 12 16 20 ; do
	 if [ ${procs} -eq 1 ];
	 then
		 ./01_array_sum_serial.x
	 else
		 export OMP_NUM_THREADS=${procs}
		 ./01_array_sum.x 1000000000
	fi
 done
