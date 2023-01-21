from PyQt5.QtWidgets import QMenu, QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenuBar
class menu(QMenuBar):

    def __init__(self, parent):
        #Set up a Q Menu menuBar
        #First init self
        super().__init__(parent)

        #Assign myself to the parent as
        #the active menu bar
        parent.setMenuBar(self)

        #Then create a dict to store all
        #of the menus assigned to me. :)
        self.menus = {}

    def newMenu(self, name, menuDict = None):
        #We are making a new menu...
        #Not a menu bar, a single menu (e.g. "file").

        #Create a new menu object
        newMenu = QMenu("&File", self)

        #Add this menu to myself (I'm a menu bar)
        self.addMenu(newMenu)

        #Now store this menu for later access
        #by name
        self.menus[name] = newMenu

        #If I have been given a dictionary of items
        #to display on this menu, then add each one
        #in turn (see the addDictTo function)
        if menuDict is not None:
            self.addDictTo(name, menuDict)



    def addDictTo(self, menu, menuDict):
        #Add many actions to a menu bar at once

        #Loop through the dict (keys, items), where
        #the keys are the action name and the items
        #are the function to call when clicked
        for key, item in  menuDict.items():

            #use the 'addcommand' function to
            #add this action to the current menu.
            self.addCommand(menu, key, item)

    def addCommand(self, menu, name, command):
        #This function retrieves a menu by name
        #and then adds a single command to it

        #First get the menu by name
        menu = self.menus[menu]

        #Then create a new 'QAction', which can represent
        #a menu bar item
        action = QAction(name, self)

        #Now add this action to the current menu
        menu.addAction(action)
