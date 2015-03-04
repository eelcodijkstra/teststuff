from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys

class Arrow3D(gl.GLLinePlotItem):
    def __init__(self, pos=pts, mode='line_strip', antialias=True):
        return self