from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

nx, ny, xL, yL, xR, yR, Imax  =500, 500, -2, -2, +2, +2, 1000

plane_coordinates = np.zeros(4, dtype='d') 
pixel_maxiter = np.zeros(3, dtype='i')

if rank == 0:
    plane_coordinates[:] = [xL, xR, yL, yR]
    pixel_maxiter[:] = [nx, ny, Imax]

    print("data",plane_coordinates,"data_type",plane_coordinates.dtype,"number_of_bytes",plane_coordinates.nbytes)
    print("data",pixel_maxiter,"data_type",pixel_maxiter.dtype,"number_of_bytes",pixel_maxiter.nbytes)
    
# Splitting data to other cores
comm.Bcast([plane_coordinates, MPI.DOUBLE], root=0)
comm.Bcast([pixel_maxiter, MPI.INT], root=0)


#print("plane_coordinates", plane_coordinates)
#print("pixel_maxiter", pixel_maxiter)

#array = np.ones((nx,ny), dtype=np.int)


amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
fh = MPI.File.Open(comm, "deneme", amode)

item_count_1 = len(plane_coordinates)

buffer_1= plane_coordinates

filetype_1 = MPI.DOUBLE.Create_vector(item_count_1, 1, size)
filetype_1.Commit()

displacement_1 = MPI.DOUBLE.Get_size()*rank
fh.Set_view(displacement_1, filetype=filetype_1)

#print("rank",rank, "displacement_1", displacement_1)

fh.Write_all(buffer_1)


filetype_1.Free()

fh.Close()