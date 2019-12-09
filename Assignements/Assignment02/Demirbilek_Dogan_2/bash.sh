#!/bin/bash 
for procs in 1 2 4 8 12 16 20 ; do
         if [ ${procs} -eq 1 ];
         then
                 /usr/bin/time ./pi.x 1000000000
         else
                 export OMP_NUM_THREADS=${procs}
                 /usr/bin/time ./openmp_pi.x 1000000000
        fi
 done

