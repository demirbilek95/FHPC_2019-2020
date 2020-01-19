from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

nx, ny, xL, yL, xR, yR, Imax  =100, 100, -2,-2, 2, 2, 1000

plane_coordinates = np.zeros(4, dtype='d') 
pixel_maxiter = np.zeros(3, dtype='i')
array = np.ones(nx*ny, dtype='i')

if rank == 0:
    plane_coordinates[:] = [xL, xR, yL, yR]
    pixel_maxiter[:] = [nx, ny, Imax]

    print("data",plane_coordinates,"data_type",plane_coordinates.dtype,"number_of_bytes",plane_coordinates.nbytes)
    print("data",pixel_maxiter,"data_type",pixel_maxiter.dtype,"number_of_bytes",pixel_maxiter.nbytes)
    print("data",array,"data_type",array.dtype,"number_of_bytes",array.nbytes)
    
# Splitting data to other cores
comm.Bcast([plane_coordinates, MPI.DOUBLE], root=0)
comm.Bcast([pixel_maxiter, MPI.INT], root=0)


#print("plane_coordinates", plane_coordinates)
#print("pixel_maxiter", pixel_maxiter)
 
amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
fh = MPI.File.Open(comm, "deneme", amode)

buffer_1= plane_coordinates

offset_1 = rank * plane_coordinates.nbytes // size

fh.Set_view(offset_1,etype=MPI.DOUBLE)

print("rank",rank,"offset_1",offset_1)

fh.Write_at_all(offset_1,buffer_1)

buffer_2 = pixel_maxiter

offset_2 = plane_coordinates.nbytes + rank * pixel_maxiter.nbytes // size

fh.Set_view(offset_2,etype=MPI.INT)

print("rank",rank,"offset_2",offset_2)

fh.Write_at_all(offset_2,buffer_2)

buffer_3 = array

filetype = MPI.INT.Create_contiguous(array.shape[0])
filetype.Commit()

displacement = plane_coordinates.nbytes + pixel_maxiter.nbytes + rank * array.nbytes // size

fh.Set_view(disp = displacement, etype = MPI.INT, filetype = filetype)

print("rank",rank, "offset_3", displacement)

fh.Write_at_all(displacement, buffer_3)

filetype.Free()

fh.Close()