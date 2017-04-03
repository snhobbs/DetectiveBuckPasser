from Character import *
from Room import *
from hero import *
import sqlite3, os

class Game(object):
	def __init__(self):
		self.connection = None
		self.dbFile = 'gameDB.db'
		self.currRoom = None

	def setupGame(self):
		os.system('sqlite3 {0} < {1}'.format(self.dbFile, 'sqlStructure.sql'))
		sdm = SixDollarMan(self.connection)
		sdm.writeToDB()
		HomeApt(self.connection).writeToDB()
		HomeApt.peopleList = [sdm]
		HomeApt.inventoryCode

	def userInput(self):
		userIn = None
		return userIn

	def loadLevel(self):
		pass

	def save(self):
		self.connection.commit()
		self.currRoom =

	def move(self, roomCode):
		#change current room to an available neighboor


	def run(self):
		self.connection = sqlite3.connect(self.dbFile)
		try:
			self.setupGame()
			self.currRoom = HomeApt(self.connection)
			print(self.currRoom.description.value)
			self.save()
		finally:
			self.connection.close()

Game().run()
