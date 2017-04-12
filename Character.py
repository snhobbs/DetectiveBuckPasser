from sqlTable import SQLTable
import userInput
import inventory
class Character(SQLTable):
	'''
	Character is the base class for all characters in the game
	'''
	def __init__(self, db, code):
		SQLTable.__init__(self, db)
		self.code = code
		self.subType = self.elementTable.addElement(title = 'Characters Type', name = 'subType', value = None, elementType = 'STRING')
		self.charName = self.elementTable.addElement(title = 'Characters Name', name = 'charName', value = None, elementType = 'STRING')
		self.money = self.elementTable.addElement(title = 'Characters Net Worth', name = 'money', value = None, elementType = 'FLOAT')
		self.bac = self.elementTable.addElement(title = 'Blood Alcohol Content', name = 'bac', value = 0, elementType = 'FLOAT')
		self.descrip = self.elementTable.addElement(title = 'Character Description', name = 'descrip', value = None, elementType = 'STRING')

		self.table = 'chars'
		self.codeName = 'charCode'
		self.inventoryCode = None
		self.inventory = None
		self.commands = {
			'kill':userInput.Command(func=self.kill, takesArgs=False, hide = True),
			'gun':userInput.Command(func=self.kill, takesArgs=False, hide = True),
			'shoot':userInput.Command(func=self.kill, takesArgs=False, hide = True),
			'murder':userInput.Command(func=self.kill, takesArgs=False, hide = True),
			'describe':userInput.Command(func=self.describe, takesArgs=False, hide = True),
			'search':userInput.Command(func=self.search, takesArgs=False, hide = True),
			'talk':userInput.Command(func=self.talk, takesArgs=False, hide = True)
			}

	def kill(self):
		print("Don't shoot him, what the hell's wrong with you, you gaddamn maniac?")

	def grab(self):
		pass

	def store(self):
		pass

	def move(self):
		pass

	def look(self):
		pass

	def drink(self):
		pass

	def talk(self):
		print("They wont talk to the cops")

	def listItems(self):
		if self.inventory == None or len(self.inventory.items) < 0:
			print('Nothing found')
		else:
			print("Type\t\tAmount\t\tTotal Weight")
			self.inventory.listItems()

	def search(self):
		self.listItems()

	def describe(self):
		print("\n{0.objName.value}\n-------------------\n{0.descrip.value}".format(self))

	def addInventory(self, inventory):
		self.inventory = inventory
		self.inventoryCode = self.inventory.code
		self.inventory.writeToDB()
