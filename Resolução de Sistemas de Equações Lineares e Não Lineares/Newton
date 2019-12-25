import numpy as np
import math
import matplotlib.pyplot as plt
from time import perf_counter
from scipy import linalg
from __future__ import division  
from time import perf_counter


def newton(F, J, x, eps):
  t1_start = perf_counter()
  Ff = F(x)
  Fn = np.linalg.norm(Ff, ord=2)
  it = 0
  while abs(Fn) > eps and it < 4:
      delta = np.linalg.solve(J(x), -Ff)
      x = x + delta
      Ff = F(x)
      Fn = np.linalg.norm(Ff, ord=2)
      it += 1
      print(x, it)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
