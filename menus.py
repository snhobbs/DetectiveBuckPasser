'''
menu classes
'''
import subprocess, readline, userInput, os


class BaseMenu(object):

	linePad = 50

	def __init__(self, db, title, description):
		self.db = db
		self.title = title
		self.description = description

	def borderString(self):
		columns, rows = userInput.getTerminalSize()
		return ''.center(columns,'#')

	def underLine(self, inStr = None, minLength = 12):
		if len(inStr) < minLength:
			return '='*minLength
		return len(inStr) * '='

	def makeTitle(self, title, description):
		titleString = []
		columns, rows = userInput.getTerminalSize()
		titleString.append(self.borderString())
		titleString.append('\n')
		titleString.append(title.center(columns))
		titleString.append('\n')
		titleString.append('%s'%(self.underLine(inStr=title).center(columns)))
		titleString.append('\n')
		if not self.description in [None, ""]:
			titleString.append(('    %s:'%(description)).center(columns).title())
			titleString.append('\n')
		return titleString

	def makeScreen(self):
		screen = self.makeTitle(self.title, self.description)
		screen.extend(self.makeScreenLines())
		screen.append(self.borderString() + '\n')
		return ''.join(screen)

class Menu(BaseMenu):
	'''
	Menu is the base class for all numberical selection menus
	'''

	def __init__(self, db, title, description, cursor):
		BaseMenu.__init__(self, db, title, description)
		self.cursor = cursor
		self.MenuOptions = []
		self.addOption(MenuOption(db = db, title = "Exit Menu", description="Exit Menu", commit = True, clear=True, action = self.exitMenu))

	def exitMenu(self):
		raise KeyboardInterrupt

	def runMenu(self):
		userInput.printToScreen(self.makeScreen())
		while True:
			varIn = input(self.cursor).upper().strip()

			if(varIn.isdigit() and int(varIn) <= len(self.MenuOptions)):
				try:
					if(self.MenuOptions[int(varIn) -1].clear):
						os.system('clear')
						userInput.printToScreen(self.makeScreen())
					self.MenuOptions[int(varIn) -1].run()
					if(self.MenuOptions[int(varIn) -1].commit):
						self.db.commit()
					break
				except KeyboardInterrupt:
					break
				except UserWarning as uw:
					print(uw)
					continue

	def addOption(self, option):
		self.MenuOptions.append(option)
		return option

	def numberedLine(self, text, count):
		columns, rows = userInput.getTerminalSize()
		return ("\t\t%d)  %s"%(count, text)).ljust(self.linePad, ' ').center(columns).title()

	def makeScreenLines(self):
		return ("%s"%(self.numberedLine(self.MenuOptions[i].title, i + 1)) + '\n' for i in range(len(self.MenuOptions)))

class MenuOption(object):
	def __init__(self, db = None, title = None, description = None, commit = False, clear = True, action=None):
		self.db = db
		self.title = title
		self.description = description
		self.commit = commit
		self.clear = clear
		self.action = action
		self.typeCheck()

	def typeCheck(self):

		if(not type(self.commit) == bool):
			raise UserWarning('commit must be a boolean')
		if(not type(self.clear) == bool):
			raise UserWarning('clear must be a boolean')

	def run(self):
		if self.action != None:
			self.action()

class ListMenu(BaseMenu):
	'''
	make a command controlled menu with a list
	'''
	def __init__(self, db, title, description, cursor, closeOnPrint = True, fields = 3, fieldLengths = [.3,.3,.4]):
		BaseMenu.__init__(self, db, title, description)
		self.cursor = cursor
		self.commands = {
			'exit':userInput.Command(func=self.exitMenu, takesArgs=False, descrip = 'Exit Inventory'),
			'commands':userInput.Command(func=self.printCommands, takesArgs=False, descrip = 'Print the available commands'),
			'help':userInput.Command(func=self.printCommands, takesArgs=False, descrip = 'No one can save you now')
			}
		self.listItems = []
		self.fields = fields
		self.fieldLengths = fieldLengths

	def printCommands(self):
		userInput.printToScreen("Some of the Avaliable Commands:")

		maxLen = max([len(command) for command in self.commands if not self.commands[command].hide])
		for command in self.commands:
			if not self.commands[command].hide:
				userInput.printToScreen('{0}{1} -> {2.descrip}'.format(' '*(maxLen - len(command)), command, self.commands[command]))

	def exitMenu(self):
		raise KeyboardInterrupt

	def runMenu(self):
		userInput.printToScreen(self.makeScreen())
		while True:
			varIn = input(self.cursor).lower().strip()
			try:
				arrayIn = varIn.split(' ')
				command = self.commands[arrayIn[0]]
				if command.takesArgs == True:
					command.func(arrayIn[1:])
				else:
					command.func()
			except KeyboardInterrupt:
				break
			except UserWarning as uw:
				print(uw)
				continue
			except IndexError:
				continue
			except KeyError:
				continue

	def addListItem(self, itemArray):
		if(len(itemArray) > self.fields):
			raise UserWarning('item array is longer than the number of fields of this menu ({0} vs {1})'.format(len(itemArray), self.fields))
		else:
			self.listItems.append(itemArray)
			return itemArray

	def listLine(self, listItem):
		formattedFields = []
		columns, rows = userInput.getTerminalSize()

		for field, relFieldLen in zip(listItem, self.fieldLengths):
			field = str(field)
			fieldLen = relFieldLen * columns
			if len(field) > fieldLen:
				formattedFields.append(field[:fieldLen - 3] + '...')
			else:
				formattedFields.append( field + ' '*int(fieldLen - len(field)) )
		return " | ".join(formattedFields)

	def makeScreenLines(self):
		return (self.listLine(listItem) + '\n' for listItem in self.listItems)

if __name__ =="__main__":
	menuEx = Menu(db = None, title = "Title", description = "Description", cursor = "  >")
	screen = menuEx.makeScreen()
	userInput.printToScreen(screen)
