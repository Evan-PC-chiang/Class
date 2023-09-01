# -*- coding: utf-8 -*-


""" exp(x) """
def exp(x):
  # initialize e
  e = 1

  plus = 1

  # loop times
  n = 100

  # iteration
  for i in range(1,n):
    plus *= (1/i)
    e += plus

  # fron e to exp(x)
  x = e**x
  return(x)


""" factoria """
def factorial(n):
  # exception for 0!
  if n == 0:
      return 1
      # multiply n times to get n!
  return n * factorial(n - 1)


""" pi """
def pi():
  # initialize pi
  pi = 0

  # loop times
  n = 15000

  # store values
  pi_list = []

  # iteration
  for i in range(1,n):
    plus = -4*(((-1)**i)*(1/(2*i-1)))
    pi += plus
  return pi


""" cos (degree)"""
# use Taylor series
def cos(x):

  # convert degree to radius (X*pi/180)
  x = x * (pi()/180)

  # set up variables
  result = 1.0
  sign = -1.0
  power = 2

  # iter 20 times
  for n in range(1, 20):
      plus = sign * (x ** power) / factorial(power)
      result += plus
      sign *= -1.0
      power += 2

  return result


""" sin (degree) """
# use sin^2 + cos^2 = 1
def sin(x):
  result = (1 - cos(x)**2)**(1/2)
  return result


""" tan (degree)"""
# use tan=sin/cos
def tan(x):
  result = sin(x)/cos(x)
  return result
