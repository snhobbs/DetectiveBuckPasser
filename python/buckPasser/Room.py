from buckPasser.sqlTable import SQLTable, StagedSqlTable
from . import objects, Character, userInput, inventory

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
			'search':userInput.Command(func=self.inventory.runMenu, takesArgs=False, descrip = 'Search the room'),
			'look':userInput.Command(func=self.look, takesArgs=False, descrip = 'Look around the room')
			}

		self.table = 'rooms'
		self.codeName = 'roomCode'

	def look(self):
		def printStuff(self, cols):
			'''
			Format the character and object printing
			'''
			if self.characters is None:
				charLen = 0
			else:
				charLen = len(self.characters)

			if self.objects is None:
				objLen = 0
			else:
				objLen = len(self.objects)

			outArray = [[None, None] for _ in range(1+max(charLen, objLen))]
			if self.characters is None:
				outArray[0][0] = "You're all alone"
			else:
				outArray[0][0] = "People around:"
				for i, char in enumerate(self.characters):
					outArray[i+1][0] = char.charName.value

			if self.objects is not None:
				outArray[0][1] = "Things around:"
				for i, obj in enumerate(self.objects):
					outArray[i+1][1] = obj.objName.value

			width = int(cols/2)
			for line in outArray:
				if line[0] is None:
					left = ' '*width
				else:
					left = "{1}{0}".format(' '*(width - len(line[0])), line[0])
				if line[1] is None:
					right = '|'
				else:
					right = '| {}'.format(line[1])
				userInput.printToScreen("{}{}".format(left, right))

		cols, rows = userInput.getTerminalSize()
		userInput.clearScreen()
		userInput.printToScreen(self.roomName.value.center(cols), color='CYAN')
	
		userInput.printToScreen(''.center(cols, '='), color='WHITE')
		userInput.printToScreen(self.descrip.value)
		
		printStuff(self, cols)
	
	def loadRoom(self, stage):
		'''
		Load objects, inventories, and characters based off of the current game stage
		'''
		self.readFromDB(stage)
		self.inventory.setCode(self.inventoryCode.value)
		self.inventory.readFromDB()

		self.objects = userInput.loadObjList(db = self.db, codeString = self.objectCodeString.value, stage = stage, factory = objects.objectFactory)
		self.characters = userInput.loadObjList(db = self.db, codeString = self.characterCodeString.value, stage = stage, factory = Character.characterFactory)
		self.linkInventories()

	def linkInventories(self):
		try:
			for obj in self.objects:
				obj.inventory.charInventory = self.inventory.charInventory
		except TypeError:
			pass

		try:
			for char in self.characters:
				char.inventory.charInventory = self.inventory.charInventory
		except TypeError:
			pass

	def writeRoom(self):
		try:
			for obj in self.objects:
				obj.updateTable()

		except TypeError: #will fail if no objects
			pass
		try:
			for character in self.characters:
				character.updateTable()
		except TypeError as te:
			pass
		self.db.commit()
