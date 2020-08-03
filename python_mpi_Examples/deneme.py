#import sys
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#N = int(sys.argv[1])  # It is taking the input from command line same as mpi_pi.c program

#read_start_time = MPI.Wtime()
f = open("input_file.txt","r")
#read_end_time = MPI.Wtime()

#print("Read time for rank",rank,"is",read_end_time - read_start_time)

N = int(f.readline()[:-2]) 

elements_per_rank = N//size-1

start_time = MPI.Wtime()

#comp_start_time = MPI.Wtime()

#comp_end_time = MPI.Wtime()
#print("Comp time for rank",rank,"is",comp_end_time-start_time)

 
if rank == 0: #master nodes gather results from others

    if N % size != 0:
        reminder_array = np.arange(N - N % size+1,N+1)
        reminder_sum = np.sum(reminder_array)
    else:
        reminder_sum = 0

    print("\nOn master rank reminder sum is",reminder_sum)

    total = reminder_sum

    for i in range(1,size):
        #recv_start_time = MPI.Wtime()
        partial_sum = comm.recv(source = i, tag = i*11)
        #recv_end_time = MPI.Wtime()
        #print("From rank",rank,"to master node receiving time:",recv_end_time-recv_start_time)
        total += partial_sum

    end_time = MPI.Wtime()

    print("\n # walltime on master processor :",end_time-start_time)
    print("\nTotal of N",N,":",total)

    
else:
    array = np.arange(rank*elements_per_rank+1,(rank+1)*elements_per_rank+1)
    partial_sum = np.sum(array)
    print("\nOn rank" ,rank,"partial sum is",partial_sum)
    #send_start_time = MPI.Wtime()
    comm.send(partial_sum, dest = 0, tag = rank*11)
    #send_end_time = MPI.Wtime()
    #print("From rank",rank,"to master node sending time:",send_end_time-send_start_time)
    #print("rank",rank, "sent partial sum to master node")
    end_time = MPI.Wtime()
    print("\n # walltime on processor ",rank,":", end_time-start_time)

    

