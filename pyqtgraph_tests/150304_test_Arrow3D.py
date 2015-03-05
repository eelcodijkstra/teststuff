# Example from http://www.pyqtgraph.org/documentation/qtcrashcourse.html

from PyQt4 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np


class Arrow3D(gl.GLLinePlotItem):
    def __init__(self, *args, **kwargs):
        super(Arrow3D, self).__init__(*args, **kwargs)


## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()
w.resize(1000,600)

## Create some widgets to be placed inside
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()
plot = gl.GLViewWidget()
plot.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
g = gl.GLGridItem()
#g.rotate(90,1,0,0)
plot.addItem(g)
arrowlength = 1
arrowheadlength = 0.3
pts = np.array( [[0, 0, 0], [0, 0, arrowlength-arrowheadlength]] )
arrowcolor = (255, 0, 0, 255)
linewidth = 7.0
arrow = Arrow3D(pos=pts, color=arrowcolor, mode='line_strip', width=linewidth, antialias=True)
print arrow
plot.addItem(arrow)

md = gl.MeshData.cylinder(rows=10, cols=20, radius=[0.1, 0.0], length=arrowheadlength)
colors = np.zeros((md.faceCount(), 4), dtype=float)
colors[:,0] = 1.0
colors[:,3] = 1.0
md.setFaceColors(colors)
m5 = gl.GLMeshItem(meshdata=md, smooth=True, drawEdges=True, edgeColor=(1,0,0,1), shader='balloon')
m5.translate(0, 0, arrowlength - arrowheadlength)
plot.addItem(m5)

## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)
layout.setColumnStretch (1, 2)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)   # button goes in upper-left
layout.addWidget(text, 1, 0)   # text edit goes in middle-left
layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows

## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
