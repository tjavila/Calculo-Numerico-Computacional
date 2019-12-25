def Simpson38(l1, l2, n, func):
  t1_start = perf_counter()
  h = (float(l2 - l1)/n)

  res = func(l1) + func(l2)

  for i in range(1, n):
    if(i%3 == 0):
      res+= 2 * func(l1 + i * h)
    else:
      res+= 3 * func(l1 + i * h)

  res = (float(3 * h)/8) * res

  print(res)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
