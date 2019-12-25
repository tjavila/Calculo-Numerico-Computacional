def MMQ(x, y, tipo):
  t1_start = perf_counter()
  n = len(x)
  raizes = np.zeros(n)
  xy2 = np.zeros(n)
  quad = np.zeros(n)
  
  for i in range (0,n):
    xy2[i] = x[i] * y[i]
    quad[i] = math.pow(x[i], 2)
  
  somax = sum(x)
  somay = sum(y)
  somaxy = sum(xy2)
  somaquad = sum(quad)

  a1 = (n * somaxy) - (somax * somay)
  a2 = (n * somaquad) - (somax * somax)
  a = a1/a2
  print(a)
  b1 = (somax * somaxy) - (somay * somaquad)
  b2 = (somax * somax) - (n * somaquad)
  b =  b1/b2
  print(b)

  if(tipo == 1):
    f = lambda x: a*x + b
    for i in range (0, n):
      raizes[i] = f(x[i]) 
  
  else:
      if(tipo == 2):
        f = lambda x: a*(x**2) + b*(1/x)
        for i in range (0, n):
          raizes[i] = f(x[i])
      
      
  print(raizes)
  t1_stop = perf_counter()
  print(t1_stop - t1_start)
  plt.grid()
  plt.title('MMQ')
  plt.axhline(0, color = 'gray')
  plt.axvline(0, color = 'gray')
  plt.plot(x, y, '.', color = 'r', label = 'Pontos')
  plt.plot(x, raizes, '-', color = 'g', marker = ".", label = 'Funçao ajustada')
  plt.legend(loc = 'upper left')
  plt.show()
