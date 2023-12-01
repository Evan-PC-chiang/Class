import generate_frame
import numpy as np
from mpi4py import MPI # import MPI


# get the 'communicator'
comm = MPI.COMM_WORLD

# get the 'rank' of the process
my_rank = comm.rank

# get the total number of processes
total_ranks = comm.size # number of copies running.

# print the rank
print(f"I am {my_rank} of {total_ranks}.") 

# make a matrix from 0 to 719, with 20 rows
# this is the number of frames we want to generate
# each process will get a row of this matrix
# so that each process generates 36 frames
# (720/20 = 36)
Index = np.matrix(range(720)).reshape(20,36)
A = np.asarray(Index[my_rank,1:]).reshape(-1)

for i in A:
    generate_frame.generate_frame(i)
    print(f"Process {my_rank} generated frame {i}.")

# salloc -A r00389 -p debug -N 1 -n 20 -t 30
# srun -n 20 python3 -u parallel_generate_frames.py
