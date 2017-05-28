#inventory.py
from sqlTable import SQLTable
import items
from menus import *
class InventoryMenu(Menu):
	'''
	inventory commands:
		-> put bottle 3
		-> take bottle 3 or take 3 bottles
		-> drop 3 bottles
		-> combine bottle, rag, gasoline -> replace these with moltov
	'''
	def __init__(self, db):
		Menu.__init__(self, db, title = "Inventory", description="Item Menu", cursor = "What do you want to do? ")
		self.addOption(MenuOption(db = db, title = "List Items", description="List the items in this inventory", commit = True, clear=True, action=self.put))
		self.addOption(MenuOption(db = db, title = "Put", description="Move an item to this inventory", commit = True, clear=True, action=self.put))
		self.addOption(MenuOption(db = db, title = "Take", description="Take an item", commit = True, clear=True, action=self.take))
		self.addOption(MenuOption(db = db, title = "Drop", description="Drop an item on the floor", commit = True, clear=True, action=self.drop))
		self.addOption(MenuOption(db = db, title = "Combine", description="Combine Items", commit = True, clear=True, action=self.combine))



	def put(self):
		'''
		move an item from the users inventory to an inventory in scope
		'''
		pass

	def take(self):
		'''
		move an item from an inventory in scope to the users inventory
		'''
		pass

	def drop(self):
		'''
		move an item from the users inventory to the inventory of the current room
		'''
		pass

	def combine(self):
		'''
		takes a list of item codes and checks to see if this is an item in a sql table combinedItems
		'''
		pass

class InventoryEntry(object):
	def __init__(self, db):
		items.Item.__init__(self, db)
		self.db = db
		self.amount = None
		self.item = None

	def loadEntry(self, itemCode, amount):
		self.amount = amount
		self.item = items.Item(self.db)
		self.item.code = itemCode
		self.item.readFromDB()

class Inventory(SQLTable, InventoryMenu):#when interfacing w/ the db need to loop through all the items and their count as its duplicated
	def __init__(self, db):
		InventoryMenu.__init__(self, db)
		SQLTable.__init__(self, db)
		self.table = 'inventory'
		self.codeName = 'inventoryCode'
		self.amount = self.elementTable.addElement(title = 'Item Amount', name = 'amount', value = None, elementType = 'FLOAT')
		self.itemCode = self.elementTable.addElement(title = 'Item Code', name = 'itemCode', value = None, elementType = 'INT')
		self.items = None

		self.assignCode()

	def addItem(self, itemCode, amount):
		if self.items is None:
			self.items = []
		newItem = InventoryEntry(self.db)
		newItem.loadEntry(itemCode, float(amount))
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
		resp = self.selectSql(columnNames = self.columnNames, conditions = (self.tableCode))
		if(resp is None):
			raise UserWarning("No inventory for this code '%s'"%(self.code))
		self.items = []
		for amount, itemCode in resp:
			self.addItem(itemCode, amount)

	def listItems(self):
		inventoryMenu = ListMenu(db = self.db, title = 'Inventory', description = "", cursor = "Inventory> ", closeOnPrint = True, fields = 3, fieldLengths = [.3,.3,.4])
		inventoryMenu.addListItem(['Name', 'Amount', 'Total Weight'])
		for item in self.items:
			weight = float(item.item.weight.value) * float(item.amount)
			inventoryMenu.addListItem([item.item.itemName.value, item.amount, "%.3f"%weight])
		inventoryMenu.runMenu()

	def inventoryMenu(self):
		self.runMenu()

	def itemTransfer(self):
		self.inventoryMenu()

