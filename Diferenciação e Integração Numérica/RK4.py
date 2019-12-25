def RungeKutta4(l1, l2, b, h, func):
  t1_start = perf_counter()
  n = round((b - l1) / h)
  x = np.zeros(n+1)
  y = np.zeros(n+1)
  x[0] = l1
  y[0] = l2

  for i in range(0,n):
    x[i+1] = x[i] + h
    k1 = func(x[i], y[i])
    k2 = func(x[i] + 0.5 * h, y[i] + h* 0.5 * k1)
    k3 = func(x[i] + 0.5 * h, y[i] + h* 0.5 * k2)
    k4 = func(x[i] + h, y[i] + h*k3)
    y[i+1] = y[i] + h * (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4)

  t1_stop = perf_counter()
  print(t1_stop - t1_start)
  return list(zip(x, y))
