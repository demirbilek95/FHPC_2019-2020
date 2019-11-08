There are many scripts in the codes folder so for MPI program **sumNumbers_mpi.py** (naive operation) and **sumNumbers_mpi_collective.py** (collective operaiton) must be considered.

To run the python mpi program, mpi4py package for python must be installed. (anaconda distribution highly recommended)


mpi4py is compatible with Python 3.6 not 3.7 so in order to run the program below steps should be followed

1- conda create -n <enviroment name> python=3.6 anaconda --> with this command new enviroment will be created.
2- conda activate <enviroment name> --> new enviroment will be activated
3- conda install -c anaconda mpi4py  and conda install -c anaconda numpy --> install the required packages.



To run these programs from the terminal mpiexec / mpirun -np {number_of_processor} python sumNumbers_mpi.py / sumNumbers_mpi_collective.py command



Rest of the scripts are the plot scripts which are asked throughout the sections. In order to run them from the terminal python script_name will be sufficient.

	*Important note, for the scripts output or input files should be in same directory.*


For all programs:

Python 3.6.9 :: Anaconda, Inc.
numpy 1.17.2
matplotlib: 3.1.1
mpi4py 2.0.0

packages are used.
