import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt
import sys

def mandelbrot(x, y, Imax):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < Imax:
        z = z**2 + c
        it += 1
    return it

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


if rank == 0:
	#Default parameters
        
    print("Running MPI Mandelbrot with {} cores".format(size))

    nx, ny, xL, yL, xR, yR, Imax  =500, 500, -2, -2, +2, +2, 1000

    if len(sys.argv) == 8:

        nx, ny, xL, yL, xR, yR, Imax  = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]

        print("Using assigned parameters nx = {}, ny = {}, xL = {}, yL = {}, xR = {}, yR = {}, Imax = {}".format(nx, ny, xL, yL, xR, yR, Imax))

    else:
        print("To assign paramters: mpirun -np 4 {} nx ny xL yL xR yR Imax \n".format(sys.argv[0]));
        print("Using default parameters nx = {}, ny = {}, xL = {}, yL = {}, xR = {}, yR = {}, Imax = {}".format(nx, ny, xL, yL, xR, yR, Imax))


tstart = MPI.Wtime()

plane_coordinates = np.zeros(4, dtype='d') 
pixel_maxiter = np.zeros(3, dtype='i')

if rank == 0:
    plane_coordinates[:] = [xL, xR, yL, yR]
    pixel_maxiter[:] = [nx, ny, Imax]

    
# Splitting data to other cores
comm.Bcast([plane_coordinates, MPI.FLOAT], root=0)
comm.Bcast([pixel_maxiter, MPI.INT], root=0)



xL, xR, yL, yR = [float(r) for r in plane_coordinates]
nx, ny, Imax    = [int(i) for i in pixel_maxiter]
dx = (xR - xL) / nx
dy = (yR - yL) / ny

# Amount of work that will be done from the core
N = ny // size + (ny % size > rank)  # integer division + reminder 
N = np.array(N, dtype='i')
# indices of lines to compute here
I = np.arange(rank, ny, size, dtype='i')

# iterating over pixels
C = np.zeros([N, ny], dtype='i')
for k in np.arange(N):
    y = yL + I[k] * dy
    for j in np.arange(ny):
        x = xL + j * dx
        C[k, j] = mandelbrot(x, y, Imax)
        #print("rank", rank,"I[k]",I[k], "------>", "k,j=",k,j,"----->","C[k,j]","----->"	)

#print("rank", rank, "matrix\n", C, "\nshape of matrix\n", C.shape, "\nindices\n", I)

        
# gather results at root
counts = 0
indices = None
cdata = None

if rank == 0:
	counts = np.empty(size, dtype='i')
	indices = np.empty(ny, dtype='i')
	cdata = np.empty([ny, nx], dtype='i')


comm.Gather(sendbuf=[N, MPI.INT],
            recvbuf=[counts, MPI.INT],
            root=0)

#print("rank",rank,"counts",N)

comm.Gatherv(sendbuf=[I, MPI.INT],
             recvbuf=[indices, (counts, None), MPI.INT],
             root=0)

#print("rank",rank,"indices",I)

comm.Gatherv(sendbuf=[C, MPI.INT],
             recvbuf=[cdata, (counts*nx, None), MPI.INT],
             root=0)

#print("rank",rank, "cdata",C)


if rank == 0:
    M = np.zeros([ny,nx], dtype='i')
    M[indices, :] = cdata

else:
    M = np.zeros([ny,nx], dtype='i')
    
tend = MPI.Wtime()

wct = comm.gather(tend-tstart, root=0)
if rank == 0:
    for rank_id, time in enumerate(wct):
        print('wall clock time of processor %d is: %8.2f seconds' % (rank_id,time))
    
    plt.gray()
    plt.imshow(M)
    plt.savefig("mandelbrot_mpi.png")
    #plt.show()

## MPI IO Part

# Broadcast the array that we are going to write with io
comm.Bcast([M, MPI.INT], root=0)

amode = MPI.MODE_WRONLY|MPI.MODE_CREATE
fh = MPI.File.Open(comm, "io_output", amode)

# Writing the coordinates

buffer_1= plane_coordinates

offset_1 = rank * plane_coordinates.nbytes // size

#print("plane_coordinates",plane_coordinates.nbytes)

#print("rank",rank,"offset_1",offset_1)

fh.Set_view(offset_1,etype=MPI.DOUBLE)

fh.Write_at_all(offset_1,buffer_1)

# Writing the pixels

buffer_2 = pixel_maxiter

offset_2 = plane_coordinates.nbytes + rank * pixel_maxiter.nbytes // size
#print("rank",rank,"offset_2",offset_2)

fh.Set_view(offset_2,etype=MPI.INT)

fh.Write_at_all(offset_2,buffer_2)

# Writing the matrix

buffer_3 = M

filetype = MPI.INT.Create_contiguous(M.shape[0])
filetype.Commit()

displacement = plane_coordinates.nbytes + pixel_maxiter.nbytes + rank * M.nbytes // size

#print("rank",rank,"offset_3",displacement)
fh.Set_view(disp = displacement, etype = MPI.INT, filetype = filetype)

fh.Write_at_all(displacement, buffer_3)

filetype.Free()
fh.Close()