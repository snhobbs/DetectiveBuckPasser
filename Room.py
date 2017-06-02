from sqlTable import SQLTable, StagedSqlTable
import objects
import Character
import userInput
import inventory

class Room(StagedSqlTable):
	'''
	base for every generalized space in the game, this includes hallways, apartment blocks, etc
	'''
	def __init__(self, db):
		StagedSqlTable.__init__(self, db)
		self.code = None
		self.stage = self.elementTable.addElement(title = 'Game Stage', name = 'stage', value = 0, elementType = 'INT')
		self.neighbors = self.elementTable.addElement(title = 'Neightboring Rooms', name = 'neighbors', value = None, elementType = 'STRING')
		self.characterCodeString = self.elementTable.addElement(title = 'Characters in Room', name = 'chars', value = None, elementType = 'STRING')
		self.descrip = self.elementTable.addElement(title = 'Room Description', name = 'descrip', value = '', elementType = 'STRING')
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Room', name = 'inventoryCode', value = None, elementType = 'INT')
		self.objectCodeString = self.elementTable.addElement(title = 'Interactable Objects', name = 'objects', value = None, elementType = 'STRING')
		self.roomName = self.elementTable.addElement(title = 'Room Name', name = 'roomName', value = None, elementType = 'STRING')

		self.objects = None#array of different interactable objects
		self.inventory = inventory.PassiveInventory(db, title = "Room Items", charInventory = None)
		self.characters = None
		self.inspection = None
		self.commands = {
			'search':userInput.Command(func=self.search, takesArgs=False, descrip = 'Search the room'),
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around the room')
			}

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

	def loadRoom(self, stage):
		'''
		Load objects, inventories, and characters based off of the current game stage
		'''
		self.readFromDB(stage)
		self.objects = userInput.loadObjList(db = self.db, codeString = self.objectCodeString.value, stage = stage, factory = objects.objectFactory)
		#self.inventory.setCode(int(self.inventoryCode.value))
		self.characters = userInput.loadObjList(db = self.db, codeString = self.characterCodeString.value, stage = stage, factory = Character.characterFactory)

	def search(self):
		'''
		brings up the rooms inventory
		'''
		self.inventory.menu.runMenu()

	def getRoomByName(self, roomName):
		self.roomName.value = roomName.title()#change to title case
		resp = self.selectSql(columnNames = [self.tableCode[0]], conditions=(self.roomName.sqlPair))
		if resp in [None, 'NULL','']:
			raise UserWarning('No Room Found')

		self.setCode(resp[0][0])
		self.loadRoom(self.stage)

	def writeRoom(self):
		try:
			self.inventory.updateTable()
		except TypeError:
			pass

		try:
			for obj in self.objects:
				obj.updateTable()
				obj.inventory.updateTable()
		except TypeError: #will fail if no objects
			pass
		try:
			for character in self.characters:
				character.updateTable()
				character.inventory.updateTable()
		except TypeError as te:
			pass
		self.db.commit()
