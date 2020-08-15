import sys
import numpy as np
from timeit import default_timer as timer
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#N = int(sys.argv[1])  # It is taking the input from command line same as mpi_pi.c program

#read_start_time = MPI.Wtime()
f = open("input_file.txt","r")
#read_end_time = MPI.Wtime()

N = int(f.readline()[:-2]) 

elements_per_rank = N//size

if N % size != 0:
    reminder = elements_per_rank * size
else:
    reminder = 0

array = np.arange(rank*elements_per_rank,(rank+1)*elements_per_rank)

partial_sum = np.zeros(1)

start_time = MPI.Wtime()

partial_sum[0] = np.sum(array)

#print("Computation time on rank",rank,"is",comp_time_end-comp_time_end	)

#print("On rank" ,rank,"partial sum is",partial_sum)
	
if rank == 0:
    total = np.zeros(1)
else:
    total = None

comm.Reduce(partial_sum,total,op=MPI.SUM,root=0)
    
if rank == 0: #master nodes gather results from others

    if reminder != 0:
        reminder_sum = np.sum(array[reminder:])
    else:
        reminder_sum = 0

    total[0]= total[0] + reminder_sum + N
    end_time = MPI.Wtime()
    print("\n # walltime on master processor :",end_time-start_time)
    print("\nTotal", int(total))

else:
    end_time = MPI.Wtime()
    print("\n # walltime on processor",rank,":",end_time-start_time)





    

