'''
This code links the GUI to the functionality.

We defina aclass to inherit from the GUI generated
by PYUIC to give access to GUI elements in the simple
form self.button1 e.t.c.

We then call an instance of the functionality class
which is held readily accessible in func

'''

from .PythonFunctionality import functionality
from PyQt5.QtWidgets import QTableView
from .menus.exampleMenu import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt
func = functionality.functionality()

from .appSettings import *

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
