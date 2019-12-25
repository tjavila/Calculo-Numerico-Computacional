def Simpson13(l1, l2, n, func):
  t1_start = perf_counter()
  h = (l2 - l1)/n

  x = list()
  fx = list()

  for i in range(0, n+1):
    x.append(l1 + i * h)
    fx.append(func(x[i]))

  res = 0

  for i in range(0,n+1):
    if i == 0 or i == n:
      res+= fx[i]
    elif i % 2 != 0:
      res+= 4 * fx[i]
    else:
      res+= 2 * fx[i]

  res = res * (h/3)
  print(res)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
