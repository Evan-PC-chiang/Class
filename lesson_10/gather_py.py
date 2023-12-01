#!/usr/bin/env python3

# import pi_cal
from pi_cal import picalsec

# import MPI
from mpi4py import MPI

# import numpy
import numpy as np

# get the communicator
comm = MPI.COMM_WORLD

# get the mpi rank
my_rank = comm.rank

# get the total number of processes
total_ranks = comm.size # number of copies running.

# set loop times
n = 180000000

# set the individual result for each rank
Index = np.matrix(range(1,n+1)).reshape(total_ranks,-1)

pi_sap = picalsec(Index[my_rank,:].tolist()[0])

# gather the results on rank 0
full_list = comm.gather(pi_sap, root=0)

# calculate pi
if my_rank == 0:
    avg_rank = sum(full_list)
else:
    avg_rank = None

# print the result
print(f"{my_rank}: pi= {avg_rank}.")