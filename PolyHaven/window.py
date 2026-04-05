try:
    from PySide6.QtWidgets import QMainWindow, QPushButton, QProgressBar, QLineEdit, QFileDialog, QMenuBar, QMenu, QMessageBox
    from PySide6.QtCore import QThread, Signal
    from PySide6 import QtWidgets, QtCore, QtGui
    from shiboken6 import wrapInstance
except ImportError:
    from PySide2.QtWidgets import QMainWindow, QPushButton, QProgressBar, QLineEdit, QFileDialog, QMenuBar, QMenu, QMessageBox
    from PySide2.QtCore import QThread, Signal
    from PySide2 import QtWidgets, QtCore, QtGui
    from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

# Main windows pointer
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

# Create plugin main windows class
class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=maya_main_window()):
        super(Window, self).__init__(parent)
        self.setWindowTitle('Poly Haven Asset Manager')
