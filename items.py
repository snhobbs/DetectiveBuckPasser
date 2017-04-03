#items.py
from sqlTable import SQLTable

class Item(SQLTable):
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.descrip = self.elementTable.addElement(title = 'Description', name = 'descrip', value = None, elementType = 'STRING')
		self.weight = self.elementTable.addElement(title = 'Item Weight', name = 'weight', value = 0, elementType = 'FLOAT')
		self.itemSize = self.elementTable.addElement(title = 'Item Size', name = 'itemSize', value = 0, elementType = 'FLOAT')
		self.critical = self.elementTable.addElement(title = 'Critical Item', name = 'critical', value = False, elementType = 'BOOL')

		self.table = 'items'
		self.codeName = 'itemCode'

class bottle(Item):
	def __init__(self, db):
		Item.__init__(self, db)
		self.code = 0
		self.descrip = 'An empty bottle'
		self.weight = 0.1
		self.itemSize = 1
		self.critical = False
