#!/usr/bin/python3
import Room, hero, Character, objects, inventory, userInput
import traceback, sqlite3
from gameEvents import EventManager
from musicPlayer import MusicMenu
from menus import Menu, MenuOption
from sqlTable import SQLTable
import startScreen
from cutScene import CutScene
global gameFiles
gameFiles = "gameFiles"
global sqlDir
sqlDir = gameFiles
global logsAndSaves
logsAndSaves = 'logsAndSaves'

def loadSQLFile(db, fileName):
	sqlLines = []
	with open(fileName, 'r') as f:
		for line in f:
			sqlLines.append(line)
	db.executescript('\n'.join(sqlLines))
	db.commit()

class GameTable(SQLTable):
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.table = 'game'
		self.codeName = 'code'
		self.stage = self.elementTable.addElement(title = 'Game Stage', name = 'stage', value = None, elementType = 'INT')

class GameCommands(object):
	'''
	self.currRoom is the room the character is in
	self.inspection is the object, item, room, character that is being looked at. Each of these needs to have a dictionary of possible commands. The games superset of commands always apply.
	'''
	def __init__(self, db):
		self.db = db
		self.currRoom = None
		self.inspection = None
		self.buckPasser = None
		self.commands = {
			'start':userInput.Command(func=self.startMenu, takesArgs=False, descrip = 'Start Menu'),
			'help':userInput.Command(func=self.printHelp, takesArgs=False, hide = True, descrip = 'No one can save you now'),
			'move':userInput.Command(func=self.move, takesArgs=True, descrip = 'Move to a neighboring room'),
			'describe':userInput.Command(func=self.describe, takesArgs=True, descrip = 'Description of a person or thing'),
			'talk':userInput.Command(func=self.talkTo, takesArgs=True, descrip = 'Really need this explained you {}?'.format(userInput.genInsult())),
			'items':userInput.Command(func=self.listItems, takesArgs=False, descrip = 'List what you have on you'),
			'search':userInput.Command(func=self.search, takesArgs=True, descrip = 'Root around for something'),
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around'),
			'mute':userInput.Command(func=self._mute, takesArgs=False, hide = True, descrip = 'Mute the sound'),
			'inspect':userInput.Command(func=self._inspect, takesArgs=True, hide = False, descrip = 'Inspect an object')
			}

		self.neighbors = None

	def _getObject(self, objName = None):
		if self.currRoom.objects == None:
			return False
		try:
			self.inspection = [obj for obj in self.currRoom.objects if obj.objName.value.lower() == objName.lower()][0]
			return True
		except IndexError:
			raise UserWarning('No Object Found')

	def _getCharacter(self, charName = None):
		if self.currRoom.characters == None:
			return False
		try:
			self.inspection = [character for character in self.currRoom.characters if character.charName.value.lower() == charName.lower()][0]
			return True
		except IndexError:
			raise UserWarning('No Character Found')

	def _getRoom(self, roomName = None):
		try:
			code = self.neighbors[roomName.title()]
		except KeyError:
			return False
		self.inspection = Room.Room(self.db)
		self.inspection.setCode(code)

	def _getItem(self, itemName = None):
		if self.buckPasser.inventory == None or self.buckPasser.inventory.items ==  None or len(self.buckPasser.inventory.items) < 1:
			#print('You ain\'t got shit')
			return False
		try:
			self.inspection = [item for item in self.buckPasser.inventory.items if item.item.subType.value.lower() == itemName.lower()][0]
			return True
		except IndexError:
			raise UserWarning('No Item Found')

	def __runCommand(self, command = None, args = None):
		try:
			if(args == None):
				func = self.inspection.__dict__['commands'][command].run()
			else:
				func = self.inspection.__dict__['commands'][command].run(args)
		except KeyError:
			pass

	def __makeCommand(self, subject = None, command = None, args = None, onObject = False, onCharacter = False, onItem = False):
		if type(subject) in [list, set, tuple]:
			subject = ' '.join(subject).lower().strip()
		try:
			#set the type of items its supposed to search for
			if onObject:
				try:
					if self._getObject(subject):
						self.__runCommand(command = command, args = args)
				except UserWarning:
					pass
			if onCharacter:
				try:
					if self._getCharacter(subject):
						self.__runCommand(command = command, args = args)
				except UserWarning:
					pass

		except UserWarning as uw:
			print(uw)
			userInput.printToScreen("I don't know what you're jabbering about you driveling idiot")

	def printCommands(self):
		userInput.printToScreen("Some of the Available Commands:")

		maxLen = max([len(command) for command in self.commands if not self.commands[command].hide])
		for command in self.commands:
			if not self.commands[command].hide:
				userInput.printToScreen('{0}{1} -> {2.descrip}'.format(' '*(maxLen - len(command)), command, self.commands[command]))

	def printHelp(self):
		userInput.printToScreen('\nNo one can help you\n')
		self.commands['talk'].descrip = 'Really need this explained you {}?'.format(userInput.genInsult())
		self.printCommands()

	def describe(self, subject = None):
		if self.currRoom.objects is None and self.currRoom.characters is None:
			userInput.printToScreen("Theres nothing here")
			return

		if subject is None:
			options = []
			if self.currRoom.objects is not None:
				options.extend(obj.objName.value for obj in self.currRoom.objects)

			if self.currRoom.characters is not None:
				options.extend(char.charName.value for char in self.currRoom.characters)

			if len(options) == 1:
				subject = options
			else:
				subject = [userInput.printSelectGetOption(options = options, cursor = 'Describe What?> ')]
				if subject[0] is None:
					return
		self.__makeCommand(subject = subject, command = 'describe', onObject = True, onCharacter = True)

	def _inspect(self, subject = None):
		if self.currRoom.objects is None:
			userInput.printToScreen("Theres nothing here")
			return

		if subject is None:
			if len(self.currRoom.objects) == 1:
				subject = self.currRoom.objects[0].objName.value
			else:
				options = [obj.objName.value for obj in self.currRoom.objects]
				subject = [userInput.printSelectGetOption(options = options, cursor = 'Inspect What?> ')]
				if subject[0] is None:
					return
		self.__makeCommand(subject = subject, command = 'inspect', onObject = True)

	def talkTo(self, charName = None):
		if self.currRoom.characters == None:
			userInput.printToScreen("No one is here")
			return
		elif len(self.currRoom.characters) == 1:
			charName = self.currRoom.characters[0].charName.value

		if type(charName) in [tuple, list]:
			charName = ' '.join(charName).upper()
		elif charName == None:
			charNames = [char.charName.value for char in self.currRoom.characters]
			charName = userInput.printSelectGetOption(options = charNames, cursor = 'To Whom?> ', exitPrompt = 'No one')
			if charName is None:
				return
		char = [char for char in self.currRoom.characters if char.charName.value.upper() == charName.upper()]
		if len(char) > 0:
			char[0].talk()

	def getRoomNeighbors(self):
		room = Room.Room(self.db)
		self.neighbors = {}
		for code in userInput.parseCSVNumString(self.currRoom.neighbors.value):
			room.setCode(code)
			room.readFromDB(self.stage)
			self.neighbors.update({room.roomName.value : int(code)})

	def setupNewRoom(self):
		'''
		Sets up self.currRoom properly
		'''
		self.currRoom.inventory.charInventory = self.buckPasser.inventory
		self.currRoom.inventory.refreshList()
		self.currRoom.loadRoom(self.stage)

	def move(self, room = None):
		'''
		change current room to an available neighbor.
		if the room code is a valid room, change the currRoom object to the corresponding room and print the room description
		'''
		from operator import itemgetter
		if room == None:
			options = ['Stay Put']
			options.extend(room[0] for room in sorted(self.neighbors.items(), key=itemgetter(1)))#print with lowest room code first
			selection = userInput.printSelect(options = options, cursor = 'To Where?> ')
			if(selection == 0):
				return
			else:
				room = options[selection]
		else:
			try:
				room = ' '.join(room).title()
			except AttributeError:
				return

		if room in self.neighbors.keys():
			self.currRoom.writeRoom()
			self._getRoom(room)

			self.currRoom = self.inspection
			self.setupNewRoom()
			self.currRoom.look()
			self.getRoomNeighbors()
			self.buckPasser.inventory.roomInventory = self.currRoom.inventory

		else:
			raise UserWarning("{} is not a valid neighbor".format(room))

	def listItems(self):
		self.buckPasser.listItems()

	def search(self, args = None):
		if args is None:
			self.currRoom.commands['search'].run()
		else:
			subject = args[0]
			self.__makeCommand(subject = subject, command = 'search', onObject = True, onCharacter = True)

	def look(self):
		self.currRoom.look()

