#!/usr/bin/python3
import characters, Character
import Room, Rooms
import hero
import objects
import userInput
import getpass, readline, csv, traceback, sqlite3, os
import items
import inventory
from gameEvents import EventManager
from musicPlayer import MusicMenu
from menus import Menu, MenuOption
import subprocess
'''
To do:
1) Item transfers, special items, linking inventorys
2) remove simpleaudio if possible with wav
'''
class GameCommands(object):
	'''
	self.currRoom is the room the character is in
	self.inspection is the object, item, room, character that is being looked at. Each of these needs to have a dictionary of possible commands. The games superset of commands always apply.
	Have the user declare that they're done to either go up a layer of inspection or back to the room
	'''
	def __init__(self, db):
		self.db = db
		self.currRoom = None
		self.inspection = None
		self.buckPasser = None
		self.commands = {
			'start':userInput.Command(func=self.startMenu, takesArgs=False, descrip = 'Start Menu'),
			'commands':userInput.Command(func=self.printCommands, takesArgs=False, descrip = 'Print the available commands'),
			'help':userInput.Command(func=self.printHelp, takesArgs=False, descrip = 'No one can save you now'),
			'mute':userInput.Command(func=self._mute, takesArgs=False, hide = True, descrip = 'Mute the sound'),
			'move':userInput.Command(func=self.move, takesArgs=True, descrip = 'Move to a neighboring room'),
			'describe':userInput.Command(func=self.describe, takesArgs=True, descrip = 'Description of a person or thing'),
			'talk':userInput.Command(func=self.talkTo, takesArgs=True, descrip = 'Really need this fucking explained you dim wit?'),
			'items':userInput.Command(func=self.listItems, takesArgs=True, descrip = 'List what you have on you'),
			'search':userInput.Command(func=self.search, takesArgs=True, descrip = 'Root around for something'),
			'neighbors':userInput.Command(func=self.printNeighbors, takesArgs=False, descrip = 'Lists available rooms, same as exits and rooms'),
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around')
			}

	def _getObject(self, objName = None):
		if self.currRoom.objects == None:
			print("There's nothing in here")
			return
		try:
			self.inspection = [obj for obj in self.currRoom.objects if obj.objName.value.lower() == objName][0]
			return True
		except IndexError:
			raise UserWarning('No Object Found')

	def _getCharacter(self, charName = None):
		if self.currRoom.characters == None:
			#print('You\'re all alone')
			return
		try:
			self.inspection = [character for character in self.currRoom.characters if character.charName.value.lower() == charName][0]
			return True
		except IndexError:
			raise UserWarning('No Character Found')

	def _getRoom(self, roomName = None):
		roomObj = Room.Room(self.db)
		roomObj.roomName.value = roomName
		resp = roomObj.selectSql(columnNames = [roomObj.tableCode[0]], conditions=(roomObj.roomName.sqlPair))
		if resp in [None, 'NULL','']:
			raise UserWarning('No Room Found')
		self.inspection = Rooms.roomFactory(self.db, resp[0][0], self.stage)
		self.inspection.loadRoom(self.stage)

	def _getItem(self, itemName = None):
		if self.buckPasser.inventory == None or self.buckPasser.inventory.items ==  None or len(self.buckPasser.inventory.items) < 1:
			#print('You ain\'t got shit')
			return
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
					self._getObject(subject)
					self.__runCommand(command = command, args = args)
				except UserWarning:
					pass
			if onCharacter:
				try:
					self._getCharacter(subject)
					self.__runCommand(command = command, args = args)
				except UserWarning:
					pass
			if onItem:
				try:
					self._getItem(subject)
					self.__runCommand(command = command, args = args)
				except UserWarning:
					pass
		except UserWarning as uw:
			print(uw)
			print("I don't know what you're jabbering about you driveling idiot")

	def printCommands(self):
		print("Some of the Available Commands:")

		maxLen = max([len(command) for command in self.commands if not self.commands[command].hide])
		for command in self.commands:
			if not self.commands[command].hide:
				print('{0}{1} -> {2.descrip}'.format(' '*(maxLen - len(command)), command, self.commands[command]))

	def printHelp(self):
		print('\n\nNo one can help your sorry ass, just go score some blow.\n\n')
		self.printCommands()

	def describe(self, subject = None):
		if subject == None:
			subject = [input('Describe What? :  ').strip().lower()]
		self.__makeCommand(subject = subject, command = 'describe', onObject = True, onCharacter = True, onItem = True)

	def talkTo(self, charName = None):
		if self.currRoom.characters == None:
			print("No one is here")
			return
		if charName == None:
			charName = [input("Who do you want to talk to? ")]
		self.__makeCommand(subject = charName, command = 'talk', onCharacter = True)
		#self.currRoom.look()

	def search(self, subject = None):
		self.currRoom.commands['search'].run()

	def listItems(self):
		self.buckPasser.listItems()

	def printNeighbors(self):
		room = Room.Room(self.db)
		neighbors = []
		for code in userInput.parseCSVNumString(self.currRoom.neighbors.value):
			room.setCode(code)
			room.readFromDB(self.stage)
			neighbors.append(room.roomName.value)
		print("Neighboring Rooms:\n\t{}".format('\n\t'.join(neighbors)))

	def move(self, room = None):
		'''
		change current room to an available neighbor.
		if the room code is a valid room, change the currRoom object to the corresponding room and print the room description
		'''
		if room == None:
			room = [input('To Where?> ').strip().lower()]
		self.currRoom.writeRoom()
		self._getRoom(room[0])

		if str(self.inspection.code) in self.currRoom.neighbors.value.split(','):
			os.system('clear')
			self.currRoom = self.inspection
			self.currRoom.look()
			self.buckPasser.roomInventory = self.currRoom.inventory
			self.currRoom.inventory.charInventory = self.buckPasser.inventory
		else:
			raise UserWarning("{} is not a valid neighbor".format(room[0]))

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
			#subprocess.call(['sqlite3', self.dbFile, '<', sqlFile])
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

	def music(self, args = None):
		self.musicMenu.runMenu()

	def __setupGame(self):
		self.currRoom = Room.Room(self.db)
		self.currRoom.setCode(0)
		self.currRoom.readFromDB(self.stage)
		self.currRoom.loadRoom(self.stage)

		self.buckPasser = hero.Hero(self.db)
		self.buckPasser.inventory = inventory.HeroInventory(self.db)
		self.buckPasser.inventory.setCode(0)
		self.buckPasser.inventory.readFromDB()

		self.buckPasser.inventory.roomInventory = self.currRoom.inventory
		self.buckPasser.inventory.refreshList()
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

Game(dataBaseFile).run()
