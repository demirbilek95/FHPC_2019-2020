#include <stdlib.h>
#include <stdio.h>
#include "math.h"
#include <complex.h>
#include <mpi.h>
#include <time.h>

// default values for the parameters 
#define N_X 900
#define N_Y 600
#define X_L -2.1
#define Y_L -1
#define X_R 0.7
#define Y_R 1.1
#define I_MAX 20000

void write_pgm_image( void *image, int maxval, int xsize,
                        int ysize, const char *image_name);

int main( int argc, char **argv ) {

    double start_time, end_time;
    int myid , numprocs , proc, len;
        MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD,&myid);

    // Where are my processes?
    char hostname[MPI_MAX_PROCESSOR_NAME];
    MPI_Get_processor_name(hostname, &len);
    printf ("Number of tasks= %d My rank= %d Running on %s\n",numprocs,myid,hostname);

    short int n_x = N_X;
    short int n_y = N_Y;
    double x_l = X_L;
    double y_l = Y_L;
    double x_r = X_R;
    double y_r = Y_R;
    unsigned short int i_max = I_MAX;
    double complex z, c;
    unsigned short int iter;
    short int *m;
    short int *M;

    // input parameters
    if ( argc > 1 ) {
            n_x = atoi( *(argv+1) );
        n_y = atoi( *(argv+2) );
        if ( argc > 3 ) {
            x_l = atof( *(argv+3) );
            y_l = atof( *(argv+4) );
            x_r = atof( *(argv+5) );
            y_r = atof( *(argv+6) );
            if ( argc > 7 )
                i_max = atoi( *(argv+7) );
        }
    }

    if(myid==0) {
        // big matrix M allocation
        if ((M = (short int*)malloc(n_x * n_y * sizeof(short int))) == NULL) {
            printf("Not enough memory");
            return 1;
        }
    }

    // small matrices m allocation
    int chunk = n_x * n_y / numprocs;
    if ((m = (short int*)malloc(chunk * sizeof(short int))) == NULL) {
        printf("Not enough memory");
        return 1;
    }

    int start_point = n_y/numprocs*myid;
    double xscale = (x_r - x_l)/(n_x-1);
    double yscale = (y_r - y_l)/(n_y-1);
    start_time = MPI_Wtime();
    for(int i = 0; i<n_x; i++) {
        for(int j = start_point; j<n_y/numprocs*(myid+1); j++) {
            c = (x_l + xscale*i) + (y_r - yscale*j)*I;
            z = 0;
            iter = 0;
            while(cabs(z) < 2 && iter < i_max) {
                z = z*z + c;
                iter++;
            }
            m[(j-start_point)*n_x+i] = iter == i_max ? 0 : iter;
        }
    }

    // the master thread builds the matrix M from the other threads
    MPI_Gather(m, chunk, MPI_UNSIGNED_SHORT, M, chunk, MPI_UNSIGNED_SHORT, 0, MPI_COMM_WORLD);

    end_time=MPI_Wtime();
    free(m);
    if(myid == 0){
        write_pgm_image(M, i_max, n_x, n_y, "mandelbrot_mpi.pgm" );
        free(M);
    }
    printf ("%10.8f\n",end_time - start_time);
    MPI_Finalize() ;

}

void write_pgm_image( void *image, int maxval, int xsize, int ysize, const char *image_name) {
  FILE* image_file;
  image_file = fopen(image_name, "w");
  int color_depth = 1+((maxval>>8)>0);
  fprintf(image_file, "P5\n%d %d\n%d\n", xsize, ysize, maxval);
  fwrite( image, color_depth, xsize*ysize, image_file);
  fclose(image_file);
  return ;
}



