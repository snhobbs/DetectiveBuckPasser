from sqlTable import SQLTable
import objects
import Character
from characters import characterFactory
import userInput
import inventory

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
		self.roomName = self.elementTable.addElement(title = 'Room Name', name = 'roomName', value = None, elementType = 'STRING')
		self.subType = self.elementTable.addElement(title = 'Room Type', name = 'subType', value = None, elementType = 'STRING')

		self.objects = None#array of different interactable objects
		self.inventory = inventory.Inventory(db)
		self.characters = None
		self.inspection = None
		self.defaultCommands = {
			'search':userInput.Command(func=self.search, takesArgs=False, descrip = 'Search the room'),
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around the room')
			}

		self.commands = self.defaultCommands
		self.table = 'rooms'
		self.codeName = 'roomCode'

	def look(self):
		print(self.descrip.value)
		if self.characters != None:
			print("Characters: \n\t{}".format('\n\t'.join(char.charName.value for char in self.characters)))
		else:
			print("You're all alone")

		if self.objects != None:
			print("Shit in the room: \n\t{}".format('\n\t'.join(obj.objName.value for obj in self.objects)))

	def loadRoom(self):
		self.objects = userInput.loadObjList(db = self.db, codeString = self.objectCodeString.value, factory = objects.objectFactory)
		#self.inventory.setCode(int(self.inventoryCode.value))
		self.characters = userInput.loadObjList(db = self.db, codeString = self.characterCodeString.value, factory = characterFactory)

	def search(self):
		pass
