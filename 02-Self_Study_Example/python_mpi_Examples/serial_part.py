import numpy as np
from timeit import default_timer as timer

N = int(input("Please enter the N: "))

N_array = np.arange(1,N+1)

start = timer()

np.sum(N_array)

end = timer()

print("Sum of numbers are ",np.sum(N_array) )

print("Serial execeution time is: ",end-start, "second")
