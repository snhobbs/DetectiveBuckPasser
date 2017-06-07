#inventory.py
from sqlTable import SQLTable, StagedSqlTable
import items
from menus import *
import userInput

'''
inventory commands:
	-> put bottle 3
	-> take bottle 3 or take 3 bottles
	-> drop 3 bottles
	-> combine bottle, rag, gasoline -> replace these with moltov

	Item code None is not a number
'''

class InventoryEntry(object):
	def __init__(self, db):
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
	def __init__(self, db, title = "Inventory"):
		SQLTable.__init__(self, db)
		self.table = 'inventory'
		self.codeName = 'inventoryCode'
		self.amount = self.elementTable.addElement(title = 'Item Amount', name = 'amount', value = None, elementType = 'FLOAT')
		self.itemCode = self.elementTable.addElement(title = 'Item Code', name = 'itemCode', value = None, elementType = 'INT')
		self.items = None
		self.menu = ListMenu(db = db, title = title, description = "Inventory", cursor = "Inventory> ", closeOnPrint = True, fields = 3, fieldLengths = [.3,.3,.4])
		self.menuCommands = {
			'describe':userInput.Command(func=self.describe, takesArgs=True, descrip = 'Describe an item'),
			'look':userInput.Command(func=self.refreshInventory, takesArgs=False, descrip = 'List items again')
		}

	def addAmount(self, itemCode, amount):
		'''
		If the item already is in the items, combine amounts
		'''
		if self.isEmpty():
			return

		for inventEntry in self.items:
			if int(inventEntry.item.code) == int(itemCode):
				inventEntry.amount += float(amount)
				self.amount.value = inventEntry.amount
				self.itemCode.value = inventEntry.item.code
				break#update amount in db and exit

	def addNewItem(self, itemCode, amount):
		'''
		No entry of this item exists, so add it
		'''
		newEntry = InventoryEntry(self.db)
		newEntry.loadEntry(itemCode, float(amount))
		self.items.append(newEntry)
		self.amount.value = newEntry.amount
		self.itemCode.value = itemCode

	def addItem(self, itemCode, amount):
		'''
		Loads in an inventory entry and writes change to database
		'''
		if self.items is None:
			self.items = []

		if self.itemInInventory(itemCode):
			self.addAmount(itemCode, amount)
			self.updateTable()
		else:
			#this item doesn't exist in this inventory, add the item and write it to the database
			self.addNewItem(itemCode, amount)
			self.writeToDB()

	def loadItem(self, itemCode, amount):
		'''
		Loads in an inventory entry but does not write to database
		'''
		if self.items is None:
			self.items = []

		if self.itemInInventory(itemCode):
			self.addAmount(itemCode, amount)
		else:
			#this item doesn't exist in this inventory, add the item and write it to the database
			self.addNewItem(itemCode, amount)

	def getItemEntryByName(self, itemName):
		itemName = itemName.title()
		for inventEntry in self.items:
			if inventEntry.item.itemName.value.title() == itemName:
				return inventEntry
		return None #item not in inventory

	def getItemEntry(self, itemCode):
		for inventEntry in self.items:
			if inventEntry.item.code == itemCode:
				return inventEntry
		return None #item not in inventory

	def _moveItem(self, itemName, amount):
		import math
		inventEntry = self.getItemEntryByName(itemName)
		if inventEntry is None:
			raise UserWarning("Item {} doesn't exist".format(itemName))

		if(float(amount) <= float(inventEntry.item.smallestUnit.value)):
			raise UserWarning("You can't move an amount <= the smallest unit you clot")

		if(float(amount) > float(inventEntry.amount)):
			raise UserWarning("You don't have enough to do that")

		discreteAmount = math.floor(float(amount)/float(inventEntry.item.smallestUnit.value)) # Amount in units of the smallestUnit
		adjustedAmount = discreteAmount*float(inventEntry.item.smallestUnit.value)
		remaining = float(inventEntry.amount) - adjustedAmount

		if float(remaining) < float(inventEntry.item.smallestUnit.value):
			self.items.pop(self.items.index(inventEntry))
			self.deleteSql(inventEntry.item.tableCode)#delete item from inventory
		else:
			inventEntry.amount = remaining
		return (inventEntry.item.code, adjustedAmount)

	def placeItem(self, inventory, itemName, amount):
		'''
		moves an item from this inventory to that of another inventory
		'''
		assert(isinstance(inventory, Inventory))
		try:
			itemCode, itemAmount = self._moveItem(itemName, amount)
			# itemAmount is the highest whole value of the items smallest unit that is <= amount
			inventory.addItem(itemCode, itemAmount)
		except UserWarning as uw:
			print(uw)

	def readFromDB(self):
		self.items = None
		resp = self.selectSql(columnNames = self.columnNames, conditions = (self.tableCode))
		if(resp is not None):
			# inventory is not empty
			for amount, itemCode in resp:
				self.loadItem(itemCode, amount)
		self.refreshList()

	def itemInInventory(self, itemCode):
		try:
			itemCode = int(itemCode)
		except (ValueError, TypeError):
			raise UserWarning("Item code {} is not a number".format(itemCode))

		if self.checkEntryLength() == 0:
			return False
		else:
			for entry in self.items:
				if itemCode == int(entry.item.code):
					return True
			return False

	def itemInInventoryByName(self, itemName):
		try:
			itemName = itemName.title()
		except AttributeError:#not a string
			return False

		if self.checkEntryLength() == 0:#no items
			return False
		else:
			for entry in self.items:
				if itemName == (entry.item.itemName.value).title():
					return True
			return False

	def checkEntryLength(self):
		if type(self.items) not in [list, tuple]:
			return 0
		else:
			return len(self.items)

	def checkItemAmount(self, itemCode):
		entry = self.getItemEntry(itemCode)
		if int(itemCode) == entry.item.itemCode:
			return float(entry.amount)

	def refreshList(self):
		if not self.checkEntryLength():
			return
		self.menu.listItems = []
		self.menu.addListItem(['Name', 'Amount', 'Total Weight'])
		for inventEntry in self.items:
			weight = float(inventEntry.item.weight.value) * float(inventEntry.amount)
			self.menu.addListItem([inventEntry.item.itemName.value, inventEntry.amount, "%.3f"%weight])

	def refreshInventory(self):
		self.refreshList()
		userInput.printToScreen(self.menu.makeScreen())

	def parseTransaction(self, inventory, args):
		'''
		Takes an inventory and an aray of args. Tests to see if either the first or 2nd arg is a known item, if it is the other (first or 2nd) is taken as the amount to be passed to put or take, returns the item name and amount. Otherwise raises a user warning.
		'''
		amount = None
		if(inventory.itemInInventoryByName(args[0])):
			itemName = args[0]
			if len(args) >= 2:
				amount = args[1]

		elif(inventory.itemInInventoryByName(args[1])):
			itemName = args[1]
			if len(args) >= 2:
				amount = args[0]

		else:
			userInput.printToScreen("I don't know what that means")
			raise UserWarning("Unknown arguments {}".format(args))

		try:
			float(amount)
		except (ValueError, TypeError):
			amount = None

		if amount is None:
			try:
				amount = float(userInput.inputUniversal('Amount?> '))
			except ValueError:
				userInput.printToScreen("What?")
		return(itemName, amount)

	def isEmpty(self):
		'''
		Test if inventory is empty
		'''
		try:
			self.items[0]
			return False
		except:
			return True

	def describe(self, itemsName = None):
		if self.isEmpty():
			return

		if itemsName in [None, [], '']:
			options = ['Nothing']
			options.extend(entry.item.itemName.value for entry in self.items)
			selection = userInput.printSelect(options = options, cursor = 'Describe What?> ')
			if(selection == 0):
				return
			else:
				itemsName = [options[selection]]
		userInput.printToScreen(self.getItemEntryByName(itemsName[0].title()).item.descrip.value)

