'''
This code links the GUI to the functionality.

We defina aclass to inherit from the GUI generated
by PYUIC to give access to GUI elements in the simple
form self.button1 e.t.c.

We then call an instance of the functionality class
which is held readily accessible in func

'''

from .PYQTGUI import GUI
from .PythonFunctionality import functionality
from PyQt5.QtWidgets import QTableView

func = functionality.functionality()


class GUI(GUI.Ui_MainWindow):
	i = 0
	def __init__(self, window):
		
		super().__init__()
		self.setupUi(window)
		
		#This is whete you define 
		#all of your button actions.
		self.button1.clicked.connect(self.button1_action)
	
		return
		
	def button1_action(self):
		print ('Button 1 Pressed')
		print ('Current Vars:')
		print (func.get())
				
		
	
if __name__ == '__main__':

	import sys
	from PyQt5.QtWidgets import QApplication, QMainWindow

	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = GUI(window)
	

	window.show()
	sys.exit(app.exec_())