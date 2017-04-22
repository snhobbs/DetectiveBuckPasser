'''
menu classes
'''
import subprocess, readline, os, textwrap
global linePad
linePad = 50
class Menu(object):
	'''
	Menu is the base class for all menus
	'''
	def __init__(self, db, title, description, cursor):
		self.db = db
		self.cursor = cursor
		self.title = title
		self.description = description
		self.MenuOptions = []
		self.addOption(MenuOption(db = db, title = "Leave", description="Exit Menu", commit = True, clear=True, action = self.exitMenu))

	def exitMenu(self):
		raise UserWarning

	def runMenu(self):
		print(self.makeScreen())
		while True:
			userInput = input(self.cursor).upper().strip()

			if(userInput.isdigit() and int(userInput) <= len(self.MenuOptions)):
				try:
					if(self.MenuOptions[int(userInput) -1].clear):
						os.system('clear')
						print(self.makeScreen())
					self.MenuOptions[int(userInput) -1].run()
					if(self.MenuOptions[int(userInput) -1].commit):
						self.db.commit()
				except KeyboardInterrupt:
					continue
				except UserWarning as uw:
					print(uw)
					continue

	def addOption(self, option):
		self.MenuOptions.append(option)
		return option

	def calcScreen(self):
		try:
			rows, columns = subprocess.check_output(['stty', 'size']).split()
		except:
			rows, columns = [100, linePad]
		return [int(rows), int(columns)]

	def numberedLine(self, text, count):
		rows, columns = self.calcScreen()
		return ("\t\t%d)  %s"%(count, text)).ljust(linePad, ' ').center(columns).title()

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
		titleString.append('\n\n')
		titleString.append(title.center(columns))
		titleString.append('\n')
		titleString.append('%s'%(self.underLine(inStr=title).center(columns)))
		titleString.append('\n\n')
		titleString.append(('    %s:'%(description)).center(columns).title())
		titleString.append('\n\n')
		return titleString

	def makeScreen(self):
		screen = self.makeTitle(self.title, self.description)
		screen.extend("%s"%(self.numberedLine(self.MenuOptions[i].title, i + 1)) + '\n' for i in range(len(self.MenuOptions)))
		screen.append('\n\n')
		screen.append(self.borderString())
		screen.append('\n\n')
		return ''.join(screen)

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

import sqlite3
import characters
if __name__ =="__main__":
	dbFile = 'test.db'
	os.system('sqlite3 {0} < {1}'.format(dbFile, 'sqlStructure.sql'))
	db = sqlite3.connect(dbFile)
	bear = characters.Bear(db)
	bear.runMenu()

