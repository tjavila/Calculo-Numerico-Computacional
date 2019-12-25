import numpy as np
import math
from scipy import misc
import matplotlib.pyplot as plt
from time import perf_counter

def secante(f, x0, x1, precisao):
  t1_start = perf_counter()
  lista = []
  n = 0
  if(abs(f(x1))< precisao or abs(x1 - x0) < precisao):
    xx = x1
    print("A raiz é: ", xx)
    print("Número de iterações: 1")
    t1_stop = perf_counter()
    print(t1_stop - t1_start)
      
  else:
    while(True):
      if(n >= 500):
        print("A raiz é: ", x2)
        print("Número de iterações: ", n)
        t1_stop = perf_counter()
        print(t1_stop - t1_start)
        return lista
        break
      x2 = x0 - (f(x0) /(f(x1)-f(x0))) * (x1 - x0)
      n = n + 1
      lista.append(x2)
      
      if(abs(f(x2))< precisao or abs(x2 - x1) < precisao):
        xx = x2
        print("A raiz é: ", xx)
        print("Número de iterações: ", n)
        t1_stop = perf_counter()
        print(t1_stop - t1_start)
        return lista
        break
      elif (f(x0)*f(x2) < 0):
        x0 = x0
        x1 = x2
      elif (f(x1)*f(x2) < 0):
        x0 = x2
        x1 = x1
