'''
menu classes
'''
import subprocess, readline, userInput


class BaseMenu(object):
	def __init__(self, db, title, description):
		self.db = db
		self.title = title
		self.description = description

	def clearLines(self, lines):
		print("\033[F\033[K" * lines)

	def calcScreen(self):
		try:
			rows, columns = subprocess.check_output(['stty', 'size']).split()
		except:
			rows, columns = [100, self.linePad]
		return [int(rows), int(columns)]

	def borderString(self):
		rows, columns = self.calcScreen()
		return ''.center(columns,'#')

	def underLine(self, inStr = None, minLength = 12):
		if len(inStr) < minLength:
			return '='*minLength
		return len(inStr) * '='

	def makeTitle(self, title, description):
		titleString = []
		rows, columns = self.calcScreen()
		titleString.append(self.borderString())
		titleString.append('\n')
		titleString.append(title.center(columns))
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
	linePad = 50
	def __init__(self, db, title, description, cursor):
		BaseMenu.__init__(self, db, title, description)
		self.cursor = cursor
		self.MenuOptions = []
		self.addOption(MenuOption(db = db, title = "Exit Menu", description="Exit Menu", commit = True, clear=True, action = self.exitMenu))

	def exitMenu(self):
		raise KeyboardInterrupt

	def runMenu(self):
		print(self.makeScreen())
		while True:
			varIn = input(self.cursor).upper().strip()

			if(varIn.isdigit() and int(varIn) <= len(self.MenuOptions)):
				try:
					if(self.MenuOptions[int(varIn) -1].clear):
						subprocess.call(['cls','||','clear'])
						print(self.makeScreen())
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
		rows, columns = self.calcScreen()
		return ("\t\t%d)  %s"%(count, text)).ljust(self.linePad, ' ').center(columns).title()

	def makeScreenLines(self):
		return ("%s"%(self.numberedLine(self.MenuOptions[i].title, i + 1)) + '\r' for i in range(len(self.MenuOptions)))

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
		print("Some of the Avaliable Commands:")

		maxLen = max([len(command) for command in self.commands if not self.commands[command].hide])
		for command in self.commands:
			if not self.commands[command].hide:
				print('{0}{1} -> {2.descrip}'.format(' '*(maxLen - len(command)), command, self.commands[command]))
		input('Enter to continue')
		self.clearLines(3+len(self.commands))

	def exitMenu(self):
		raise KeyboardInterrupt

	def runMenu(self):
		print(self.makeScreen())
		while True:
			varIn = input(self.cursor).lower().strip()
			self.clearLines(2)
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
		rows, cols = self.calcScreen()

		for field, relFieldLen in zip(listItem, self.fieldLengths):
			field = str(field)
			fieldLen = relFieldLen * cols
			if len(field) > fieldLen:
				formattedFields.append(field[:fieldLen - 3] + '...')
			else:
				formattedFields.append( field + ' '*int(fieldLen - len(field)) )
		return " | ".join(formattedFields)

	def makeScreenLines(self):
		return (self.listLine(listItem) + '\n' for listItem in self.listItems)

if __name__ =="__main__":
	import sqlite3
	import characters, os
	dbFile = 'test.db'
	os.system('sqlite3 {0} < {1}'.format(dbFile, 'sqlStructure.sql'))
	db = sqlite3.connect(dbFile)
	bear = characters.Bear(db)
	bear.runMenu()

