#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <omp.h>

#define CPU_TIME (clock_gettime( CLOCK_REALTIME, &ts ), (double)ts.tv_sec +	\
		  (double)ts.tv_nsec * 1e-9)


int main (int argc, char ** argv) {

  if (argc<2)
    {
      printf(" Usage: %s number \n",argv[0]);
      return 1;
    }

  struct  timespec ts;

  long long int N = atoll(argv[1]);
  long long int M = 0 ;
  double pi = 0;
  // point coordinates
  double x , y;
  long long int i;
  unsigned int seed;
  double tstart,tend;
  int     nthreads = 1;
  

  struct drand48_data buf;

#if !defined(_OPENMP)

printf("Serial approach\n");

#define seed 68111 // seed for number generator
  
srand48 ( seed ) ; // seed the number generator

tstart  = CPU_TIME;

  for (i = 0 ; i < N ; i++)
    {
      // take a point P(x,y) inside the unit square
      x = drand48(); 
      y = drand48();
      
      // check if the point P(x,y) is inside the circle
      if ((x*x + y*y)<1)
	M++; 
    }

tend = CPU_TIME;

#else

#pragma omp parallel
#pragma omp master
  nthreads = omp_get_num_threads();

  printf("omp summation with %d threads\n", nthreads );

#pragma omp parallel default(none) private(nthreads,i,x,y,seed,buf) shared(tstart,tend,ts,N,M)
{

seed = 68111 * omp_get_thread_num();
srand48_r(seed, &buf);

tstart  = CPU_TIME;

#pragma omp for reduction(+:M)

  for (i = 0 ; i < N ; i++)
    {
      // take a point P(x,y) inside the unit square
      drand48_r(&buf,&x); 
      drand48_r(&buf,&y);

      // check if the point P(x,y) is inside the circle
      if ((x*x + y*y)<1)
	M++; 
    }
}
tend = CPU_TIME;

#endif

  pi = 4.0*M/N ; // calculate area
  printf ( "\n # of trials = %llu , estimate of pi is %1.9f \n", N, pi ) ;

  //total_time= (double)(end_time - start_time) / CLOCKS_PER_SEC;
  printf ( "\n # walltime : %f \n", tend-tstart );

  return 0;
}
