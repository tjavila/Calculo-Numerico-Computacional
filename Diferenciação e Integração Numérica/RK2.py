def RungeKutta2(l1, l2, z, h, func):
  t1_start = perf_counter()
  n = round((z-l1)/h)
  x = np.zeros(n+1)
  y = np.zeros(n+1)
  x[0] = l1
  y[0] = l2

  for i in range(0,n):
    x[i+1] = x[i] + h
    k1 = h*func(y[i])
    k2 = h*func(y[i] + k1)
    y[i+1] = y[i] + (h/2)*(k1 + k2)
  
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
  return list(zip(x, y))
