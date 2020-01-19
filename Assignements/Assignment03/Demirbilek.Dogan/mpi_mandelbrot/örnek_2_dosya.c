MPI_File file;

  MPI_File_open(MPI_COMM_WORLD, "image.pgm", MPI_MODE_CREATE | MPI_MODE_WRONLY, MPI_INFO_NULL, &file);


  int header;
  if( myid == 0 ) header = start_image( Imax, Nx, Ny, "image.pgm" );
  MPI_Bcast( &header, 1, MPI_INT, 0, MPI_COMM_WORLD );


mysize=N/numprocs + (myid<N%numprocs);


    //now I want to write the matrix in a binary file with MPI I/O
    MPI_File matrixFile;
    MPI_File_open(MPI_COMM_WORLD,"mymatrix",MPI_MODE_CREATE|MPI_MODE_WRONLY,MPI_INFO_NULL,&matrixFile);
    //master will write n_x, n_y and I_max -    IT WORKS
    if(myid==0){
        MPI_File_write(matrixFile,coordinates,4,MPI_DOUBLE,MPI_STATUS_IGNORE);
        MPI_File_write_at(matrixFile,4*sizeof(double),&n_x,1,MPI_INT,MPI_STATUS_IGNORE);
        MPI_File_write_at(matrixFile,4*sizeof(double)+sizeof(int),&n_y,1,MPI_INT,MPI_STATUS_IGNORE);
        MPI_File_write_at(matrixFile,4*sizeof(double)+2*sizeof(int),&I_max,1,MPI_UNSIGNED_SHORT,MPI_STATUS_IGNORE);
    }


    //I need to define a pattern to write the file: one write numprocs-1 skip
    MPI_Datatype Myblock;
    // (how many elements, one at time, separated by a stride of numprocs)
    MPI_Type_vector(N/numprocs,1,numprocs,MPI_UNSIGNED_SHORT,&Myblock);
    MPI_Type_commit(&Myblock);

    //each proc write its elements without reminder
    //i skip the first 2 integers an myid+1 unsigned long int (I_max and start of other procs)
    MPI_Offset mydisp = 4*sizeof(double)+2*sizeof(int)+sizeof(unsigned short int)*(myid+1);
    MPI_File_set_view(matrixFile,mydisp,MPI_UNSIGNED_SHORT,Myblock,"native",MPI_INFO_NULL);
    MPI_File_write_all(matrixFile,matrix,N/numprocs,MPI_UNSIGNED_SHORT,MPI_STATUS_IGNORE);

    //I take care of the reminder
    if (myid < N%numprocs){
        // I need to skip the headers and (N/numprocs)*numprocs uns short int and myid
        mydisp = 4*sizeof(double)+2*sizeof(int)+sizeof(unsigned short int)*((N/numprocs)*numprocs+myid+1);
        MPI_File_write_at_all(matrixFile,mydisp,&matrix[mysize-1],1,MPI_UNSIGNED_SHORT,MPI_STATUS_IGNORE);
    }

    MPI_File_close(&matrixFile);
    MPI_Type_free(&Myblock);
    free(matrix);
    MPI_Finalize() ;

    //this is just to see if the result is correct looking at the image
    int nx, ny;
    unsigned short int Imax;

    FILE *file;
    file = fopen("mymatrix","rb");
    int d = fileno(file);
    ssize_t out = pread(d,&nx,sizeof(int),4*sizeof(double));
    out = pread(d,&ny,sizeof(int),4*sizeof(double)+sizeof(int));
    out = pread(d,&Imax,sizeof(unsigned short int),4*sizeof(double)+sizeof(int)*2);
    unsigned short int* m = (unsigned short int*)malloc( nx*ny * sizeof( unsigned short int) );
    out = pread(d,m,nx*ny*sizeof(unsigned short int),4*sizeof(double)+sizeof(int)*2+sizeof(unsigned short int));
    fclose(file);
    write_pgm_image(m, Imax, nx, ny, "image.pgm" );
    free(m);

}


