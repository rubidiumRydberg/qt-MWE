from PyQt5.QtWidgets import QTableView
from .menus.exampleMenu import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt

from .appSettings import *

class UIWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class GUI(QMainWindow):
	# Snip...
	i = 0
	appTitle = 'oceanLiner'
	def __init__(self, parent, settings):
		self.assignSettings(settings)

		super().__init__()
		self.setupWindow()
		#This is whete you define 
		#all of your button actions.
		fileMenu(self)


		return

	def assignSettings(self, settings):
		prefix = '__setting__'
		for key, value in settings.items():
			attrName = prefix+key
			setattr(self, attrName, value)


	def setupWindow(self):

		windowTitle = getattr(self, '__setting__windowTitle')

		self.setWindowTitle(windowTitle)
		self.resize(400, 200)
		self.centralWidget = QLabel("Hello, World")
		self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.setCentralWidget(self.centralWidget)

	def setupUi(self):
		pass


if __name__ == '__main__':

	import sys
	from PyQt5.QtWidgets import QApplication, QMainWindow

	app = QApplication(sys.argv)
	ui = GUI(app, appSettings)


	ui.show()
	sys.exit(app.exec_())
