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
	obj.loadObjects()

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
		self.objectCodeString = self.elementTable.addElement(title = 'Interactable Objects', name = 'objects', value = None, elementType = 'STRING')

		self.table = 'objects'
		self.codeName = 'objCode'
		self.objects = None
		self.defaultCommands = {
			'search':userInput.Command(func=self.search, takesArgs=False, hide = False),
			'list':userInput.Command(func=self.list, takesArgs=False, hide = False),
			'inspect':userInput.Command(func=self.inspect, takesArgs=True, hide = False)
			}
		self.commands = self.defaultCommands
		self.inspection = self

	def loadObjects(self):
		self.objects = userInput.loadObjList(db = self.db, codeString = self.objectCodeString.value, factory = objectFactory)

	def list(self):
		if self.objects != None:
			for obj in self.objects:
				print('\n')
				print(obj.objName.value)
				print('__________________________')
				print(obj.descrip.value)

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
			if inspectionName in [obj.objName.value.lower().strip() for obj in self.objects]:
				self.__inspectObject(inspectionName)
				return
		except TypeError:
			pass

		print('What the hell is that mmaaannnn?')


	def search(self):
		pass

	def grab(self):
		pass

	def store(self):
		pass

	def drink(self):
		pass

class Couch(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 0
		self.subType.value = 'Couch'
		self.objName.value = 'Couch'
		self.descrip.value = "Standard couch with removable cushions, just like the one you sat on when you're wife left you."
		self.inventoryCode.value = 0
		self.objectCodeString.value = "1"


class Cushions(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 1
		self.subType.value = 'Cushions'
		self.objName.value = 'Cushions'
		self.descrip.value = 'A couch cushion with zipper, its hard and lumpy like your shitty heart'
		self.inventoryCode.value = 0
		self.objectCodeString.value = '2'

class Feathers(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 2
		self.subType.value = 'Feathers'
		self.objName.value = 'Feathers'
		self.descrip.value = 'A shit ton of feathers'
		self.inventoryCode.value = 0
		self.objectCodeString.value = None

class Computer(Objects):
	def __init__(self, db):
		Objects.__init__(self, db)
		self.code = 3
		self.subType.value = 'Computer'
		self.objName.value = 'Computer'
		self.descrip.value = "A beige Dell covered in Cheeto dust. Some Dope website's on the screen"
		self.inventoryCode.value = 0
		self.objectCodeString.value = None
		self.defaultCommands.update({
			'use':userInput.Command(func=self.website, takesArgs=False, hide = False)
		})
	def website(self):
		fileName = "file:///home/simon/Documents/interests/eatABattery/home.html"
		os.system("firefox {}".format(fileName))
