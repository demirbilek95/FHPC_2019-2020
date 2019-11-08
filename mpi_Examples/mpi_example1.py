import numpy as np
from timeit import default_timer as timer
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

start = timer()

if rank == 0:
    
    N = int(input("Please enter the N: "))

    N_array = np.arange(1,N+1)
    
    #Split data equal for all processors for now let's make 2
    
    data1 = N_array[:int(N/2)]
    data2 = N_array[int(N/2):]
    
    comm.send(data1, dest = 1, tag = 11)
    
    print("Data1 send to rank 1")
    
    comm.send(data2, dest = 2, tag = 12)
    
    print("Data2 send to rank 2")

elif rank == 1:
    
    data1 = comm.recv(source = 0, tag = 11)
    
    print("Data1 is received from rank 0")
    
    sum_data1 = np.sum(data1)
    
    comm.send(sum_data1, dest = 3, tag = 13)
    
    print("Sum of data1 send to rank 3")
    

elif rank == 2:
    
    data2 = comm.recv(source = 0, tag = 12)
    
    print("Data2 is received from rank 0")
    
    sum_data2 = np.sum(data2)
    
    comm.send(sum_data2, dest = 3, tag = 14)
    
    print("Sum of data2 send to rank 3")

    
elif rank == 3:
    
    sum_data1 = comm.recv(source = 1, tag = 13)
    
    print("sum_data1 is received from rank 1")
    
    sum_data2 = comm.recv(source = 2, tag = 14)
    
    print("sum_data2 is received from rank 2")
    
    
    print("Sum of the numbers are: " ,sum_data1+sum_data2)
   
end = timer()

print("Parallel execeution time is: ",end-start, "second")

    
    
    
