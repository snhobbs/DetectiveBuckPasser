from sqlTable import SQLTable
import inventory
import objects
import Character
import csv
import userInput

roomDict = {
	'home':0,
	'b3':1,
	'murder':2
}

def roomFactory(db, roomCode):
	roomBase = Room(db)
	roomBase.setCode(roomCode)
	roomBase.readFromDB()

	roomType = roomBase.subType.value
	if roomType == 'Apartment':
		room = Apartment(db)

	elif(roomType == 'HomeApt'):
		room = HomeApt(db)

	elif(roomType == 'MurderScene'):
		room = MurderScene(db)

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
		self.characterCodeString = self.elementTable.addElement(title = 'Characters in Room', name = 'chars', value = None, elementType = 'STRING')
		self.descrip = self.elementTable.addElement(title = 'Room Description', name = 'descrip', value = '', elementType = 'STRING')
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Room', name = 'inventoryCode', value = None, elementType = 'INT')
		self.objectCodeString = self.elementTable.addElement(title = 'Interactable Objects', name = 'objects', value = None, elementType = 'STRING')
		self.subType = self.elementTable.addElement(title = 'Room Type', name = 'subType', value = None, elementType = 'STRING')

		self.objects = None#array of different interactable objects
		self.inventory = inventory.Inventory(db)
		self.characters = None

		self.commands = {
			'look':userInput.Command(func=self.look)
			}

		self.table = 'rooms'
		self.codeName = 'roomCode'

	def parseCSVNumString(self, stringIn):
		if stringIn in [None, '', 'None','NULL','Null','null']:
			return None
		csv_reader = csv.reader(stringIn)
		ret = []
		for row in csv_reader:
			ret += [int(entry) for entry in row]
		return ret

	def loadCharacterList(self, codeString):
		if codeString != None:
			codes = self.parseCSVNumString(codeString)
			if codes is None:
				return
			objList = []
			for code in codes:
				objList.append(Character.characterFactory(self.db, code))
			return objList

	def loadRoom(self):
		#self.objects = self.loadObjList(codeString = self.objectCodeString.value, classToSet = objects.Objects)
		#self.inventory.setCode(int(self.inventoryCode.value))
		self.characters = self.loadCharacterList(codeString = self.characterCodeString.value)

	def look(self):
		print(self.descrip.value)
		if self.characters != None:
			for char in self.characters:
				print('\n', char.charName.value, char.descrip.value)
		else:
			print("\nYou're all alone")
		#for obj in self.objectsList:
		#	print(char.descrip.value)

class HomeApt(Room):
	'''
	This is the so called heros apartment
	'''
	def __init__(self, db):
		Room.__init__(self, db)

		self.neighbors.value = '1,2'#apt3b
		self.characterCodeString.value = None
		self.descrip.value = "You're in your garbage apartment. Your goldfish tank festers in the corner. Just another damn day."
		self.inventoryCode.value = '0'
		self.objectCodeString.value = '0'
		self.subType.value = 'HomeApt'

		self.code = 0
		self.inventory = inventory.Inventory(db)

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
		self.subType.value = 'Apartment'

class Apartment_3B(Apartment):
	def __init__(self, db):
		Apartment.__init__(self, db)
		self.neighbors.value = '0,2'#next to the homeapt
		self.characterCodeString.value = '0'#3dollar man
		self.descrip.value = "Apartment 3B"
		self.inventoryCode.value = 1
		self.objectCodeString.value = '0'

		self.code = 1
		self.inventory = inventory.Inventory(db)

class Hallway(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)

class ParkingLot(Room):
	'''
	This is the home depot parking lot, theres the burnt out pontiac fiero
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
	bear is ffffuuuuccccckkkkkkkeeeddddd
	'''
	def __init__(self, db):
		Apartment.__init__(self, db)
		self.neighbors.value = '0,1'
		self.characterCodeString.value = '1,0'
		self.descrip.value = "Greusume murder scene"
		self.inventoryCode.value = 1
		self.objectCodeString.value = '0'

		self.code = 2
		self.inventory = inventory.Inventory(db)
