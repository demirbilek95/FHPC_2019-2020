#include <stdlib.h>
#include <stdio.h>
#include <complex.h>
#include <mpi.h>
#include <time.h>

void write_pgm_image( void *image, int maxval, int xsize, int ysize, const char *image_name){
  FILE* image_file; 
  image_file = fopen(image_name, "w"); 

  int color_depth = 1+((maxval>>8)>0);

  fprintf(image_file, "P5\n%d %d\n%d\n", xsize, ysize, maxval);
  
  fwrite( image, color_depth, xsize*ysize, image_file);  

  fclose(image_file); 
  return ;
}

char MandelBrotPoint_Check(double complex c, int Imax ){
    double complex  z = 0 + 0.0 * I;
    int count = 0;
    //printf("count = %i, Imax = %i\n",count,Imax);
    //printf("%f%+fi\n",creal(c),cimagf(c));
    for (count = 0; count < Imax && cabs(z) < 2; count++){
        z = z * z + c;
    }
    if (cabs(z)>2) // if modulus is bigger than 2, point is unbounded
        //printf(" Sanal sayı %f%+fi -- > abs of sanal sayı %f -- >  iteration %i\n",creal(c),cimagf(c), cabs(z), count );
        return count;
    else
        return Imax-count;   // This point is in mandelbrotset,
}



int main( int argc, char **argv ) {

    double tstart, tend;
    int rank , numprocs ;
    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);

    // Decleariton of variables
    int nx,ny,Imax;  // nx, ny : Pixels, I_max : Maximum number of iteration
    float xL,xR,yL,yR; //c_L : left corner,  x_L + iy_L ,, c_R : right corner,  x_R + iy_R
    double complex z, c;
    char *local_matrix;
    char *Matrix;

 // Check the command line arguments
  if (argc > 7) {

    if(rank==0){
    printf("Using assigned parameters\n");}
    // Assigning command line arguments to variables    
    nx = atoi(*(argv+1));
    ny = atoi(*(argv+2));     // pixels
    xL = atof(*(argv+3));
    yL = atof(*(argv+4));   // left corner of complex plane
    xR = atof(*(argv+5));
    yR = atof(*(argv+6));     // rigt corner of complex plain
    Imax = atoi(*(argv+7));   // max iterations

  }

  else{
    if(rank == 0){
    printf("To assign paramters: %s nx ny xL yL xR yR Imax \n", argv[0]);
    printf("Example: %s 100 100 -2 -2 +2 +2 500\n", argv[0]);}
    // default parameters
    nx = 100;
    ny = 100;
    xL = -2.0;
    yL = -2.0;
    xR = 1.0;
    yR = 1.0;
    Imax = 100;

    if(rank==0){
    printf("Using default parameters nx=%i, ny=%i xL=%f, yL=%f, xR=%f, yR=%f, Imax=%i\n",nx,ny,xL,yL,xR,yR,Imax);}
  }

    if(rank==0) {
        // Matrix allocation
        Matrix = (char*)malloc(nx * ny * sizeof(char));
    }

    // small matrices m allocation
    int chunk = nx * ny / numprocs;
    local_matrix = (char*)malloc(chunk * sizeof(char));

    int start_point = nx/numprocs*rank;

    float dx = (xR - xL) / nx;
    float dy = (yR - yL) / ny; 

   //printf("start point= %i, dx = %f, dy = %f", start_point,dx,dy);


//iterating over rectangle area in complex plaine

    tstart = MPI_Wtime();
  for (int y = 0; y < ny; y++){
    for (int x = start_point; x < nx/numprocs*(rank+1); x++){
        c = xL + (x*dx) + (yL+(y*dy)) * I;
        //printf("%f\n",xL + (x+dx) );  
        printf("rank %i --> %f%+fi\n",rank,creal(c),cimagf(c));
        local_matrix[y*nx+x] = MandelBrotPoint_Check(c, Imax);
    }
  }

    // the master thread builds the matrix M from the other threads
    MPI_Gather(local_matrix, chunk, MPI_CHAR, Matrix, chunk, MPI_CHAR, 0, MPI_COMM_WORLD);

    tend=MPI_Wtime();
    free(local_matrix);
    if(rank == 0){
        write_pgm_image(Matrix, Imax, nx, ny, "mandelbrot_mpi.pgm" );
        free(Matrix);
    }
    printf ("%10.8f\n",tend - tstart);
    MPI_Finalize() ;

}







