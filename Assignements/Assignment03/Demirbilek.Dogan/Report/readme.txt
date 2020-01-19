# OPENMP

**Ulysses compiler and openmp info**

gcc compiler 4.9 patchevel 2
OpenMP supported version is 4.0

**My compiler and openmp info**

gcc compiler 7.4 patchevel 0
OpenMP supported version is 4.5
	
To be able to compile code in Ullyses (parallel) following bash command can be used --> gcc -fopenmp -o parallel_MandeBrot.x parallel_MandeBrot.c -lm -std=gnu11
To be able to compile code in Ullyses (serial) following bash command can be used --> gcc -o serial_MandeBrot.x parallel_MandeBrot.c -lm -std=gnu11 -lrt


# MPI

To run the python mpi program, mpi4py package for python must be installed. (anaconda distribution highly recommended)


mpi4py is compatible with Python 3.6 not 3.7 so in order to run the program below steps should be followed

1- conda create -n <enviroment name> python=3.6 anaconda --> with this command new enviroment will be created.
2- conda activate <enviroment name> --> new enviroment will be activated
3- conda install -c anaconda mpi4py, conda install -c anaconda numpy, conda install -c anaconda matplotlib --> install the required packages.


To run these programs from the terminal mpiexec / mpirun -np {number_of_processor} python mpi_mandelbrot.py / read_io_output.py command



Rest of the scripts are the plot scripts which are asked throughout the sections. In order to run them from the terminal "python script_name" will be sufficient.

	*Important note, for the scripts output or input files should be in same directory.*


For all programs:

Python 3.6.9 :: Anaconda, Inc.
numpy 1.17.4
matplotlib: 3.1.1
mpi4py 3.0.3

packages are used.
