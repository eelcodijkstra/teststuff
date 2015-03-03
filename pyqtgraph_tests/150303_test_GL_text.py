# From http://stackoverflow.com/questions/27571494/how-to-avoid-using-global-variable-to-set-text-in-glviewwidget

import pyqtgraph.opengl as gl
from PyQt4.Qt import QApplication

class MyGLView(gl.GLViewWidget):
    def __init__(self, text):
        super(MyGLView, self).__init__()
        self.text = text

    def setText(self, text):
        self.text = text
        self.update()

    def paintGL(self, *args, **kwds):
        gl.GLViewWidget.paintGL(self, *args, **kwds)
        self.renderText(0, 0, 0, self.text)


app = QApplication([])
w = MyGLView(text="O HAI World")
w.show()

import time
time.sleep(3)
