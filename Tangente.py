import numpy as np
import math
from scipy import misc
import matplotlib.pyplot as plt
from time import perf_counter


def tangente(f, x, precisao):
  t1_start = perf_counter()
  n = 0
  lista = []
  if(abs(f(x)) < precisao):
    x1 = x
    print("A raiz é: ", x1)
    print("Número de iterações: 1")
  
  else:
    while(True):
      if(n>=500):
        print("A raiz é: ", x)
        print("Número de iterações: ", n)
        t1_stop = perf_counter()
        print(t1_stop - t1_start)
        return lista
        break
      x2 = x - (f(x)/misc.derivative(f,x))
      n = n + 1
      lista.append(x2)
  
      if(abs(f(x2))< precisao or abs(x2 - x) < precisao):
        x1 = x2
        print("A raiz é: ", x1)
        print("Número de iterações: ", n)
        t1_stop = perf_counter()
        print(t1_stop - t1_start)
        return lista
        break
      else:
        x = x2
