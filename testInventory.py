#testInventory.py

import sqlite3, glob
from inventory import *
import copy

class InventoryTest(object):
	'''
	Test the Inventory Transactions
	'''
	dbFile = 'gameDB.db'

	def __init__(self):
		os.system('rm {}'.format(self.dbFile))
		os.system('touch {}'.format(self.dbFile))
		os.system("chmod +w {}".format(self.dbFile))
		print("chmod +w {}".format(self.dbFile))
		sqlFiles = ['sqlStructure.sql', 'items.sql'] + glob.glob('stage*.sql')
		for sqlFile in sqlFiles:
			os.system('sqlite3 {0} < {1}'.format(self.dbFile, sqlFile))

		os.system("chmod +w {}".format(self.dbFile))
		self.db = sqlite3.connect(self.dbFile)

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

		#_moveItem(self, itemName, amount)
		testI = Inventory(self.db)
		testI.addItem('0','300')
		testI.addItem('1','300')

		testMove('0', 'bottle', 300, testI)

		ret = testI.getItemEntry('0')
		assert(ret is None)

		del testI

	def test_placeItem(self):
		testI = Inventory(self.db)
		testII = Inventory(self.db)

		testI.addItem('0','300')
		testI.addItem('1','300')

		testI.placeItem(testII, 'bottle', '300')

		del testI
		del testII

	def run(self):
		self.test_readFromDB()
		self.db.commit()
		self.test_MoveItem()
		self.db.commit()
		self.test_placeItem()

if __name__ == "__main__":
	ti = InventoryTest()
	ti.run()
