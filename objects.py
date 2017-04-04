#objects.py
from sqlTable import SQLTable
from inventory import Inventory

class Objects(SQLTable):
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.descrip = self.elementTable.addElement(title = 'Description', name = 'descrip', value = None, elementType = 'STRING')
		self.inventoryCode = self.elementTable.addElement(title = 'Items in Object', name = 'inventoryCode', value = None, elementType = 'INT')
		self.objects = self.elementTable.addElement(title = 'Interactable Objects', name = 'objects', value = None, elementType = 'STRING')

		self.objectsList = None#array of different interactable objects
		self.inventory = Inventory(db)
		self.peopleList = None

		self.table = 'items'
		self.codeName = 'itemCode'


