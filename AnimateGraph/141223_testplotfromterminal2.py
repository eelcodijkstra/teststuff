import numpy as np
from matplotlib import pyplot as plt
import time

X = np.linspace(0,2,100)
Y = X**2 + np.random.random(X.shape)

plt.ion()
fig = plt.figure
ax = plt.subplot(111)
ax.plot(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.title('title')
ax.draw()
time.sleep(0.1)
