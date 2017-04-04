import Character
import Room
import hero
import userInput
import sqlite3, os
import getpass, readline, click, csv, traceback

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
		self.inspection = None#the thing that the current command set applies to, the superset of game commands always hold
		self.gameCommands = {
			'save':userInput.Command(func=self.__save),
			'load':userInput.Command(func=self.__load),
			'exit':userInput.Command(func=self.__exit),
			'move':userInput.Command(func=self.move)
			}
		self.commands = self.gameCommands

	def __setupGame(self):
		os.system('sqlite3 {0} < {1}'.format(self.dbFile, 'sqlStructure.sql'))
		Character.SixDollarMan(self.connection).writeToDB()
		Character.Bear(self.connection).writeToDB()
		Room.HomeApt(self.connection).writeToDB()
		Room.Apartment_3B(self.connection).writeToDB()
		Room.MurderScene(self.connection).writeToDB()
		self.__save()

	def __load(self, dbFile):
		pass

	def __save(self):
		self.connection.commit()
		self.currRoom = 0

	def __exit(self):
		self.__save()
		exit(0)

	def move(self, room = None):
		'''
		change current room to an available neighbor.
		if the room code is a valid room, change the currRoom object to the corresponding room and print the room description
		'''
		if room == None:
			room = input('To Where?> ').strip().lower()
		try:
			roomCode = Room.roomDict[room]
		except KeyError:
			print('Nahh Bro, that room aint shit')
			return

		if str(roomCode) in self.currRoom.neighbors.value.split(','):
			self.currRoom = Room.roomFactory(self.connection, roomCode)
			self.inspection = self.currRoom
			self.currRoom.loadRoom()
			self.currRoom.look()
		else:
			raise UserWarning("Not a valid neighbor {}".format(roomCode))

	def run(self):
		self.connection = sqlite3.connect(self.dbFile)
		try:
			self.__setupGame()
			self.currRoom = Room.HomeApt(self.connection)
			self.inspection = self.currRoom
			self.currRoom.loadRoom()
			self.currRoom.look()
			os.system('reset')

			while True:
				try:
					investDict = self.gameCommands
					investDict.update(self.inspection.commands)
					command = userInput.userInput(investDict, input('Fuck Wit Me > '))
					if command:
						command.run()

				except:
					print(traceback.format_exc())
					exit(0)
			self.__save()
		finally:
			self.connection.close()
os.system('rm *.db')
Game().run()