class GameMenu(Menu):
	def __init__(self, db):
		Menu.__init__(self, db, title =  'Start Menu', description="", cursor = " Start Menu> ")
		self.addOption(MenuOption(db = db, title = "Quit Game", description="Exit Game", commit = True, clear=True, action = self._exit))
		self.addOption(MenuOption(db = db, title = "Save", description="", commit = True, clear=True, action = self._save))
		self.addOption(MenuOption(db = db, title = "Load", description="Load a previous save", commit = False, clear=True, action=self._load))
		self.addOption(MenuOption(db = db, title = "Music", description="Play some sultry tunes", commit = False, clear=True, action=self.music))

	def startMenu(self):
		self.runMenu()
		self.currRoom.look()

class StartGame(Menu):
	def __init__(self):
		Menu.__init__(self, db = None, title =  'Detective Buck Passer', description="", cursor = "Game Menu> ")
		self.addOption(MenuOption(db = None, title = "New Game", description="It's your own funeral", clear=False, commit = False, action = self._newGame))
		self.addOption(MenuOption(db = None, title = "Load", description="Load a previous save", clear=False, commit = False, action=self._loadGame))
		startScreen.printScreen()

	def _newGame(self, dbFile = None):
		import os
		if dbFile is None:
			# Get a new game name
			dbFileName = "game_{}.db".format(userInput.inputUniversal('Enter a save name> ').upper().replace(' ','_').strip())
			dbFile = os.path.join(logsAndSaves, dbFileName)

		if os.path.isfile(dbFile):
			raise UserWarning("File name {} exists".format(dbFile))

		db = sqlite3.connect(dbFile)
		# make the new db ensuring its not writing over another file of the same name
		sqlFiles = ['sqlStructure.sql', 'items.sql', 'events.sql', 'stage0.sql']
		for sqlFile in sqlFiles:
			loadSQLFile(db = db, fileName = os.path.join(sqlDir, sqlFile))
		db.commit()
		cutScene = CutScene(db)
		cutScene.setCode(0)
		cutScene.readFromDB()
		cutScene.play()
		return dbFile

	def _loadGame(self):
		import glob, os
		# Print a list of the available saves, have them choose one and load it in
		dbs = glob.glob(os.path.join(logsAndSaves, 'game_*.db'))
		if len(dbs) < 1:
			print('No Saved Games')
			return

		dbFile = userInput.printSelectGetOption(options = dbs, cursor = "Choose a saved game> ")
		if dbFile is not None:
			db = sqlite3.connect(dbFile)
			db.commit()
			return dbFile

