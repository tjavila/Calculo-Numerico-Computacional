import numpy as np
import math
import matplotlib.pyplot as plt
from time import perf_counter
from scipy import linalg
from __future__ import division  
from time import perf_counter

def cholesky(A, b, m): 
  t1_start = perf_counter()
  n = len(A)
  L = np.zeros_like(A)
    
  for j in range(0,n):
      for k in range(0, j+1):
        if j==k:
          t= A[j,j] - np.sum(np.square(L[j,:j]))
          if t>0:
            L[j,j] = np.sqrt(t)
        else:
          L[j,k] = (A[j,k] - np.sum(L[j,:k]*L[k,:k]))/L[k,k]
      
        At = L.T
      
  y = np.linalg.solve(L, b)  
  x = np.linalg.solve(At, y)  
  
  
  for i in range (0,n):
    y[i] = round(y[i], m)
  for i in range (0,n):
    x[i] = round(x[i], m)
  
  print("L:", L)
  print("Lt:", At)
  print("y:", y)
  print("x:", x)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
