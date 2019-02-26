from math import *

def factors(n):
  flist = []
  for i in range(1,n+1):
    if n%i == 0:
       flist.append(i)
  return(flist)

def isprime(n):
  return(factors(n) == [1,n])


def issquare(n):
  root = int(sqrt(n))
  return(n == root*root)

"""
def sqpr(l):
  if len(l) < 1:
    return(True)
  elif issquare(l[0]):
    if len(l) == 1:
      return(True)
    else:
      return(prsq(l[1:]))
  else:
    return(False)

def prsq(l):
  if len(l) < 1:
    return(True)
  elif isprime(l[0]):
    if len(l) == 1:
      return(True)
    else:
      return(sqpr(l[1:]))
  else:
    return(False)

def primesquare(l):
  return(sqpr(l) or prsq(l))
"""

n = int(input("Enter prime number to fidn quare : "))
print(issquare(n))