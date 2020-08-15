gcc -fopenmp -o parallel_MandeBrot.x parallel_MandeBrot.c -lm -std=gnu11
gcc -o serial_MandeBrot.x parallel_MandeBrot.c -lm -std=gnu11 -lrt


for procs in 1 2 4 8 12 16 20; do
         if [ ${procs} -eq 1 ];
         then
                 /usr/bin/time ./serial_MandeBrot.x 1024 1024 -2 -2 2 2 40000
         else
                 export OMP_NUM_THREADS=${procs}
                 /usr/bin/time ./parallel_MandeBrot.x 1024 1024 -2 -2 2 2 40000
        fi
 done

