**My Computer**

sudo perf stat -r 5 -e duration_time,branch-instructions,branch-misses,cache-misses,cache-references,cpu-cycles,instructions,mem-loads,mem-stores,icache.hit,icache.misses ./06_touch_by_all_parallel.x 1000000000

**Ulyses**

perf stat -r 5 -e cpu-cycles,instructions,cache-references,cache-misses,branch-instructions,branch-misses,stalled-cycles-frontend,stalled-cycles-backend,cpu-clock,task-clock,L1-dcache-loads,L1-dcache-load-misses,LLC-loads,LLC-load-misses ./06_touch_by_all_parallel.x 1000000000






**On My Computer** (with 8 threads )

 Performance counter stats for './01_array_sum_parallel.x 1000000000' (5 runs):

     4.753.397.430 ns   duration_time                                                 ( +-  0,53% )
     2.965.115.545      branch-instructions                                           ( +-  0,30% )  (28,76%)
         3.928.250      branch-misses             #    0,13% of all branches          ( +-  2,25% )  (38,60%)
        14.113.021      cache-misses              #   53,652 % of all cache refs      ( +-  1,57% )  (39,29%)
        26.304.974      cache-references                                              ( +-  0,91% )  (39,02%)
    27.315.634.083      cpu-cycles                                                    ( +-  0,10% )  (38,93%)
    28.628.519.377      instructions              #    1,05  insn per cycle           ( +-  0,18% )  (48,94%)
                 0      mem-loads                                                     (49,07%)
     5.500.029.276      mem-stores                                                    ( +-  0,40% )  (42,44%)
     2.511.321.763      icache.hit                                                    ( +-  1,23% )  (24,23%)
         1.280.373      icache.misses                                                 ( +-  8,13% )  (21,80%)

            4,7534 +- 0,0254 seconds time elapsed  ( +-  0,53% )


 Performance counter stats for './06_touch_by_all_parallel.x 1000000000' (5 runs):

     1.634.316.576 ns   duration_time                                                 ( +-  2,03% )
     2.943.283.463      branch-instructions                                           ( +-  0,31% )  (27,85%)
         5.374.145      branch-misses             #    0,18% of all branches          ( +-  0,68% )  (37,27%)
        19.025.382      cache-misses              #   39,482 % of all cache refs      ( +-  1,29% )  (38,56%)
        48.187.157      cache-references                                              ( +-  0,93% )  (38,46%)
    34.940.586.957      cpu-cycles                                                    ( +-  0,34% )  (38,57%)
    27.544.218.005      instructions              #    0,79  insn per cycle           ( +-  0,13% )  (48,54%)
                 0      mem-loads                                                     (48,57%)
     5.353.567.164      mem-stores                                                    ( +-  0,31% )  (35,00%)
     3.994.818.323      icache.hit                                                    ( +-  1,31% )  (29,79%)
         2.770.789      icache.misses                                                 ( +- 16,03% )  (24,69%)

            1,6343 +- 0,0332 seconds time elapsed  ( +-  2,03% )

 



**Ulysses Computational Node** (with 20 threads)

 Performance counter stats for './01_array_sum_parallel.x 1000000000' (10 runs):

       55367723248 cpu-cycles                #    3.190 GHz                      ( +-  0.69% ) [79.97%]
       29432859612 instructions              #    0.53  insns per cycle        
                                             #    1.52  stalled cycles per insn  ( +-  0.77% ) [90.00%]
         204967723 cache-references          #   11.810 M/sec                    ( +-  0.22% ) [90.00%]
         163047197 cache-misses              #   79.548 % of all cache refs      ( +-  0.12% ) [90.02%]
        3383248775 branch-instructions       #  194.938 M/sec                    ( +-  1.89% ) [90.02%]
            126687 branch-misses             #    0.00% of all branches          ( +-  1.79% ) [90.02%]
       44593600516 stalled-cycles-frontend   #   80.54% frontend cycles idle     ( +-  0.57% ) [90.02%]
   <not supported> stalled-cycles-backend  
      17355.555241 cpu-clock                                                     ( +-  0.70% )
      17355.517667 task-clock                #    3.377 CPUs utilized            ( +-  0.70% )
   <not supported> L1-dcache-loads         
         381578229 L1-dcache-load-misses     #    0.00% of all L1-dcache hits    ( +-  0.03% ) [90.01%]
         102807436 LLC-loads                 #    5.924 M/sec                    ( +-  0.66% ) [90.00%]
          74041266 LLC-load-misses           #   72.02% of all LL-cache hits     ( +-  0.68% ) [89.98%]

       5.139179988 seconds time elapsed                                          ( +-  0.28% )


Performance counter stats for './06_touch_by_all_parallel.x 1000000000' (10 runs):

       51791918166 cpu-cycles                #    3.061 GHz                      ( +-  1.00% ) [79.98%]
       28696737548 instructions              #    0.55  insns per cycle        
                                             #    1.44  stalled cycles per insn  ( +-  0.22% ) [89.98%]
         181191532 cache-references          #   10.709 M/sec                    ( +-  0.37% ) [89.97%]
         151272284 cache-misses              #   83.488 % of all cache refs      ( +-  0.19% ) [89.98%]
        3322533713 branch-instructions       #  196.377 M/sec                    ( +-  0.58% ) [90.00%]
            150170 branch-misses             #    0.00% of all branches          ( +-  0.70% ) [90.00%]
       41256239875 stalled-cycles-frontend   #   79.66% frontend cycles idle     ( +-  1.22% ) [90.01%]
   <not supported> stalled-cycles-backend  
      16919.189143 cpu-clock                                                     ( +-  0.98% )
      16919.144725 task-clock                #   18.748 CPUs utilized            ( +-  0.98% )
   <not supported> L1-dcache-loads         
         381336591 L1-dcache-load-misses     #    0.00% of all L1-dcache hits    ( +-  0.05% ) [90.02%]
          80611424 LLC-loads                 #    4.765 M/sec                    ( +-  1.57% ) [90.04%]
          56445647 LLC-load-misses           #   70.02% of all LL-cache hits     ( +-  1.55% ) [90.03%]

       0.902462656 seconds time elapsed                                          ( +-  1.07% )

	


 






