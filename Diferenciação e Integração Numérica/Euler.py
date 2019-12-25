def Euler(l1, l2, z, h, f):
  t1_start = perf_counter()
  n = round((z - l1) / h)
  x = np.zeros(n+1)
  y = np.zeros(n+1)

  x[0] = l1
  y[0] = l2

  for i in range(n):
    x[i+1] = x[i] + h
    y[i+1] = y[i] + h * f(x[i], y[i])
  
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
  return list(zip(x, y))
