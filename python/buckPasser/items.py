#items.py
from buckPasser.sqlTable import SQLTable

class Item(SQLTable):
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.descrip = self.elementTable.addElement(title = 'Description', name = 'descrip', value = None, elementType = 'STRING')
		self.itemName = self.elementTable.addElement(title = 'Item Name', name = 'itemName', value = '', elementType = 'STRING')
		self.weight = self.elementTable.addElement(title = 'Item Weight', name = 'weight', value = 0, elementType = 'FLOAT')
		self.smallestUnit = self.elementTable.addElement(title = 'Smallest Unit of the item', name = 'smallestUnit', value = 0, elementType = 'FLOAT')

		self.table = 'items'
		self.codeName = 'itemCode'
