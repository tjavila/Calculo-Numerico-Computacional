
def Newton(x, y, z):
  t1_start = perf_counter()
  r = 0
  n = len(x)
  dely = np.zeros_like(y)
  for i in range (n):
    dely[i]= y[i]
    
  for k in range(1,n):
    for i in range(n, k, -1):
      dely[i-1] = (dely[i-1] - dely[i-1-1])/(x[i-1]- x[i-k-1])
  
  r = dely[n-1]
  
  for i in range(n-1, 0, -1):
    r = r * (z - x[i-1]) + dely[i-1]
  
  print("O valor de z interpolado é: ", r)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
