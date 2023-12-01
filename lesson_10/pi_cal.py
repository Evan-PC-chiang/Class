#!/usr/bin/env python3

def picalsec(n: list):
  # initialize pi
  pi = 0

  # iteration
  for i in range(n[0],n[-1]):
    plus = -4*(((-1)**i)*(1/(2*i-1)))
    pi += plus

  return pi