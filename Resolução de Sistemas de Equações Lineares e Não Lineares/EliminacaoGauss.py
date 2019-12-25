import numpy as np
import math
import matplotlib.pyplot as plt
from time import perf_counter
from scipy import linalg
from __future__ import division  
from time import perf_counter

def eliminacaoGauss(A, b, m):
  t1_start = perf_counter()
  n = len(A)
  Det = 1
  for j in range(0,n-1):      
    Det = Det*A[j][j]
    if abs(A[j][j]) != 0:
      r = 1/A[j][j]
      for i in range(j+1,n):
        Mult = A[i][j]*r
        A[i][j] = 0
        for k in range(j+1,n):
          A[i][k] = A[i][k] - Mult*A[j][k]
          
        b[i] = b[i] - Mult*b[j]
        
  Det = Det*A[n-1][n-1]
  print('Determinante: ', Det)
  print('Matriz resultante:')
  print(A)
      
  x = linalg.solve(A, b)
  x = np.round(x, m)
  print("X:",x) 
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
