import math
from scipy import misc
import matplotlib.pyplot as plt
from time import perf_counter

def bisseccao(f, a, b, precisao):
  t1_start = perf_counter()
  n = 0
  lista = []
  if(f(a) * f(b) < 0):
    x = (a + b)/2
    while(abs(f(x)) > precisao):
      if(n<500):
        if(f(a) * f(x) < 0):
          b = x
        else:
          a = x
        x = (a + b)/2
        n = n + 1
        lista.append(x)
    print("A raiz no intervalo dado é: ", x)
    print("Número de iterações: ", n)
    t1_stop = perf_counter()
    print(t1_stop - t1_start)
  else:
    print("Não há raízes no intervalo dado")
    t1_stop = perf_counter()
    print(t1_stop - t1_start)
  return lista
