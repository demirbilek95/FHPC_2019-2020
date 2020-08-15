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

       33845418144 cpu-cycles                #    3.226 GHz                      ( +-  0.12% ) [80.02%]
       27367678869 instructions              #    0.81  insns per cycle        
                                             #    0.93  stalled cycles per insn  ( +-  0.05% ) [89.99%]
         180765348 cache-references          #   17.229 M/sec                    ( +-  0.06% ) [89.93%]
         150130073 cache-misses              #   83.052 % of all cache refs      ( +-  0.02% ) [89.94%]
        2086147013 branch-instructions       #  198.836 M/sec                    ( +-  0.10% ) [89.96%]
            119766 branch-misses             #    0.01% of all branches          ( +-  0.83% ) [90.00%]
       25395178982 stalled-cycles-frontend   #   75.03% frontend cycles idle     ( +-  0.16% ) [90.02%]
   <not supported> stalled-cycles-backend  
      10491.858119 cpu-clock                                                     ( +-  0.12% )
      10491.814773 task-clock                #    2.762 CPUs utilized            ( +-  0.12% )
   <not supported> L1-dcache-loads         
         380863046 L1-dcache-load-misses     #    0.00% of all L1-dcache hits    ( +-  0.03% ) [90.04%]
          84430448 LLC-loads                 #    8.047 M/sec                    ( +-  0.12% ) [90.05%]
          58937920 LLC-load-misses           #   69.81% of all LL-cache hits     ( +-  0.11% ) [90.05%]

       3.798835260 seconds time elapsed                                          ( +-  0.12% )



 Performance counter stats for './06_touch_by_all_parallel.x 1000000000' (10 runs):

       28103325429 cpu-cycles                #    3.066 GHz                      ( +-  0.67% ) [80.00%]
       27395801411 instructions              #    0.97  insns per cycle        
                                             #    0.72  stalled cycles per insn  ( +-  0.10% ) [89.98%]
         142379842 cache-references          #   15.533 M/sec                    ( +-  0.17% ) [89.94%]
         132912631 cache-misses              #   93.351 % of all cache refs      ( +-  0.12% ) [89.95%]
        2099494448 branch-instructions       #  229.042 M/sec                    ( +-  0.23% ) [89.97%]
            136217 branch-misses             #    0.01% of all branches          ( +-  0.84% ) [89.99%]
       19606804162 stalled-cycles-frontend   #   69.77% frontend cycles idle     ( +-  1.01% ) [90.01%]
   <not supported> stalled-cycles-backend  
       9166.426081 cpu-clock                                                     ( +-  0.72% )
       9166.408297 task-clock                #   17.454 CPUs utilized            ( +-  0.72% )
   <not supported> L1-dcache-loads         
         380786971 L1-dcache-load-misses     #    0.00% of all L1-dcache hits    ( +-  0.04% ) [90.03%]
          13799532 LLC-loads                 #    1.505 M/sec                    ( +-  2.06% ) [90.05%]
           9623979 LLC-load-misses           #   69.74% of all LL-cache hits     ( +-  2.03% ) [90.07%]

       0.525183551 seconds time elapsed                                          ( +-  2.25% )



**On My Computer** (with 8 threads )

perf c2c record | perf c2c report

**Touch by first**
=================================================
            Trace Event Information              
=================================================
  Total records                     :      64256
  Locked Load/Store Operations      :        666
  Load Operations                   :      31716
  Loads - uncacheable               :          0
  Loads - IO                        :          0
  Loads - Miss                      :          0
  Loads - no mapping                :          1
  Load Fill Buffer Hit              :        772
  Load L1D hit                      :      30870
  Load L2D hit                      :         18
  Load LLC hit                      :         32
  Load Local HITM                   :          0
  Load Remote HITM                  :          0
  Load Remote HIT                   :          0
  Load Local DRAM                   :         23
  Load Remote DRAM                  :          0
  Load MESI State Exclusive         :         23
  Load MESI State Shared            :          0
  Load LLC Misses                   :         23
  LLC Misses to Local DRAM          :      100.0%
  LLC Misses to Remote DRAM         :        0.0%
  LLC Misses to Remote cache (HIT)  :        0.0%
  LLC Misses to Remote cache (HITM) :        0.0%
  Store Operations                  :      32540
  Store - uncacheable               :          0
  Store - no mapping                :       1320
  Store L1D Hit                     :      30635
  Store L1D Miss                    :        585
  No Page Map Rejects               :       7899
  Unable to parse data source       :          0

=================================================
    Global Shared Cache Line Event Information   
=================================================
  Total Shared Cache Lines          :          0
  Load HITs on shared lines         :          0
  Fill Buffer Hits on shared lines  :          0
  L1D hits on shared lines          :          0
  L2D hits on shared lines          :          0
  LLC hits on shared lines          :          0
  Locked Access on shared lines     :          0
  Store HITs on shared lines        :          0
  Store L1D hits on shared lines    :          0
  Total Merged records              :          0

**Touch by all**

=================================================
            Trace Event Information              
=================================================
  Total records                     :      79561
  Locked Load/Store Operations      :       1113
  Load Operations                   :      37588
  Loads - uncacheable               :          0
  Loads - IO                        :          0
  Loads - Miss                      :          0
  Loads - no mapping                :          0
  Load Fill Buffer Hit              :       1743
  Load L1D hit                      :      35243
  Load L2D hit                      :        318
  Load LLC hit                      :        260
  Load Local HITM                   :         79
  Load Remote HITM                  :          0
  Load Remote HIT                   :          0
  Load Local DRAM                   :         24
  Load Remote DRAM                  :          0
  Load MESI State Exclusive         :         24
  Load MESI State Shared            :          0
  Load LLC Misses                   :         24
  LLC Misses to Local DRAM          :      100.0%
  LLC Misses to Remote DRAM         :        0.0%
  LLC Misses to Remote cache (HIT)  :        0.0%
  LLC Misses to Remote cache (HITM) :        0.0%
  Store Operations                  :      41973
  Store - uncacheable               :          0
  Store - no mapping                :       1957
  Store L1D Hit                     :      38638
  Store L1D Miss                    :       1378
  No Page Map Rejects               :      13908
  Unable to parse data source       :          0

=================================================
    Global Shared Cache Line Event Information   
=================================================
  Total Shared Cache Lines          :         35
  Load HITs on shared lines         :       1246
  Fill Buffer Hits on shared lines  :        365
  L1D hits on shared lines          :        611
  L2D hits on shared lines          :        121
  LLC hits on shared lines          :        149
  Locked Access on shared lines     :        458
  Store HITs on shared lines        :        373
  Store L1D hits on shared lines    :        343
  Total Merged records              :        452




	


 






