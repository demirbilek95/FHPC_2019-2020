#!/bin/bash 
for procs in 2 4 8 12 16 20 ; do
                 export OMP_NUM_THREADS=${procs}
                 /usr/bin/time ./openmp_pi.x ${procs} * 1000000000
 done

