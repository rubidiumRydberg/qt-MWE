from .menu import menu

def hello_world():
    print('h')



class fileMenu(menu):
    def __init__(self, parent):

        super().__init__(parent)

        menuDict = {'Open': hello_world,
                    'Quit': hello_world}

        self.newMenu('File', menuDict)




