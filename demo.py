import sys
from PySide import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
mainwindow = QtGui.QWidget()
mainwindow.resize(550,400)
mainwindow.setWindowTitle('devname')
mainwindow.show()
app.exec_()
