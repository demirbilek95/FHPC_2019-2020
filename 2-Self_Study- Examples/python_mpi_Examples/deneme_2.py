import sys
import numpy as np
from timeit import default_timer as timer
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
    print("I am master processor",rank)

else:
    print("My rank is",rank)
