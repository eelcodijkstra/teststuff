from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.opengl as gl

## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()
w.resize(1000,600)

## Create some widgets to be placed inside
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')

sliderbox = QtGui.QGroupBox()
hBoxLayout = QtGui.QHBoxLayout()
psi_slider_layout = QtGui.QVBoxLayout()
delta_slider_layout = QtGui.QVBoxLayout()

psi_label = QtGui.QLabel('psi')
psi_slider = QtGui.QSlider()
psi_slider.setOrientation(QtCore.Qt.Vertical)
psi_slider.setMinimum(0)
psi_slider.setMaximum(90)
psi_slider.setValue(0)
psi_slider_layout.addWidget(psi_label)
psi_slider_layout.addWidget(psi_slider)
delta_slider_layout.setAlignment(QtCore.Qt.AlignHCenter)

delta_label = QtGui.QLabel('delta')
delta_slider = QtGui.QSlider()
delta_slider.setOrientation(QtCore.Qt.Vertical)
delta_slider.setMinimum(-180)
delta_slider.setMaximum(180)
delta_slider.setValue(0)
delta_slider_layout.addWidget(delta_label)
delta_slider_layout.addWidget(delta_slider)

hBoxLayout.addItem(psi_slider_layout)
hBoxLayout.addItem(delta_slider_layout)
sliderbox.setLayout(hBoxLayout)

wGL = gl.GLViewWidget()
wGL.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
g = gl.GLGridItem()
wGL.addItem(g)

## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)
layout.setColumnStretch (1, 2)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)   # button goes in upper-left
layout.addWidget(sliderbox, 1, 0)   # text edit goes in middle-left
#layout.addWidget(sliderbox, 2, 0)  # list widget goes in bottom-left
#layout.addWidget(text, 1, 0)   # text edit goes in middle-left
layout.addWidget(wGL, 0, 1, 3, 1)  # wGL goes on right side, spanning 3 rows

## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
