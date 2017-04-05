import Character
import Room
import hero
import objects
import userInput
import sqlite3, os
import getpass, readline, click, csv, traceback, numpy
import toolBag
'''
To do:
1) need a variable to set for inspect that contains the levels of inspection so you can go up in the order you came in on
2) how to do items and inventories?
3) How do we wanna do the clever dialog? do each room have a string of possible exit strings to play?
4) How should conversations with the characters go?
5) Breakout objects/item inspection
'''
class Game(object):
	'''
	self.currRoom is the room the character is in
	self.inspection is the object, item, room, character, or inventory that is being looked at. Each of these needs to have a dictionary of possible commands. The games superset of commands always apply.
	Have the user declare that they're done to either go up a layer of inspection or back to the room
	'''
	def __init__(self):
		self.connection = None
		self.dbFile = 'gameDB.db'
		self.currRoom = None
		self.defaultCommands = {
			'save':userInput.Command(func=self.__save, takesArgs=False, descrip = 'save game'),
			'load':userInput.Command(func=self.__load, takesArgs=True, descrip = 'Load game from an existing save file'),
			'exit':userInput.Command(func=self.__exit, takesArgs=False, descrip = 'Exit game immediately'),
			'move':userInput.Command(func=self.move, takesArgs=True, descrip = 'Move to a neighboring room'),
			'commands':userInput.Command(func=self.printCommands, takesArgs=False, descrip = 'Print the available commands'),
			'help':userInput.Command(func=self.printHelp, takesArgs=False, descrip = 'No one can save you now', hide = False),
			'music':userInput.Command(func=self.music, takesArgs=True, descrip = 'Choose some sweet sultry tunes', hide = False)
			}
		self.commands = self.defaultCommands
		self.musicProcess = None

	def __setupGame(self):
		os.system('sqlite3 {0} < {1}'.format(self.dbFile, 'sqlStructure.sql'))
		Character.SixDollarMan(self.connection).writeToDB()
		Character.Bear(self.connection).writeToDB()

		Room.HomeApt(self.connection).writeToDB()
		Room.Apartment_3B(self.connection).writeToDB()
		Room.MurderScene(self.connection).writeToDB()

		objects.Couch(self.connection).writeToDB()
		objects.Cushions(self.connection).writeToDB()
		objects.Feathers(self.connection).writeToDB()
		self.__save()
		os.system('reset')

	def __load(self, dbFile):
		pass

	def __save(self):
		self.connection.commit()
		self.currRoom = 0

	def __exit(self):
		self.__save()
		exit(0)

	def mute(self):
		try:
			self.musicProcess.terminate()
		except:
			pass

	def music(self, args = None):
		musicDir = 'music'
		if args != None:
			if('mute' in args):
				mode = 'mute'
			elif('shuffle' in args):
				mode = 'shuffle'
			elif('single' in args or 'song' in args):
				mode = 'single'
			elif('playlist' in args):
				mode = 'playlist'
		else:
			options = (('Single Song', 'single'), ('Playlist', 'playlist'), ('Shuffle All', 'shuffle'), ('Turn Off', 'mute'))
			mode = options[toolBag.printSelect(options = [option[0] for option in options], cursor = 'music> ')][1]

		self.mute()
		if(mode != 'mute'):
			self.musicProcess = toolBag.music(musicDir, mode = mode)

	def move(self, room = None):
		'''
		change current room to an available neighbor.
		if the room code is a valid room, change the currRoom object to the corresponding room and print the room description
		'''
		if room == None:
			room = [input('To Where?> ').strip().lower()]
		try:
			roomCode = Room.roomDict[room[0]]
		except KeyError:
			print('Nahh Bro, that room aint shit')
			return

		if str(roomCode) in self.currRoom.neighbors.value.split(','):
			self.currRoom = Room.roomFactory(self.connection, roomCode)
			self.inspection = self.currRoom
			self.currRoom.look()
		else:
			raise UserWarning("Not a valid neighbor {}".format(roomCode))

	def printCommands(self):
		print("Some of the Avaliable Commands:")

		maxLen = int(max(numpy.array([len(command) for command in self.commands if not self.commands[command].hide])))
		for command in self.commands:
			if not self.commands[command].hide:
				print('{0}{1} -> {2.descrip}'.format(' '*(maxLen - len(command)), command, self.commands[command]))

	def printHelp(self):
		print('\n\nNo one can help your sorry ass, just go score some blow.\n\n')
		self.printCommands()

	def run(self):
		self.connection = sqlite3.connect(self.dbFile)
		try:
			self.__setupGame()
			self.currRoom = Room.HomeApt(self.connection)
			self.currRoom.loadRoom()
			self.currRoom.look()

			lastRoom = self.currRoom
			lastInspect = self.currRoom.inspection
			investDict = self.commands
			investDict.update(self.currRoom.commands)

			while True:
				try:
					if(self.currRoom.inspection != lastInspect):
						investDict = self.commands
						investDict.update(self.currRoom.commands)
					userInput.userInput(investDict, input('{} > '.format(self.currRoom.inspection.subType.value)))

				except:
					print(traceback.format_exc())
					exit(0)
			self.__save()
		finally:
			self.connection.close()
os.system('rm *.db')
Game().run()