class CharacterInventory(Inventory):
	def __init__(self, db):
		Inventory.__init__(self, db)

class PassiveInventory(Inventory):
	'''
	Inventory for rooms and objects
	'''
	def __init__(self, db, title = None, charInventory = None):
		Inventory.__init__(self, db)

		self.menuCommands.update({
		'put':userInput.Command(func=self.put, takesArgs=True, descrip = 'Move an item to this inventory'),
		'take':userInput.Command(func=self.take, takesArgs=True, descrip = 'Take an item')
		})
		self.menu.commands.update(self.menuCommands)

		self.charInventory = charInventory

	def put(self, args):
		'''
		Add an item to this inventory from charInventory
		'''
		try:
			itemName, amount = self.parseTransaction(inventory = self.charInventory, args = args)
		except UserWarning:
			userInput.printToScreen("Item doesn't exist")
			return

		try:
			self.charInventory.placeItem(inventory = self, itemName = itemName, amount = amount)
			self.refreshList()
			self.charInventory.refreshList()
		except UserWarning:
			userInput.printToScreen("Item doesn't exist or insufficient quantities for transaction")

	def take(self, args):
		'''
		move an item from this inventory to the charInventory
		'''

		itemName, amount = self.parseTransaction(inventory = self, args = args)
		try:
			self.placeItem(inventory = self.charInventory, itemName = itemName, amount = amount)
			self.refreshList()
			self.charInventory.refreshList()
		except UserWarning:
			userInput.printToScreen("Item doesn't exist or insufficient quantities for transaction")

	def runMenu(self):
		self.refreshList()
		self.menu.runMenu()

class HeroInventory(Inventory):
	'''
	The players inventory, allows dropping items to the current room, and combining items
	'''
	def __init__(self, db, roomInventory = None):
		Inventory.__init__(self, db = db)

		self.menuCommands.update({
		'drop':userInput.Command(func=self.drop, takesArgs=True, descrip = 'Drop an item on the floor')
		})
		self.menu.commands.update(self.menuCommands)

		self.roomInventory = roomInventory

	def drop(self, args):
		try:
			itemName, amount = self.parseTransaction(inventory = self, args = args)
		except UserWarning:
			userInput.printToScreen("Item doesn't exist")
			return
		try:
			self.placeItem(inventory = self.roomInventory, itemName = itemName, amount = amount)
			self.refreshList()
			self.roomInventory.refreshList()
		except UserWarning:
			userInput.printToScreen("Item doesn't exist or insufficient quantities for transaction")
