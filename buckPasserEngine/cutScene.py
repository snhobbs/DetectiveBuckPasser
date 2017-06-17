from sqlTable import SQLTable
import userInput

class CutScene(SQLTable):
	'''
	When a stage changes, check in the game if a cutscene with the next stage exists and display it.
	~ is a clearing pause, ^ is a none clearing pause
	'''
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.table = 'cutScene'
		self.codeName = 'stage'
		self.title = self.elementTable.addElement(title = 'Cut scene title', name = 'title', value = None, elementType = 'STRING')
		self.text = self.elementTable.addElement(title = 'Cut scene main text', name = 'text', value = None, elementType = 'STRING')
	
	def play(self):
		userInput.clearLines(1)
		userInput.clearScreen()
		columns, rows = userInput.getTerminalSize()
		userInput.printToScreen(self.title.value.center(columns), color='CYAN')
		userInput.printToScreen(''.center(columns, '='))
		textStatements = self.text.value.split('~')
		for statement in textStatements:
			lines = 0
			for pauseStatement in statement.split('^'):
				lines += userInput.printToScreen(pauseStatement)
				userInput.inputUniversal('...')
				userInput.clearLines(0)
				lines += userInput.printToScreen('')
			userInput.clearLines(lines+1) # clear the input lines
		userInput.clearLines(1)
		# print("\033[2K", end = '')
