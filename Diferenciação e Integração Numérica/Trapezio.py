def Trapezio(l1, l2, n, func):
  t1_start = perf_counter()
  h =(l2 - l1)/n
  res = np.zeros(n+1)
    
  for i in range(1, n+1):
    if(i == 0) or (i == n):
      c = 1
    else:
      c = 2
    res[i] = c*func(l1+i*h)

  res2 = (h/2) * sum(res)

  print(res2)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
