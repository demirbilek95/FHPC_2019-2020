#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <omp.h>

int main (int argc, char ** argv) {

  if (argc<2)
    {
      printf(" Usage: %s number \n",argv[0]);
      return 1;
    }

  long long int N = atoll(argv[1]);
  long long int M = 0 ;
  double pi = 0;
  // point coordinates
  double x , y;
  long long int i;

#pragma omp parallel 
{
int myseed = 68111 * omp_get_thread_num();
unsigned int random_number = rand_r(&myseed);

  #pragma omp for reduction(+:M)

  for (i = 0 ; i < N ; i++)
    {
      // take a point P(x,y) inside the unit square
      x = drand48(); 
      y = drand48();

      // check if the point P(x,y) is inside the circle
      if ((x*x + y*y)<1)
	M++; 
    }

}

  pi = 4.0*M/N ; // calculate area
  printf ( "\n # of trials = %llu , estimate of pi is %1.9f \n", N, pi ) ;
  return 0;
}
