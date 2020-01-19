#!/bin/bash
gcc -fopenmp -o parallel_MandeBrot.x parallel_MandeBrot.c -lm
gcc -o serial_MandeBrot.x parallel_MandeBrot.c -lm


for procs in 1 2 4 8 12 16 20; do
         if [ ${procs} -eq 1 ];
         then
                 /usr/bin/time ./serial_MandeBrot.x 1000 1000 -2 -2 2 2 25000
         else
                 export OMP_NUM_THREADS=${procs}
                 /usr/bin/time ./parallel_MandeBrot.x 1000 1000 -2 -2 2 2 25000
        fi
 done
