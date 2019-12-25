
def Lagrange(x, y, z):
  t1_start = perf_counter()
  n = len(x)
  r = 0
  for i in range(n):
    c = 1
    #d = 1
    for j in range(n):
      if i!=j:
        c = c*((z - x[j])/(x[i] - x[j]))
    r = r + (y[i] * c)
  print("O valor de z interpolado é: ", r)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
  return r
