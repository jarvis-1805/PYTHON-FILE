import math
import matplotlib.pyplot as plt

def fnplot(x, y, fname):
  plt.plot(x, y)
  plt.xlabel('value of x')
  plt.ylabel(fname)
  plt.title(fname)
  plt.show()

fnplot([x for x in range(10)], [math.sin(x) for x in range(10)], 'sin(x)')
fnplot([x for x in range(10)], [math.cos(x) for x in range(10)], 'cos(x)')
fnplot([x for x in range(-10, 10)], [(x**2 - 4*x -1) for x in range(-10, 10)], 'x^2 - 4*x - 1')
fnplot([x for x in range(10)], [math.exp(x) for x in range(10)], 'exp(x)')