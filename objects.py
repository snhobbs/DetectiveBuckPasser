#objects.py
from sqlTable import SQLTable, StagedSqlTable
from inventory import Inventory
import userInput, os

def objectFactory(db, code, stage):
	baseObj = Objects(db)
	baseObj.setCode(code)
	baseObj.readFromDB(stage)
	subType = baseObj.subType.value

	if subType in ['couch']:
		obj = Couch(db)

	elif subType in ['computer']:
		obj = Computer(db)

	else:
		raise UserWarning('Unknown Object subType {}'.format(subType))
	obj.setCode(code)
	obj.readFromDB(stage)
	return obj

class Objects(StagedSqlTable):
	'''
	Objects is the base class for all interactable objects in the game
	'''
	def __init__(self, db):
		StagedSqlTable.__init__(self, db)
		self.code = None
		self.stage = self.elementTable.addElement(title = 'Game Stage', name = 'stage', value = None, elementType = 'INT')
		self.subType = self.elementTable.addElement(title = 'Object Type', name = 'subType', value = None, elementType = 'STRING', updatable = False)
		self.objName = self.elementTable.addElement(title = 'Objects Name', name = 'objName', value = None, elementType = 'STRING', updatable = False)
		self.descrip = self.elementTable.addElement(title = 'Object Description', name = 'descrip', value = None, elementType = 'STRING', updatable = False)
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Object', name = 'inventoryCode', value = None, elementType = 'INT')
		self.inventory = Inventory(self.db)
		self. inventoryCode.value = self.inventory.tableCode[1]

		self.table = 'objects'
		self.codeName = 'objCode'
		self.commands = {
			'search':userInput.Command(func=self.search, takesArgs=False, hide = False),
			'describe':userInput.Command(func=self.describe, takesArgs=False, hide = False),
			'use':userInput.Command(func=self.use, takesArgs=False, hide = False)
			}

	def search(self):
		self.listItems()

	def describe(self):
		print("\n{0.objName.value}\n-------------------\n{0.descrip.value}".format(self))

	def use(self):
		print('That doesn\'t serve a purpose, just like your sorry ass.')

class Couch(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.subType.value = 'COUCH'

class Computer(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.subType.value = 'COMPUTER'

	def use(self):
		print('Who would visit this website? Why does this dirt bag have it set as his home screen? Some questions are not meant to be answered.')
		fileName = "file:///home/simon/Documents/interests/eatABattery/home.html"
		os.system("firefox {}".format(fileName))

class Phone(Objects):
	'''
	Plays voice mails, allows you to call other apartments that have a phone
	'''
	pass
