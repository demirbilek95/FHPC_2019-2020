from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


plane_coordinates = np.zeros(4, dtype='d') 
pixel_maxiter = np.zeros(3, dtype='i')

if rank == 0:
	print("data",plane_coordinates,"data_type",plane_coordinates.dtype,"number_of_bytes",plane_coordinates.nbytes)
	print("data",pixel_maxiter,"data_type",pixel_maxiter.dtype,"number_of_bytes",pixel_maxiter.nbytes)


#print("plane_coordinates", planeprint(buffer_1)
#print("pixel_maxiter", pixel_maxiter)

#array = np.ones((nx,ny), dtype=np.int)


amode = MPI.MODE_RDONLY
fh = MPI.File.Open(comm, "deneme", amode)

item_count = len(plane_coordinates)

buffer_1 = plane_coordinates

filetype_1 = MPI.DOUBLE.Create_vector(item_count, 1, size)
filetype_1.Commit()

displacement_1 = MPI.DOUBLE.Get_size()*rank
fh.Set_view(displacement_1, filetype=filetype_1)

#if rank == 0:
#	print("displacement_1:", displacement_1)
#rint("rank",rank, "displacement_1", displacement_1)

fh.Read_all(buffer_1)


filetype_1.Free()
fh.Close()

if rank==0:	
	print(buffer_1)