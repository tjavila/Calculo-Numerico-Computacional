import numpy as np
import math
from scipy import misc
import matplotlib.pyplot as plt
from time import perf_counter



def falsapos(f,a, b, precisao):
  t1_start = perf_counter()
  n = 0
  lista = []
  if(f(a) * f(b) < 0):
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    while(abs(f(x)) > precisao and abs(b - a)>precisao):
      if(n>=500):
        break
      if(f(a) * f(x) < 0):
        b = x
      else:
        a = x
      
      x = (a * f(b) - b * f(a)) / (f(b) - f(a))
      n = n + 1
      lista.append(x)
      
    print("A raiz do intervalo dado é: ", x)
    print("Número de iterações: ", n)
    t1_stop = perf_counter()
    print(t1_stop - t1_start)
  else:
    print("Não há raízes no intervalo dado")
    t1_stop = perf_counter()
    print(t1_stop - t1_start)
  return lista
