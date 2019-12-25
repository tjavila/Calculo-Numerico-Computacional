def plot(pontos, xlabel = "x", ylabel = "f(x)",
         janela_horizontal = (None, None)):  
  pontos = np.array(pontos, "float64")
  a, b = janela_horizontal
  if a is None:
    a = min(pontos[:, 0])
    b = max(pontos[:, 0])

  pontos = np.array(pontos)

  plt.plot(pontos[:, 0], pontos[:, 1], 'x', marker='.', label='')

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

  plt.axhline(0, color = "black")

  plt.grid()

  plt.show()
