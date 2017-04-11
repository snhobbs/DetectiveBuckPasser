#objects.py
from sqlTable import SQLTable
from inventory import Inventory
import userInput, os

def objectFactory(db, code):
	charObj = Objects(db)
	charObj.setCode(code)
	charObj.readFromDB()
	subType = charObj.subType.value

	if subType in ['Couch']:
		obj = Couch(db)

	elif subType in ['Cushions']:
		obj = Cushions(db)

	elif subType in ['Feathers']:
		obj = Feathers(db)

	elif subType in ['Computer']:
		obj = Computer(db)

	else:
		raise UserWarning('Unknown Object subType {}'.format(subType))

	obj.readFromDB()
	return obj

class Objects(SQLTable):
	'''
	Objects is the base class for all interactable objects in the game
	'''
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.code = None
		self.subType = self.elementTable.addElement(title = 'Object Type', name = 'subType', value = None, elementType = 'STRING')
		self.objName = self.elementTable.addElement(title = 'Objects Name', name = 'objName', value = None, elementType = 'STRING')
		self.descrip = self.elementTable.addElement(title = 'Object Description', name = 'descrip', value = None, elementType = 'STRING')
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Object', name = 'inventoryCode', value = None, elementType = 'INT')

		self.table = 'objects'
		self.codeName = 'objCode'
		self.defaultCommands = {
			'search':userInput.Command(func=self.search, takesArgs=False, hide = False),
			'describe':userInput.Command(func=self.describe, takesArgs=False, hide = False),
			'use':userInput.Command(func=self.use, takesArgs=False, hide = False)
			}
		self.commands = self.defaultCommands

	def search(self):
		#make this a function that looks for items in
		pass

	def grab(self):
		pass

	def store(self):
		pass

	def drink(self):
		pass

	def describe(self):
		print("\n{0.objName.value}\n-------------------\n{0.descrip.value}".format(self))

	def use(self):
		print('That doesn\'t serve a purpose, just like your sorry ass.')

class Couch(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 0
		self.subType.value = 'Couch'
		self.objName.value = 'Couch'
		self.descrip.value = "Standard couch with removable cushions, just like the one you sat on when you're wife left you."
		self.inventoryCode.value = 0


class Cushions(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 1
		self.subType.value = 'Cushions'
		self.objName.value = 'Cushions'
		self.descrip.value = 'A couch cushion with zipper, its hard and lumpy like your shitty heart'
		self.inventoryCode.value = 0

class Feathers(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 2
		self.subType.value = 'Feathers'
		self.objName.value = 'Feathers'
		self.descrip.value = 'A shit ton of feathers'
		self.inventoryCode.value = 0

class Computer(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 3
		self.subType.value = 'Computer'
		self.objName.value = 'Computer'
		self.descrip.value = "A beige Dell covered in Cheeto dust. Some Dope website's on the screen"
		self.inventoryCode.value = 0

	def use(self):
		print('Who would visit this website? Why does this dirt bag have it set as his home screen? Some questions are not meant to be answered.')
		fileName = "file:///home/simon/Documents/interests/eatABattery/home.html"
		os.system("firefox {}".format(fileName))

class Phone(Objects):
	'''
	Plays voice mails, allows you to call other apartments that have a phone
	'''
	pass
