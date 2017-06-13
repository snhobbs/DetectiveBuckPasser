from sqlTable import SQLTable
import userInput

class CutScene(SQLTable):
	'''
	When a stage changes, check in the game if a cutscene with the next stage exists and display it
	'''
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.table = 'cutScene'
		self.codeName = 'stage'
		self.title = self.elementTable.addElement(title = 'Cut scene title', name = 'title', value = None, elementType = 'STRING')
		self.text = self.elementTable.addElement(title = 'Cut scene main text', name = 'text', value = None, elementType = 'STRING')
	
	def play(self):
		userInput.clearScreen()
		columns, rows = userInput.getTerminalSize()
		userInput.printToScreen(self.title.value.center(columns), color='cyan')
		userInput.printToScreen(''.center(columns, '='))
		textStatements = self.text.value.split('~')
		for statement in textStatements:
			lines = userInput.printToScreen(statement)
			userInput.inputUniversal('...')
			userInput.clearLines(lines) # clear the input lines
		userInput.clearLines(1)
		print("\033[2K", end = '')

if __name__ == "__main__":
	pass
