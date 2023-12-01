#!/usr/bin/env python3

# import MPI
from mpi4py import MPI

# get the mpi rank
rank = MPI.COMM_WORLD.rank

if rank == 0:
    # reading file from a list
    full_list = list(range(100))
else:
    full_list = None

# bcast the list (copied to all ranks)
my_list = MPI.COMM_WORLD.bcast(full_list, root=0)

print(f"{rank}: {my_list}.")