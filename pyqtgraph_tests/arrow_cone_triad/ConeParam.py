# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 10:18:27 2014

@author: moynesy
"""
try: 
    from sip import setapi
    setapi("QDate", 2)
    setapi("QDateTime", 2)
    setapi("QTextStream", 2)
    setapi("QTime", 2)
    setapi("QVariant", 2)
    setapi("QString", 2)
    setapi("QUrl", 2)
except:
    pass

from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph.opengl as gl

import numpy as np   

from MyMeshData import MyMeshData   

import sys                

class ConeParam(object):
    """
    Cone's parameter test
    """
    def __init__(self):
        self.props = {}
        self.props['visible'] = True
        self.props['length'] = 1.0
        self.props['radius'] = 1.0
        self.props['cols'] = 4 

        
class ConeWidget(QtGui.QWidget):
    """    
    Widget for editing cone's parameters
    """
    
    signalObjetChanged = QtCore.pyqtSignal(ConeParam, name='coneChanged')    
        
    def __init__(self, parent=None, param=None):
        super(ConeWidget, self).__init__(parent)
    
        if param == None:
            self.param = ConeParam()
        else:
            self.param = param
            
        self.gbC = QtGui.QGroupBox(u"Hide/Show Cone") 
        self.gbC.setCheckable(True)        
        self.gbC.setChecked(self.param.props['visible'])
        self.gbC.toggled.connect(self.updateParam)
        
        lL = []
        self.sp = []
        gbC_lay = QtGui.QGridLayout()
        for pos, name in enumerate(['length', 'radius']):
            lL.append(QtGui.QLabel(name, self.gbC))
            length = self.param.props[name]
            self.sp.append(QtGui.QDoubleSpinBox(self.gbC))
            self.sp[pos].setDecimals(2)
            self.sp[pos].setMinimum(0.0)
            self.sp[pos].setMaximum(1e6)
            self.sp[pos].setLocale(QtCore.QLocale(QtCore.QLocale.English))
            self.sp[pos].setValue(length)        
        lL.append(QtGui.QLabel('cols', self.gbC))        
        self.sp.append(QtGui.QSpinBox(self.gbC))
        self.sp[-1].setMinimum(0)
        self.sp[-1].setMaximum(100)
        self.sp[-1].setValue(self.param.props['cols'])
        #Layout
        for pos in range(len(lL)):
            gbC_lay.addWidget(lL[pos],pos,0)
            gbC_lay.addWidget(self.sp[pos],pos,1)
            # Les signaux
            self.sp[pos].valueChanged.connect(self.updateParam)        
        
        self.gbC.setLayout(gbC_lay)
        
        
        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.gbC)
        hbox.addStretch(1.0)
        
        vbox.addLayout(hbox)
        vbox.addStretch(1.0)        
        
        self.setLayout(vbox)

    def updateParam(self, option):
        """
        update param and emit a signal
        """
        self.param.props['visible'] = self.gbC.isChecked()
        for pos, name in enumerate(['length', 'radius', 'cols']):
            self.param.props[name] = self.sp[pos].value()
        # emit signal 
        self.signalObjetChanged.emit(self.param)


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(300, 300)
        self.setWindowTitle('pyqtgraph example: Cone GLMeshItem')

        self.initActions()
        self.initMenus()


        self.propsWidget = ConeWidget()
        self.propsWidget.signalObjetChanged.connect(self.updateView)

        self.glWidget = gl.GLViewWidget(self)
        cols = self.propsWidget.param.props['cols']
        l = self.propsWidget.param.props['length']
        r = self.propsWidget.param.props['radius']
        md = MyMeshData.cone(cols, length=l, radius=r)
        colors = self.getColors(md.faceCount())
        md.setFaceColors(colors)
        self.glCone = gl.GLMeshItem(meshdata=md, smooth=True, drawEdges=True, edgeColor=(1,0,0,1))
        self.glWidget.addItem(self.glCone)
        self.glWidget.setCameraPosition(distance=40)
        
        # Central Widget
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal) 

        splitter1.addWidget(self.propsWidget )
        splitter1.addWidget(self.glWidget )
               
        self.setCentralWidget(splitter1)        

    def getColors(self, nbrFaces):
        colors = np.ones((nbrFaces+1, 4), dtype=float)
        colors[:] = np.array([0.0, 1.0, 0.0, 1.0])
        
        return colors

    def initActions(self):
        self.exitAction = QtGui.QAction('Quit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.close)


    def initMenus(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.exitAction)

    def close(self):
        QtGui.qApp.quit()
        
    def updateView(self, param):
        cols = param.props['cols']
        l = param.props['length']
        r = param.props['radius']
        flag = param.props['visible']
        md = MyMeshData.cone(cols, length=l, radius=r)        
        colors = self.getColors(md.faceCount())
        md.setFaceColors(colors)        
        self.glCone.setMeshData(meshdata=md)        
        self.glCone.setVisible(flag)

        
## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
        
    app = QtGui.QApplication(sys.argv)
    
    win = MainWindow()
    win.show()
    
    sys.exit(app.exec_())