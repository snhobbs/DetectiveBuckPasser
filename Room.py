from sqlTable import SQLTable
from inventory import Inventory
from objects import Objects
import csv

def getRoom(db, roomCode):
	roomBase = Room(db)
	roomBase.setCode(roomCode)
	roomBase.readFromDB()

	roomType = roomBase.roomType.value
	if roomType == 'APT':
		room = Apartment(db)

	elif(roomType == 'HOME'):
		room = HomeApt(db)

	else:
		raise UserWarning("Unknown Room Type")

	room.setCode(roomCode)
	room.readFromDB()
	return room

class Room(SQLTable):
	'''
	base for every generalized space in the game, this includes hallways, apartment blocks, etc
	'''
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.code = None
		self.neighbors = self.elementTable.addElement(title = 'Neightboring Rooms', name = 'neighbors', value = None, elementType = 'STRING')
		self.people = self.elementTable.addElement(title = 'Characters in Room', name = 'people', value = None, elementType = 'STRING')
		self.description = self.elementTable.addElement(title = 'Room Description', name = 'descrip', value = '', elementType = 'STRING')
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Room', name = 'inventoryCode', value = None, elementType = 'INT')
		self.objects = self.elementTable.addElement(title = 'Interactable Objects', name = 'objects', value = None, elementType = 'STRING')

		self.objectsList = None#array of different interactable objects
		self.inventory = Inventory(db)
		self.peopleList = None

		self.table = 'rooms'
		self.codeName = 'roomCode'

	def parseCSVNumString(self, stringIn):
		csv_reader = reader(stringIn)
		ret = []
		for row in csv_reader:
			ret += [int(entry) for entry in row]
		return ret

	def loadObjList(self, codeString, classToSet):
		if self.codeString != None:
			codes = self.parseCSVNumString(codeString)
			objList = []
			for code in codes:
				obj = classToSet(db)
				obj.setCode(code)
				objList.append(obj)
		return objList

	def loadRoom(self):
		self.objectsList = loadObjList()
		self.peopleList = loadObjList()
		self.inventory.setCode(int(self.inventoryCode.value))

class HomeApt(Room):
	'''
	This is the so called heros apartment
	'''
	def __init__(self, db):
		Room.__init__(self, db)
		self.neighbors.value = None
		self.people.value = None
		self.description.value = "Its a shit hole"
		self.inventoryCode.value = None
		self.objects.value = None

		self.inventory = Inventory(db)

class Apartment(Room):
	'''
	needs all of the rooms for an apartment, and a couch to search
	bathroom
	bedroom
	living room
	kitchen
	'''
	def __init__(self, db):
		Room.__init__(self, db)

class Hallway(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)

class ParkingLot(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)

class ChachNot(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)

class MurderScene(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)
