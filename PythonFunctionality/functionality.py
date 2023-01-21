'''Functionality Class

This file defines an arbitrary class with some unctionality
The point here is to ensure that the functionality runs
on it's own and completely in separate to the GUI.
That way you can concentrate on getting the functionality 
working and worry about the GUI later on.
'''


class functionality:

	vars = []

	def __init__(self):
		return
		
	def addVar(self, var):
		self.vars.append(var)
		return
		
	def reset(self):
		self.vars = []
		return
		
	def get(self):
		return self.vars
		
if __name__ == '__main__':
	
	varClass = functionality()
	
	switch = 'y'
	
	while switch == 'y':
	
		var = input('Please Add a Var')
		
		print (var)
		
		varClass.addVar(var)
		
		switch = input('Press y then <enter> to add another varible\
or press enter to continue')

	print('You Entered:')
	print(varClass.get())			
	print('Resetting Vars')
	print('--')
	varClass.reset()
	print('--')
	print('Variables Reset') 
	print('Current Vars:')
	print (varClass.vars)
	
	print ('\n\nExiting.')