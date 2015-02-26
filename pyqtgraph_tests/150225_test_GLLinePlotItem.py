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
w.opts['distance'] = 40
w.show()
w.setWindowTitle('pyqtgraph example: GLLinePlotItem')

gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-2, 0, 0)
#w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -2, 0)
#w.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, -2)
#w.addItem(gz)

# Define a function generating the helix coordinates
def helix(t):
    x = np.cos(4*t)
    y = np.sin(4*t)
    z = t
    return x, y, z
    
# Make a linear space from 0 to 4pi (i.e. 2 revolutions), get coords
t = np.linspace(0, 4*np.pi, 200)
x, y, z = helix(t)

pts = np.vstack([x,z,y]).transpose()
#plt = gl.GLLinePlotItem(pos=pts, color=pg.mkColor(0,0,255), width=2., antialias=True)
plt = gl.GLLinePlotItem(pos=pts, width=2., antialias=True)
w.addItem(plt)    


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
