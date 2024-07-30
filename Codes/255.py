import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.5)

y = np.cos(x) + np.sin(x)

solution = x[np.where(y == 0)]
print(solution)
