from mpi4py import MPI
import numpy as np

amode = MPI.MODE_RDONLY
comm = MPI.COMM_WORLD
fh = MPI.File.Open(comm, "deneme", amode)

if fh == None:
	print("I can not open file")


buffer = np.ones(10, dtype=np.int)
#print(buffer)

offset = comm.Get_rank()*buffer.nbytes

fh.Read_at_all(offset, buffer)
 	

print(buffer)

fh.Close()