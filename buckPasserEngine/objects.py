#objects.py
from sqlTable import SQLTable, StagedSqlTable
from inventory import Inventory
import userInput, os
from menus import ObjectMenu

def objectFactory(db, code, stage):
	obj = Objects(db)
	obj.setCode(code)
	obj.readFromDB(stage)
	obj.menu.title = obj.objName.value.title()
	obj.menu.description = obj.shortDescrip.value
	obj.menu.longDescrip = obj.descrip.value
	obj.menu.cursor = "{} > ".format(obj.objName.value)
	obj.inventory = Inventory(db)
	obj.inventory.setCode(obj.inventoryCode.value)

	obj.menu.commands.update({obj.useAlias.value.lower(): userInput.Command(func=obj.use, descrip = obj.useDescrip.value, takesArgs=False)})

	return obj

class Objects(StagedSqlTable):
	'''
	Objects is the base class for all interactable objects in the game. Each object should have its own commands so you can say flush toilet or logon for the computer, read for the magazine etc. You enter into an object list menu by typing inspect.
	'''

	def __init__(self, db, title = "Object"):
		StagedSqlTable.__init__(self, db)
		self.code = None
		self.stage = self.elementTable.addElement(title = 'Game Stage', name = 'stage', value = None, elementType = 'INT')
		self.objName = self.elementTable.addElement(title = 'Objects Name', name = 'objName', value = None, elementType = 'STRING', updatable = False)
		self.descrip = self.elementTable.addElement(title = 'Object Description', name = 'descrip', value = None, elementType = 'STRING', updatable = False)
		self.shortDescrip = self.elementTable.addElement(title = 'Short Description', name = 'shortDescrip', value = None, elementType = 'STRING', updatable = False)
		self.useAlias = self.elementTable.addElement(title = 'Object alias for the use method', name = 'useAlias', value = None, elementType = 'STRING')
		self.useDescrip = self.elementTable.addElement(title = 'Object use method description', name = 'useDescrip', value = None, elementType = 'STRING')
		self.usePrint = self.elementTable.addElement(title = 'What to print on use', name = 'usePrint', value = None, elementType = 'STRING')
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Object', name = 'inventoryCode', value = None, elementType = 'INT')
		self.inventory = None

		self.table = 'objects'
		self.codeName = 'objCode'
		self.menu = ObjectMenu(db = db)
		self.commands = {
			'inspect': userInput.Command(func=self.inspect, takesArgs=False, hide = False),
			'describe':userInput.Command(func=self.describe, takesArgs=False, hide = True)
		}

		self.menuCommands = {
			'search':userInput.Command(func=self.search, descrip = "Search for items",takesArgs=False, hide = False),
			'describe':userInput.Command(func=self.describe, takesArgs=False, hide = True),
			'use':userInput.Command(func=self.use, takesArgs=False, hide = True)
			}
		self.menu.commands.update(self.menuCommands)

	def inspect(self):
		self.menu.runMenu()

	def search(self):
		self.listItems()

	def describe(self):
		userInput.printToScreen("\n{0.objName.value}\n-------------------\n{0.descrip.value}".format(self))

	def use(self):
		if self.usePrint.value in ['', 'NULL','None', None]:
			userInput.printToScreen('That doesn\'t serve a purpose, just like your sorry ass.')
		else:
			userInput.printToScreen(self.usePrint.value)
			#userInput.printToScreen('Who would visit this website? Why does this dirt bag have it set as his home screen? Some questions are not meant to be answered.')

