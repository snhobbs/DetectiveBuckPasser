#testInventory.py

import sqlite3, glob
from inventory import *
import copy
class TestSuite(object):
	dbFile = 'gameDB.db'
	def __init__(self):
		os.system('rm {}'.format(self.dbFile))
		os.system('touch {}'.format(self.dbFile))
		os.system("chmod +w {}".format(self.dbFile))
		sqlFiles = ['sqlStructure.sql', 'items.sql'] + glob.glob('stage*.sql')
		for sqlFile in sqlFiles:
			os.system('sqlite3 {0} < {1}'.format(self.dbFile, sqlFile))

		os.system("chmod +w {}".format(self.dbFile))
		self.db = sqlite3.connect(self.dbFile)

	def printContents(self, inventory):
		for itemEntry in inventory.items:
			print("{0.item.itemName.value} {0.amount}".format(itemEntry))

class InventoryTest(TestSuite):
	'''
	Test the Inventory Transactions
	'''
	def __init__(self):
		TestSuite.__init__(self)

	def valCheck(self, inventoryI, inventoryII):
		'''
		Checks to see if the contents of the two inventories are different
		'''
		if inventoryI is inventoryII:
			raise Exception("Inventories are identical")
		print("Inventory Check\n")
		for itemEntryI, itemEntryII in zip(inventoryI.items, inventoryII.items):
			print("{0.item.itemName.value} {0.amount}\t{1.item.itemName.value} {1.amount}".format(itemEntryI, itemEntryII))

		assert(len(inventoryI.items) == len(inventoryII.items))
		for itemEntryI, itemEntryII in zip(inventoryI.items, inventoryII.items):
			print("{0.item.itemName.value} {0.amount}\t{1.item.itemName.value} {1.amount}".format(itemEntryI, itemEntryII))
			assert(float(itemEntryI.amount) == float(itemEntryII.amount))
			assert(itemEntryI.item.itemName.value.lower() == itemEntryII.item.itemName.value.lower())
			assert(int(itemEntryI.item.code) == int(itemEntryII.item.code))

	def test_readFromDB(self):
		testI = Inventory(self.db)
		testI.addItem('0','300')
		testI.addItem('1','300')
		#self.db.commit()

		testICopy = copy.deepcopy(testI)
		self.valCheck(testI, testICopy)

		#readFromDB just pulls in the database inventory overwriting the current state with the saved state
		testI.readFromDB()
		testI.readFromDB()
		testI.readFromDB()

		self.valCheck(testI, testICopy)

		del testI
		del testICopy

	def test_MoveItem(self):
		def testMove(itemCode, itemName, amount, testI):
			(code, amountOut) = testI._moveItem(itemName, amount)
			assert(amount == amountOut)
			assert(itemCode == code)

		print("\n\nMove Test\n\n")
		#_moveItem(self, itemName, amount)
		testI = Inventory(self.db)
		testI.addItem('0','300')
		testI.addItem('1','300')

		#####################################
		#move all bottles
		testMove('0', 'bottle', 300, testI)

		ret = testI.getItemEntry('0')
		assert(ret is None)

		#####################################
		#readd bottles, move more than you have, will riase userwarning
		testI.addItem('0','300')
		try:
			testMove('0', 'bottle', 400, testI)
			assert(0)#Moved more of an item than it had
		except UserWarning:
			testMove('0', 'bottle', 300, testI)

		#####################################
		#move in more bottles
		print("Just Burboun: ")
		self.printContents(testI)

		testI.addItem('0','300')
		print("\nBottles and Burboun: ")
		self.printContents(testI)
		testMove('1', 'Old Crow Burboun', 300, testI)

		print("\nJust Bottles: ")
		self.printContents(testI)

		#####################################
		#Move negative amounts
		print("\nMove Negative Amounts")
		try:
			testMove('0', 'bottle', -300, testI)
			assert(0)
		except UserWarning as uw:
			print(uw)
		self.printContents(testI)
		del testI

	def test_placeItem(self):
		testI = Inventory(self.db)
		testII = Inventory(self.db)

		print("\n\nPlace Item Test\n\n")

		testI.addItem('0','300')
		testI.addItem('1','300')

		testI.placeItem(testII, 'bottle', '300')

		#Move a nonexistant item
		testI.placeItem(testII, 'bottle', '300')

		#Move more of an item than you have
		testI.placeItem(testII, 'Old Crow Burboun', '400')

		print("\nContents 1")
		self.printContents(testI)

		print("\nContents 2")
		self.printContents(testII)

		del testI
		del testII

	def test_parseTransaction(self):
		print("\n\nParse Test:\n")
		pi = Inventory(self.db)

		pi.addItem('0',100)
		print("['bottle', 10]: {}".format(pi.parseTransaction(inventory = pi, args = ['bottle', 10])))
		print("[10, 'bottle']: {}".format(pi.parseTransaction(inventory = pi, args = [10, 'bottle'])))

	def run(self):
		self.test_readFromDB()
		self.db.commit()
		self.test_MoveItem()
		self.db.commit()
		self.test_placeItem()
		self.test_parseTransaction()

class PassiveInventoryTest(TestSuite):
	def __init__(self):
		TestSuite.__init__(self)

	def test_put_take(self):
		print("\n\nPut/Take Test:\n")
		testI = PassiveInventory(self.db, title = "Parse Transaction", charInventory = None)
		testII = PassiveInventory(self.db, title = "Parse Transaction", charInventory = testI)

		testI.charInventory = testII

		testI.addItem('0',100)
		testI.addItem('1',100)
		testI.take([100, 'bottle'])

		print("Burboun only")
		self.printContents(testI)
		print("Bottles only")
		self.printContents(testII)

	def run(self):
		self.test_put_take()

if __name__ == "__main__":
	ti = InventoryTest()
	ti.run()

	input("Continue? ")
	os.system('clear')

	piTest = PassiveInventoryTest()
	piTest.run()
