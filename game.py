#!/usr/bin/python3
import Room, hero, Character, objects, inventory, userInput
import readline, traceback, sqlite3, os
from gameEvents import EventManager
from musicPlayer import MusicMenu
from menus import Menu, MenuOption
'''
To do:
1) remove simpleaudio if possible with wav
'''

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
			'help':userInput.Command(func=self.printHelp, takesArgs=False, descrip = 'No one can save you now'),
			'move':userInput.Command(func=self.move, takesArgs=True, descrip = 'Move to a neighboring room'),
			'describe':userInput.Command(func=self.describe, takesArgs=True, descrip = 'Description of a person or thing'),
			'talk':userInput.Command(func=self.talkTo, takesArgs=True, descrip = 'Really need this fucking explained you dim wit?'),
			'items':userInput.Command(func=self.listItems, takesArgs=True, descrip = 'List what you have on you'),
			'search':userInput.Command(func=self.search, takesArgs=True, descrip = 'Root around for something'),
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around'),
			'mute':userInput.Command(func=self._mute, takesArgs=False, hide = True, descrip = 'Mute the sound')
			}

		self.neighbors = None

	def _getObject(self, objName = None):
		if self.currRoom.objects == None:
			userInput.printToScreen("There's nothing in here")
			return False
		try:
			self.inspection = [obj for obj in self.currRoom.objects if obj.objName.value.lower() == objName][0]
			return True
		except IndexError:
			raise UserWarning('No Object Found')

	def _getCharacter(self, charName = None):
		if self.currRoom.characters == None:
			#print('You\'re all alone')
			return False
		try:
			self.inspection = [character for character in self.currRoom.characters if character.charName.value.lower() == charName][0]
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
		self.inspection.loadRoom(self.stage)

	def _getItem(self, itemName = None):
		if self.buckPasser.inventory == None or self.buckPasser.inventory.items ==  None or len(self.buckPasser.inventory.items) < 1:
			#print('You ain\'t got shit')
			return False
		try:
			self.inspection = [item for item in self.buckPasser.inventory.items if item.item.subType.value.lower() == itemName][0]
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
		userInput.printToScreen('\n\nNo one can help your sorry ass, just go score some blow.\n\n')
		self.printCommands()

	def describe(self, subject = None):
		if subject == None:
			subject = [input('Describe What? :  ').strip().lower()]
		self.__makeCommand(subject = subject, command = 'describe', onObject = True, onCharacter = True, onItem = True)

	def talkTo(self, charName = None):
		if self.currRoom.characters == None:
			userInput.printToScreen("No one is here")
			return

		if type(charName) in [tuple, list]:
			charName = ' '.join(charName).upper()

		elif charName == None:
			options = ['No one']
			options.extend(char.charName.value for char in self.currRoom.characters)

			selection = userInput.printSelect(options = options, cursor = 'To Whom?> ')
			if(selection == 0):
				return
			else:
				charName = options[selection]
		char = [char for char in self.currRoom.characters if char.charName.value.upper() == charName]
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
		self.currRoom.loadRoom(self.stage)
		self.currRoom.inventory.charInventory = self.buckPasser.inventory
		self.currRoom.inventory.refreshList()

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
			self.buckPasser.roomInventory = self.currRoom.inventory
			self.currRoom.inventory.charInventory = self.buckPasser.inventory
		else:
			raise UserWarning("{} is not a valid neighbor".format(room))

	def listItems(self):
		self.buckPasser.listItems()

	def search(self):
		self.currRoom.commands['search'].run()

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
		os.system('clear')
		self.currRoom.look()

class Game(GameCommands, GameMenu):
	def __init__(self, dbFile):
		import glob
		self.stage = 0
		self.dbFile = dbFile
		sqlFiles = ['sqlStructure.sql', 'items.sql', 'events.sql'] + glob.glob('stage*.sql')
		for sqlFile in sqlFiles:
			os.system("sqlite3 {0} < {1}".format(self.dbFile, sqlFile))#FIXME this is not cross platform

		os.stderr = open('log.log', 'w+')
		self.db = sqlite3.connect(self.dbFile)
		self.musicProcess = None
		GameCommands.__init__(self, self.db)
		GameMenu.__init__(self, self.db)
		self.musicMenu = MusicMenu(self.db, self.musicProcess)
		self.eventManager = EventManager(self.db)

	def _exit(self):
		self._save()
		self._mute()
		exit(0)

	def _load(self):
		print("Not Implimented")

	def _save(self):
		self.buckPasser.inventory.updateTable()
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
		self.buckPasser.inventory = inventory.HeroInventory(self.db)
		self.buckPasser.inventory.setCode(0)
		self.buckPasser.inventory.readFromDB()
		self.buckPasser.inventory.refreshList()

		self.currRoom = Room.Room(self.db)
		self.currRoom.setCode(0)
		self.setupNewRoom()

		self.buckPasser.inventory.roomInventory = self.currRoom.inventory

		self.getRoomNeighbors()
		self._save()

	def checkStage(self):
		'''
		Here the we look at the position and inventory of the character, if a stage change event has occurred, incriment the stage attribute
		'''
		stageCheck = self.eventManager.checkGameEvent(self.buckPasser.inventory, self.currRoom)
		if(stageCheck is not None):
			self.stage = stageCheck
		self._save()

	def run(self):
		try:
			self.__setupGame()
			self.currRoom.look()

			lastRoom = self.currRoom
			while True:
				try:
					if lastRoom != self.currRoom:
						lastRoom.writeRoom()#saves in nontemporary way (until save)
						lastRoom = self.currRoom
					self.checkStage()#check to see if a game event has occured, make something happen if it has
					userInput.userInput(self.commands, input('  > '))
				except:
					print(traceback.format_exc())
					exit(1)
		finally:
			self.db.close()
dataBaseFile = 'gameDB.db'

try:
	os.remove(dataBaseFile)#remove any previous file
except FileNotFoundError:
	pass

gameObj = Game(dataBaseFile)
gameObj.linepad = userInput.getTerminalSize()[0]
gameObj.run()
