"""

Radiation patter for Hertzian dipole antenna.
April 6, 2015
G. Nordin

"""

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
  
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
#w.setCameraPosition(distance=40)
  
g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)
  
import numpy as np
  
  
## Example 1:
## Array of vertex positions and array of vertex indexes defining faces
## Colors are specified per-face
  
verts = np.array([
    [0, 0, 0],
    [2, 0, 0],
    [1, 2, 0],
    [1, 1, 1],
])
faces = np.array([
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3]
])
colors = np.array([
    [1, 0, 0, 0.3],
    [0, 1, 0, 0.3],
    [0, 0, 1, 0.3],
    [1, 1, 0, 0.3]
])
  
## Example 3:
## sphere


numpnts = 101
xx = np.linspace(-1,1,numpnts)
yy = np.linspace(-1,1,numpnts)
zz = np.linspace(-1,1,numpnts)
data_inorout = np.zeros(shape=(numpnts,numpnts,numpnts))


print xx.shape, data_inorout.shape

md = gl.MeshData.sphere(rows=10, cols=20)
m3 = gl.GLMeshItem(meshdata=md, smooth=False, shader='balloon')
m3.setGLOptions('additive')

#colors = np.random.random(size=(md.faceCount(), 4))
#colors[:,3] = 0.3
#colors[100:] = 0.0
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[:,3] = 0.2
#colors[100:] = 0.0
md.setFaceColors(colors)


#m3.translate(5, -5, 0)
w.addItem(m3)
  
'''  
# Example 4:
# wireframe
  
md = gl.MeshData.sphere(rows=4, cols=8)
m4 = gl.GLMeshItem(meshdata=md, smooth=False, drawFaces=False, drawEdges=True, edgeColor=(1,1,1,1))
m4.translate(0,10,0)
w.addItem(m4)
  
# Example 5:
# cylinder
md = gl.MeshData.cylinder(rows=10, cols=20, radius=[1., 2.0], length=5.)
md2 = gl.MeshData.cylinder(rows=10, cols=20, radius=[2., 0.5], length=10.)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m5 = gl.GLMeshItem(meshdata=md, smooth=True, drawEdges=True, edgeColor=(1,0,0,1), shader='balloon')
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md2.setFaceColors(colors)
m6 = gl.GLMeshItem(meshdata=md2, smooth=True, drawEdges=False, shader='balloon')
m6.translate(0,0,7.5)
  
m6.rotate(0., 0, 1, 1)
#m5.translate(-3,3,0)
w.addItem(m5)
w.addItem(m6)
'''  
  
  
  
  
  
## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
  