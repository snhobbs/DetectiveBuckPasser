#items.py
from sqlTable import SQLTable
def itemFactory(db, subType):
	itemDict = {
		'general':Item
	}
	try:
		return itemDict[subType](db)
	except KeyError:
		raise UserWarning('Unknown item type {}'.format(subType))


class Item(SQLTable):
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.descrip = self.elementTable.addElement(title = 'Description', name = 'descrip', value = None, elementType = 'STRING')
		self.itemName = self.elementTable.addElement(title = 'Item Name', name = 'itemName', value = '', elementType = 'STRING')
		self.weight = self.elementTable.addElement(title = 'Item Weight', name = 'weight', value = 0, elementType = 'FLOAT')
		self.itemSize = self.elementTable.addElement(title = 'Item Size', name = 'itemSize', value = 0, elementType = 'FLOAT')
		self.critical = self.elementTable.addElement(title = 'Critical Item', name = 'critical', value = False, elementType = 'BOOL')
		self.subType = self.elementTable.addElement(title = 'item Subtype', name = 'subType', value = 'general', elementType = 'STRING')
		self.table = 'items'
		self.codeName = 'itemCode'

	def loadItem(self, inventoryEntry):
		item = itemFactory(self.db, inventoryEntry)
		item.readFromDB()
