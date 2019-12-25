import numpy as np
import math
import matplotlib.pyplot as plt
from time import perf_counter
from scipy import linalg
from __future__ import division  
from time import perf_counter


def gaussjacobi(A, b, tol, itermax):
  t1_start = perf_counter()
  n = len(A)
  x = np.zeros(n)
  v = np.zeros(n)
  
  for i in range(0,n):
    x[i] = b[i]/A[i][i]
  itera = 0
  while(True):
    itera = itera + 1
    for i in range(0,n):
      Soma = 0
      for j in range(0,n):
        if i != j:
          Soma = Soma + A[i][j]*x[j]
      v[i] = (b[i] - Soma)/A[i][i]
    NormaNum = 0
    NormaDen = 0
    for i in range(0,n):
      t = abs(v[i] - x[i])
      if t> NormaNum:
        NormaNum = t
      if abs(v[i]) > NormaDen:
        NormaDen = abs(v[i])
      x[i] = v[i]
    NormaRel = NormaNum/NormaDen
    print(itera, x, NormaRel)
    if NormaRel <= tol or itera >= itermax:
      break
    
  if (NormaRel <= tol):
    print("Convergiu")
  else:
    print("Não convergiu")
  
  print("Iterações: ", itera)
  print("x: ", x)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
