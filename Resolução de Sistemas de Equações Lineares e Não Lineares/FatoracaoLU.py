import numpy as np
import math
import matplotlib.pyplot as plt
from time import perf_counter
from scipy import linalg
from __future__ import division  
from time import perf_counter

def fatLU(A, b, m):
  t1_start = perf_counter()
  U = np.copy(A)
  n = np.shape(U)[0]
  L = np.eye(n)
  
  for j in np.arange(n-1):
    for i in np.arange (j+1, n):
      L[i][j] = round(U[i][j]/U[j][j], m)
      for k in np.arange(j+1, n):
        U[i][k] = round(U[i][k] - L[i][j] * U[j][k], m)
      U[i][j] = 0
  print("L:", L)
  print("U:", U)
  
  y = np.linalg.solve(L, b)  
  x = np.linalg.solve(U, y) 
  
  for i in range(0,n):
    y[i] = round(y[i],m)
    
  for i in range(0,n):
    x[i] = round(x[i],m)
  
  print("X:", x)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
