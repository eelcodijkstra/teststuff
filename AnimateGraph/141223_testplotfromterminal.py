import numpy as np
from matplotlib import pyplot as plt
import time

X = np.linspace(0,2,1000)
Y = X**2 + np.random.random(X.shape)

plt.ion()
fig = plt.plot(X,Y)
plt.show()
time.sleep(0.1)
