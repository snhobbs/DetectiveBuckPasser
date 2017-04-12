#inventory.py
from sqlTable import SQLTable
import items
class InventoryEntry(object):
	def __init__(self, db):
		items.Item.__init__(self, db)
		self.db = db
		self.amount = None
		self.item = None

	def loadEntry(self, itemName, amount):
		self.amount = amount
		self.item = items.itemFactory( self.db, itemName.lower() )

class Inventory(SQLTable):#when interfacing w/ the db need to loop through all the items and their count as its duplicated
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.table = 'inventory'
		self.codeName = 'inventoryCode'
		self.amount = self.elementTable.addElement(title = 'Item Amount', name = 'amount', value = None, elementType = 'FLOAT')
		self.itemCode = self.elementTable.addElement(title = 'Item Code', name = 'itemCode', value = None, elementType = 'INT')
		self.items = None

		self.assignCode()

	def addItem(self, itemName, amount):
		if self.items is None:
			self.items = []
		newItem = InventoryEntry(self.db)
		newItem.loadEntry(itemName, float(amount))
		self.items.append(newItem)

	def __moveItem(self, itemName, amount):
		for item in self.items:
			if item.item.subType == itemName:
				if(float(amount) > float(item.amount)):
					UserWarning("You don't have enough to do that")
				remaining = float(item.amount) - float(amount)
				if remaining < 1e-3:
					self.items.pop(self.items.index(item))
				else:
					item.amount = remaining
				return (item.item.copy(), amount)

	def placeItem(self, inventory, itemName, amount):
		'''
		moves an item from your inventory to that of another inventory
		'''
		if type(inventory) is Inventory:
			try:
				inventory.addItem(__moveItem)
			except UserWarning as uw:
				print(uw)

	def writeToDB(self):
		if(self.items != None):
			for item in self.items:
				self.amount.value = item.amount
				self.itemCode.value = item.item.code
				self.insertSql(inputs = (self.tableCode, self.amount.sqlPair, self.itemCode.sqlPair))

	def readFromDB(self):
		resp = self.selectSql(table = self.table, columnNames = self.columnNames, conditions = (self.tableCode))
		if(resp is None):
			raise UserWarning("No inventory for this code code '%s'"%(self.code))
		self.items = []
		for itemName, amount in resp:
			self.addItem(itemName, amount)
		print(self.items)

	def listItems(self):
		print('\n\t'.join(["{0.item.subType.value}\t{0.amount}\t%.3f\nDescription: {0.descrip.value}".format(item)%(float(item.item.weight.value) * float(item.amount)) for item in self.items ]))

	def inventoryMenu(self):
		pass

