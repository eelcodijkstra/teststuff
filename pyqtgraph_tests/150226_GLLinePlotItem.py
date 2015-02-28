# -*- coding: utf-8 -*-
"""
Demonstrate use of GLLinePlotItem to draw parametric curve.

"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
#w.opts['distance'] = 3
w.resize(800,600)
w.show()
w.setWindowTitle('pyqtgraph example: GLLinePlotItem')

g = gl.GLGridItem()
w.addItem(g)

ax = gl.GLAxisItem()
ax.setSize(1.5,4,1.5)
w.addItem(ax)

# Define a function generating the helix coordinates
def helix(t):
    x = np.cos(2*np.pi*t)
    y = np.sin(2*np.pi*t)
    z = t
    return x, y, z
    
# Make a linear space from 0 to 4pi (i.e. 2 revolutions), get coords
t = np.linspace(0, 4, 200)
x, y, z = helix(t)

pts = np.vstack([x,z,y]).transpose()
#plt = gl.GLLinePlotItem(pos=pts, color=pg.mkColor(0,0,255), width=2., antialias=True)
plt = gl.GLLinePlotItem(pos=pts, width=1., antialias=True)
w.addItem(plt)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
