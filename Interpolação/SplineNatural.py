def Spline(x, y, inter):
  t1_start = perf_counter()
  n = len(x)
  a = np.zeros(n - 1)
  b = np.zeros(n - 1)
  c = np.zeros(n - 1)
  d = np.zeros(n - 1)
  
  aux1 = np.zeros(n - 1)
  aux2 = np.zeros(n - 1)
  result = np.zeros(n - 1)
  xx = np.zeros((n, n), dtype=np.float64)
  yy = np.zeros((n))
  
  
  for i in range (n - 1):
    aux1[i] = x[i + 1] - x[i]

  xx[n - 1][n - 1] = 1
  xx[0][0] = 1
  aux = 0
  for i in range(1, n - 1):
    aux = i
    for j in range(0, n):
      if(i == j):
        xx[i][j] = 2*(aux1[j] + aux1[j-1])

      else:
        if ((i - j) != 1 and (j - i) != 1):
          xx[i][j] = 0

        else:
          xx[i][j] = aux1[aux]
          aux = aux - 1
  

  for i in range (1, n - 1):
    yy[i] = 6 * (((y[i + 1] - y[i])/aux1[i]) - ((y[i] - y[i - 1])/aux1[i - 1]))

  aux2 = np.linalg.solve(xx,yy)
  print("Vetor de solução:", aux2)


  for i in range(0, n - 1):
    a[i] = (aux2[i] - aux2[i+1])/(6*aux1[i])
    b[i] = aux2[i+1]/2
    c[i] = (y[i] - y[i+1]/aux1[i]) + (2*aux1[i]*aux2[i+1] - aux2[i]*aux1[i])/6
    d[i] = y[i+1]

  for j in range(0, n - 1):
    result[j] = a[j]*((inter - x[j+1])**3) + b[j]*((inter - x[j+1])**2) + c[j]*(inter - x[j+1]) + d[j] 
    

  for i in range(0, n - 1):
    if(inter > x[i] and inter < x[i + 1]):
      print('Valor aproximado:', result[i])
      print("\n")
      
      numero_pontos = 300
      curve = np.linspace(x[i], x[i+1], numero_pontos)
      
      values = [f(value, a[i], b[i], c[i], d[i], inter) for value in curve] 
      plt.plot(curve, values, linestyle='-', color = 'red', alpha = 0.7)
      plt.plot(curve[0], values[0], marker = 'o', color = 'orange')
      plt.plot(curve[299], values[299], marker = 'o', color = 'orange')

      plt.grid(True)
      plt.show()
      
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
  print("\n")
