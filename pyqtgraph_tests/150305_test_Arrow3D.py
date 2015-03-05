# Example from http://www.pyqtgraph.org/documentation/qtcrashcourse.html

from PyQt4 import QtGui, QtCore 
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
from MyMeshData import MyMeshData


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

## Create arrow
arrow_length = 1.0
arrow_md = MyMeshData.arrow(rows=10, cols=20, radius = 0.05, length=arrow_length)
colors = np.zeros((arrow_md.faceCount(), 4), dtype=float)
colors[:,0] = 1.0
colors[:,3] = 1.0
arrow_md.setFaceColors(colors)
arrow = gl.GLMeshItem(meshdata=arrow_md, smooth=True, drawEdges=True, edgeColor=(1,0,0,1), shader='balloon')
plot.addItem(arrow)

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
# Set up some animation parameters
frametime = 50 # frame refresh time in ms
velocity = 1./frametime
n_rotations_per_second = 0.5
n_rotations = 3.0
counter = 0

# Function to update scene for each frame
def update():
    global counter, frametime, n_rotations, n_rotations_per_second
    global arrow_length
    counter +=1
    n_steps_per_rotation = 1000./frametime
    rotation_angle = 360.0/n_steps_per_rotation
    n_draws = n_rotations * n_steps_per_rotation
    if counter <= n_draws:
        arrow.rotate(rotation_angle, 0, 1, 0)
        if counter < n_draws:
            z_scale = 0.95
        else:
            z_scale = 1.1
        arrow.scale(1, 1, z_scale)
        
# Set up timer for animation
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(frametime)

## Start the Qt event loop
app.exec_()
