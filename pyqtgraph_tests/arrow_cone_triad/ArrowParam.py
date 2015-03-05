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

import sys 

from MyMeshData import MyMeshData


class ArrowParam(object):
    """
    Arrow's parameter test    
    """               
    def __init__(self):
        self.props = {}
        self.props['visible'] = True
        self.props['length'] = 1.0
        self.props['radius'] = 0.1
        self.props['cols'] = 10 
        self.props['rows'] = 5
        self.props['fLC'] = 0.3
        self.props['fRC'] = 2.0
    

class ArrowWidget(QtGui.QWidget):
    """    
    Widget for editing cone's parameters
    """
    
    signalObjetChanged = QtCore.pyqtSignal(ArrowParam, name='arrowChanged')    
        
    def __init__(self, parent=None, param=None):
        super(ArrowWidget, self).__init__(parent)
    
        if param == None:
            self.param = ArrowParam()
        else:
            self.param = param
            
        self.gbC = QtGui.QGroupBox(u"Hide/Show Arrow") 
        self.gbC.setCheckable(True)        
        self.gbC.setChecked(self.param.props['visible'])
        self.gbC.toggled.connect(self.updateParam)
        
        lL = []
        self.sp = []
        gbC_lay = QtGui.QGridLayout()
        for pos, name in enumerate(['length', 'radius', 'fLC', 'fRC']):
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
        lL.append(QtGui.QLabel('rows', self.gbC))        
        self.sp.append(QtGui.QSpinBox(self.gbC))
        self.sp[-1].setMinimum(0)
        self.sp[-1].setMaximum(100)
        self.sp[-1].setValue(self.param.props['rows'])
        
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
        for pos, name in enumerate(['length', 'radius', 'fLC', 'fRC', 'cols', 'rows']):
            self.param.props[name] = self.sp[pos].value()
        # emit signal 
        self.signalObjetChanged.emit(self.param)        
        

class ArrowMainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(300, 300)
        self.setWindowTitle('pyqtgraph example: Cone GLMeshItem')

        self.initActions()
        self.initMenus()


        self.propsWidget = ArrowWidget()
        self.propsWidget.signalObjetChanged.connect(self.updateView)

        self.glWidget = gl.GLViewWidget(self)
        cols = self.propsWidget.param.props['cols']
        rows = self.propsWidget.param.props['rows']
        l = self.propsWidget.param.props['length']
        r = self.propsWidget.param.props['radius']
        fRC = self.propsWidget.param.props['fRC']
        fLC =  self.propsWidget.param.props['fLC']
        md = MyMeshData.arrow(rows, cols, radius=r, length=l, fLC=fLC, fRC=fRC)
        colors = self.getColors(md.faceCount())
        md.setFaceColors(colors)
        self.glArrow = gl.GLMeshItem(meshdata=md, drawEdges=True, edgeColor=(1,0,0,1))
        self.glWidget.addItem(self.glArrow)
        self.glWidget.setCameraPosition(distance=5)
        
        # Central Widget
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal) 

        splitter1.addWidget(self.propsWidget )
        splitter1.addWidget(self.glWidget )
               
        self.setCentralWidget(splitter1)        

    def getColors(self, nbrFaces):
        cols = self.propsWidget.param.props['cols']
        colors = np.ones((nbrFaces, 4), dtype=float)
        colors[:] = np.array([0.0, 1.0, 0.0, 1.0])
        colors[0:cols+1] = np.array([0.0, 0.0, 1.0, 1.0])
        
        
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
        rows = param.props['rows']
        l = param.props['length']
        r = param.props['radius']
        fRC = param.props['fRC']
        fLC =  param.props['fLC']        
        flag = param.props['visible']
        md = MyMeshData.arrow(rows, cols, length=l, radius=r, fRC=fRC, fLC=fLC)        
        colors = self.getColors(md.faceCount())
        md.setFaceColors(colors)       
        self.glArrow.setMeshData(meshdata=md)
        self.glArrow.setVisible(flag)    
    

        
## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
        
    app = QtGui.QApplication(sys.argv)

    win = ArrowMainWindow()
    win.show()
    
    sys.exit(app.exec_())