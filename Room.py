from sqlTable import SQLTable
import inventory
import objects
import Character
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
	room.loadRoom()
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

		self.inspection = None

		self.defaultCommands = {
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around the room'),
			'rooms':userInput.Command(func=self.printNeighbors, takesArgs=False, descrip = 'Lists available rooms, same as neighbors and exits', hide = True),
			'neighbors':userInput.Command(func=self.printNeighbors, takesArgs=False, descrip = 'Lists available rooms, same as exits and rooms'),
			'exits':userInput.Command(func=self.printNeighbors, takesArgs=False, descrip = 'Lists available rooms, same as neighbors and rooms', hide = True),
			'inspect':userInput.Command(func=self.inspect, takesArgs=True, descrip = 'Interact with an object or item'),
			'talk':userInput.Command(func=self.talkTo, takesArgs=True, descrip = 'Talk to a character')
			}

		self.commands = self.defaultCommands

		self.table = 'rooms'
		self.codeName = 'roomCode'

	def loadRoom(self):
		self.inspection = self
		self.objects = userInput.loadObjList(db = self.db, codeString = self.objectCodeString.value, factory = objects.objectFactory)
		#self.inventory.setCode(int(self.inventoryCode.value))
		self.characters = userInput.loadObjList(db = self.db, codeString = self.characterCodeString.value, factory = Character.characterFactory)

	def printNeighbors(self):
		neighbors = [roomDictKey for roomDictKey in roomDict if roomDict[roomDictKey] in userInput.parseCSVNumString(self.neighbors.value)]
		print("Neighboring Rooms: \n\t{}".format('\n\t'.join(neighbors)))

	def look(self):
		print(self.descrip.value)
		if self.characters != None:
			print("Characters: \n\t{}".format('\n\t'.join(char.charName.value for char in self.characters)))
		else:
			print("You're all alone")

		if self.objects != None:
			print("Shit in the room: \n\t{}".format('\n\t'.join(obj.objName.value for obj in self.objects)))

	def __inspectCharacter(self, characterName = None):
		if characterName == None:
			characterName = input('Who do you wanna snoop on? ').strip().lower().replace(' ','')
		try:
			self.inspection = [char for char in self.characters if char.charName.value.lower() == characterName][0]
			self.commands = self.defaultCommands
			self.commands.update(self.inspection.commands)
			return True
		except IndexError:
			print("I dont know that character %s"%characterName)
			return False

	def __inspectObject(self, objName = None):
		if objName == None:
			objName = input('Inspect what? ').strip().lower().replace(' ','')
		try:
			self.inspection = [obj for obj in self.objects if obj.objName.value.lower() == objName][0]
			self.commands = self.defaultCommands
			self.commands.update(self.inspection.commands)
			return True
		except IndexError:
			print("I dont know that object %s"%objName)
			return False

	def inspect(self, inspectionName = None):
		if inspectionName == None:
			inspectionName = [input("What do you want to inspect? ")]
		inspectionName = ' '.join(inspectionName).lower().strip()

		try:
			if inspectionName in [char.charName.value.lower().strip() for char in self.characters]:
				self.__inspectCharacter(inspectionName)
				return
		except TypeError:
			pass

		try:
			if inspectionName in [obj.objName.value.lower().strip() for obj in self.objects]:
				self.__inspectObject(inspectionName)
				return
		except TypeError:
			pass

		print('What the hell is that mmaaannnn?')

	def talkTo(self, charName = None):
		if self.characters == None:
			print("No one is here")
			return
		if charName == None:
			charName = [input("Who do you want to talk to? ")]
		charName = ' '.join(charName).lower().replace('to', '').replace('with','').strip()
		if charName in [char.charName.value.lower().strip() for char in self.characters]:
			if self.__inspectCharacter(charName):
				self.inspection.talk()
		else:
			print(charName)
			print('What the hell is that mmaaannnn?')

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
		self.objectCodeString.value = '0,3'
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
		self.neighbors.value = '0'
		self.characterCodeString.value = '0,1'
		self.descrip.value = "Greusume murder scene"
		self.inventoryCode.value = 1
		self.objectCodeString.value = '0'

		self.code = 2
		self.inventory = inventory.Inventory(db)