class Game(GameCommands, GameMenu):
	def __init__(self, dbFile):
		import os
		self.stage = None
		self.musicProcess = None
		os.stderr = open(dbFile.split('.')[0] + '.log', 'w+')
		self.db = sqlite3.connect(dbFile)
		GameCommands.__init__(self, self.db)
		GameMenu.__init__(self, self.db)
		self.musicMenu = MusicMenu(self.db, self.musicProcess)
		self.eventManager = EventManager(self.db)
		self._load()
		self.cutScene = CutScene(self.db)

	def _loadStage(self):
		import os
		stageFile = os.path.join(sqlDir, 'stage{}.sql'.format(self.stage))
		if(os.path.isfile(stageFile)):
			loadSQLFile(db = self.db, fileName = stageFile)
			self.currRoom.writeRoom()
			self.currRoom.loadRoom(self.stage)
			self.setupNewRoom()
			self.getRoomNeighbors()
	def _exit(self):
		self._save()
		self._mute()
		exit(0)

	def _load(self):
		gameDB = GameTable(self.db)
		gameDB.setCode(0)
		gameDB.readFromDB()
		self.stage = int(gameDB.stage.value)
		self.eventManager.stage = self.stage
		self.eventManager.nextEvent = self.stage#forces reloading of the event
		self.__setupGame()

	def _save(self):
		self.db.commit()

	def _mute(self):
		try:
			self.musicMenu.musicProcess.terminate()
		except:
			pass

	def music(self):
		self.musicMenu.runMenu()

	def __setupGame(self):
		self.buckPasser = hero.Hero(self.db)

		self.currRoom = Room.Room(self.db)
		self.currRoom.setCode(0) # you always start in your apartment on loading
		self.setupNewRoom()

		self.buckPasser.inventory.roomInventory = self.currRoom.inventory
		self.getRoomNeighbors()

	def setStage(self, stage):
		self.stage = stage
		self._loadStage()

	def checkStage(self):
		'''
		Here the we look at the position and inventory of the character, if a stage change event has occurred, incriment the stage attribute
		'''
		stageCheck = self.eventManager.checkGameEvent(self.buckPasser.inventory, self.currRoom)
		if(stageCheck is not None):
			self.setStage(stageCheck)
			self.cutScene.setCode(self.stage)
			cutSceneCount = self.cutScene.getCountInTable(conditions = self.cutScene.tableCode)
	
			if(self.cutScene.getCountInTable(conditions = self.cutScene.tableCode) > 0):
				self.cutScene.readFromDB()
				self.cutScene.play()
				userInput.clearScreen()
				self.currRoom.look()
		self._save()
		
		
	def run(self):
		try:
			userInput.clearScreen()
			self.currRoom.look()

			lastRoom = self.currRoom
			while True:
				try:
					if lastRoom != self.currRoom:
						lastRoom.writeRoom()#saves in nontemporary way (until save)
						lastRoom = self.currRoom
					self.checkStage()#check to see if a game event has occured, make something happen if it has
					userInput.userInput(self.commands, userInput.inputUniversal('  > '))
				except:
					print(traceback.format_exc())
					exit(1)
		finally:
			self.db.close()

def run():
	import os
	start = StartGame()
	dbFile = start.runMenu()

	if dbFile is not None:
		gameObj = Game(dbFile)
		gameObj.linepad = userInput.getTerminalSize()[0]
		gameObj.run()

if __name__ == "__main__":
	start = StartGame()
	fdb = 'game.db'
	os.system("rm %s"%fdb)
	dbFile = start._newGame(fdb)
