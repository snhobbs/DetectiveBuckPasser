#inventory.py
from sqlTable import SQLTable, StagedSqlTable
import items
from menus import *
import userInput
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
		print("Not Implimented")

	def drop(self):
		'''
		move an item from the users inventory to the inventory of the current room
		'''
		print("Not Implimented")

	def combine(self):
		'''
		takes a list of item codes and checks to see if this is an item in a sql table combinedItems
		'''
		print("Not Implimented")

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

class Inventory(SQLTable):#when interfacing w/ the db need to loop through all the items and their count as its duplicated
	'''
	Inventory is the base class for the hero, passive, and character classes
	'''
	def __init__(self, db):
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
		for inventEntry in self.items:
			if int(inventEntry.item.code) == int(itemCode):
				inventEntry.amount += float(amount)
				self.amount.value = inventEntry.amount
				self.itemCode.value = inventEntry.item.code
				self.updateTable()
				return #update amount in db and exit

		#this item doesn't exist in this inventory, add the item and write it to the database
		newEntry = InventoryEntry(self.db)
		newEntry.loadEntry(itemCode, float(amount))
		self.items.append(newEntry)
		self.amount.value = newEntry.amount
		self.itemCode.value = itemCode
		super().writeToDB()

	def _moveItem(self, itemName, amount):
		for inventEntry in self.items:
			if inventEntry.item.itemName.value == itemName:
				if(float(amount) > float(inventEntry.amount)):
					UserWarning("You don't have enough to do that")
				remaining = float(inventEntry.amount) - float(amount)
				if remaining < 1e-3:
					self.items.pop(self.items.index(inventEntry))
					self.deleteSql(inventEntry.item.itemName.sqlPair)#delete item from inventory
				else:
					inventEntry.amount = remaining
				return (inventEntry.item.code, amount)
		raise UserWarning("Item doesn't exist")

	def placeItem(self, inventory, itemName, amount):
		'''
		moves an item from this inventory to that of another inventory
		'''

		assert(isinstance(inventory, Inventory))
		try:
			itemCode, itemAmount = self._moveItem(itemName, amount)
			assert(itemAmount == amount)
			inventory.addItem(itemCode, itemAmount)
		except UserWarning as uw:
			print(uw)

	def writeToDB(self):
		if(self.items != None):
			for inventEntry in self.items:
				self.amount.value = inventEntry.amount
				self.itemCode.value = inventEntry.item.code
				super().writeToDB()
				#self.insertSql(inputs = (self.tableCode, self.amount.sqlPair, self.itemCode.sqlPair))

	def readFromDB(self):
		resp = self.selectSql(columnNames = self.columnNames, conditions = (self.tableCode))
		if(resp is None):
			raise UserWarning("No inventory for this code '%s'"%(self.code))
		print(resp)
		self.items = []
		for amount, itemCode in resp:
			self.addItem(itemCode, amount)

	def itemInInventory(self, itemName):
		itemName = itemName.lower().strip()

		for entry in self.items:
			if itemName == entry.item.itemName.value:
				return True
		return False

	def checkItemAmount(self, itemCode):
		for entry in self.items:
			if int(itemCode) == entry.item.itemCode:
				return float(entry.amount)
		raise Exception("Unknown item code {}".format(itemCode))

class CharacterInventory(Inventory):
	def __init__(self, db):
		Inventory.__init__(self, db)

class PassiveInventory(Inventory):
	'''
	Inventory for rooms and objects
	'''
	def __init__(self, db, title = None, charInventory = None):
		Inventory.__init__(self, db)

		self.menu = ListMenu(db = db, title = title, description = "Inventory", cursor = "Inventory> ", closeOnPrint = True, fields = 3, fieldLengths = [.3,.3,.4])
		self.menuCommands = {
		'put':userInput.Command(func=self.put, takesArgs=True, descrip = 'Move an item to this inventory'),
		'take':userInput.Command(func=self.take, takesArgs=True, descrip = 'Take an item')
		}
		self.menu.commands.update(self.menuCommands)

		self.charInventory = charInventory

	def parseTransaction(self, inventory, args):
		amount = None
		if(inventory.itemInInventory(args[0])):
			itemName = args[0]
			if len(args) >= 2:
				amount = args[1]

		elif(inventory.itemInInventory(args[1])):
			itemName = args[1]
			if len(args) >= 2:
				amount = args[0]

		try:
			float(amount)
		except (ValueError, TypeError):
			amount = None

		if amount is None:
			try:
				amount = float(input('Amount?> '))
			except ValueError:
				print("What?")

		return(itemName, amount)

	def put(self, args):
		'''
		Add an item to this inventory from charInventory
		'''
		try:
			itemName, amount = self.parseTransaction(self.charInventory, args)
		except UserWarning:
			print("Item doesn't exist")

		try:
			self.charInventory.placeItem(self, itemName, amount)
			self.refreshList()
		except UserWarning:
			print("Item doesn't exist or insufficient quantities for transaction")

	def take(self, args):
		'''
		move an item from this inventory to the charInventory
		'''

		itemName, amount = self.parseTransaction(self, args)
		try:
			self.placeItem(self.charInventory, itemName, amount)
			self.refreshList()
		except UserWarning:
			print("Item doesn't exist or insufficient quantities for transaction")

	def refreshList(self):
		self.menu.listItems = []
		self.menu.addListItem(['Name', 'Amount', 'Total Weight'])
		for inventEntry in self.items:
			weight = float(inventEntry.item.weight.value) * float(inventEntry.amount)
			self.menu.addListItem([inventEntry.item.itemName.value, inventEntry.amount, "%.3f"%weight])
		print(self.menu.makeScreen())

	def runMenu(self):
		self.refreshList()
		super().runMenu()

class HeroInventory(Inventory):
	def __init__(self, db):
		Inventory.__init__(self, db)

if __name__ == "__main__":
	import sqlite3, glob
	dbFile = 'gameDB.db'
	os.system('rm {}'.format(dbFile))
	sqlFiles = ['sqlStructure.sql', 'items.sql'] + glob.glob('stage*.sql')
	for sqlFile in sqlFiles:
		os.system('sqlite3 {0} < {1}'.format(dbFile, sqlFile))

	db = sqlite3.connect(dbFile)

	hi = PassiveInventory(db, title = "Hi Inventory", charInventory = None)
	hi.assignCode()
	db.commit()

	hi.addItem('0','300')
	hi.addItem('1','300')
	pi = PassiveInventory(db, title = "Pi Inventory", charInventory = hi)
	pi.assignCode()
	db.commit()
	hi.charInventory = pi
	pi.addItem('0','100')
	pi.addItem('0','100')
	pi.addItem('0','100')
	pi.addItem('0','100')
	pi.addItem('1','100')


	pi.code = '5'
	db.commit()
	pi.take(['bottle',10])
	pi.put(['bottle',100])

	hi.take(['bottle',50])
	hi.put(['bottle',5])

	db.commit()

	#pi.readFromDB()
	#pi.menu.runMenu()
	#hi.readFromDB()
	#hi.menu.runMenu()
	#db.commit()
