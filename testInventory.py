#testInventory.py

import sqlite3
from inventory import *
import copy
import unittest
from game import StartGame
import os

def printContents(inventory):
	for itemEntry in inventory.items:
		print("{0.item.itemName.value} {0.amount}".format(itemEntry))

class DBTest(unittest.TestCase):
	def setUp(self):
		self.db = sqlite3.connect(self.loadDb())

	def tearDown(self):
		self.db.commit()
		self.db.close()

	def loadDb(self, fdb = 'gameDB.db'):
		os.remove(fdb)
		start = StartGame()
		return start._newGame(fdb)

	def valCheck(self, inventoryI, inventoryII):
		'''
		Checks to see if the contents of the two inventories are different
		'''
		if inventoryI is inventoryII:
			raise Exception("Inventories are identical")

		self.assertEqual(len(inventoryI.items), len(inventoryII.items))

		for itemEntryI, itemEntryII in zip(inventoryI.items, inventoryII.items):
			self.assertEqual(float(itemEntryI.amount), float(itemEntryII.amount))
			self.assertEqual(itemEntryI.item.itemName.value.lower(), itemEntryII.item.itemName.value.lower())
			self.assertEqual(int(itemEntryI.item.code), int(itemEntryII.item.code))

class InventoryTest(DBTest):
	'''
	Test the Inventory Transactions
	'''

	def Step_readFromDB(self):
		db = self.db
		testI = Inventory(db)
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

	def Step_MoveItem(self):
		def testMove(itemCode, itemName, amount, testI):
			(code, amountOut) = testI._moveItem(itemName, amount)
			self.assertEqual(amount, amountOut)
			self.assertEqual(itemCode, code)
		db = self.db
		# Move Test
		#_moveItem(self, itemName, amount)

		testI = Inventory(db)
		bottleAmount = 300
		whiskeyAmount = 300
		testI.addItem('0',bottleAmount)
		testI.addItem('1',whiskeyAmount)

		#####################################
		#move all bottles
		testMove('0', 'bottle', bottleAmount, testI)

		ret = testI.getItemEntry('0')
		self.assertIsNone(ret)

		#####################################
		#readd bottles, move more than you have, will riase userwarning
		testI.addItem('0',bottleAmount)
		with self.assertRaises(UserWarning):
			testMove('0', 'bottle', bottleAmount + 100, testI)

		testMove('0', 'bottle', bottleAmount, testI)

		#####################################
		#move in more bottles

		# Just Burboun
		self.assertIn('1', [entry.item.code for entry in testI.items])
		self.assertNotIn('0', [entry.item.code for entry in testI.items])
		self.assertEqual(len(testI.items), 1)

		testI.addItem('0','300')
		# Bottles and Burboun
		self.assertIn('1', [entry.item.code for entry in testI.items])
		self.assertIn('0', [entry.item.code for entry in testI.items])
		self.assertEqual(len(testI.items), 2)

		testMove('1', 'Whiskey', 300, testI)

		# Just Bottles
		self.assertNotIn('1', [entry.item.code for entry in testI.items])
		self.assertIn('0', [entry.item.code for entry in testI.items])
		self.assertEqual(len(testI.items), 1)


		#####################################
		#Move negative amounts
		#print("\nMove Negative Amounts")

		with self.assertRaises(UserWarning):
			testMove('0', 'bottle', -300, testI)

		self.assertEqual(testI.getItemEntryByName('bottle').amount, bottleAmount)
		del testI

	def Step_placeItem(self):
		db = self.db
		testI = Inventory(db)
		testII = Inventory(db)

		#print("\n\nPlace Item Test\n\n")

		bottleAmount = 300
		whiskeyAmount = 300
		testI.addItem('0', bottleAmount)
		self.assertEqual(len(testI.items), 1)
		testI.addItem('1',whiskeyAmount)
		self.assertEqual(len(testI.items), 2)

		testI.placeItem(testII, 'bottle', bottleAmount)
		self.assertEqual(len(testI.items), 1)
		self.assertEqual(len(testII.items), 1)

		#Move a nonexistant item
		testI.placeItem(testII, 'bottle', bottleAmount)
		self.assertEqual(bottleAmount, [entry.amount for entry in testII.items if entry.item.itemName.value.upper() == 'BOTTLE'][0])

		self.assertNotIn('WHISKEY', [entry.item.itemName.value.upper() for entry in testII.items])
		self.assertNotIn('BOTTLE', [entry.item.itemName.value.upper() for entry in testI.items])

		#Move more of an item than you have
		testI.placeItem(testII, 'Whiskey', whiskeyAmount + 100)
		self.assertEqual(whiskeyAmount, testI.getItemEntryByName('Whiskey').amount)
		self.assertEqual(bottleAmount, testII.getItemEntryByName('Bottle').amount)

		del testI
		del testII

	def Step_parseTransaction(self):
		#print("\n\nParse Test:\n")
		db = self.db
		pi = Inventory(db)

		pi.addItem('0',100)
		self.assertEqual(pi.parseTransaction(inventory = pi, args = ['bottle', 10]), pi.parseTransaction(inventory = pi, args = [10, 'bottle']))

	def test_Inventory(self):
		self.Step_readFromDB()
		self.Step_parseTransaction()
		self.Step_placeItem()
		self.Step_MoveItem()

class HeroPassiveInventoryTest(DBTest):
	def Step_drop(self):
		db = self.db
		testI = HeroInventory(db)
		testII = PassiveInventory(db, title = "Parse Transaction", charInventory = testI)
		testI.roomInventory = testII

		bottleAmount = 100
		whiskeyAmount = 1000
		testI.addItem('0',bottleAmount)
		testI.addItem('1',whiskeyAmount)
		self.assertEqual(len(testI.items), 2)

		testI.drop(['bottle', bottleAmount])

		#whiskey only
		self.assertEqual(len(testI.items), 1)
		self.assertEqual(testI.items[0].item.itemName.value.upper(), 'WHISKEY')
		self.assertEqual(testI.items[0].amount, whiskeyAmount)

		#bottles only
		self.assertEqual(len(testII.items), 1)
		self.assertEqual(testII.items[0].item.itemName.value.upper(), 'BOTTLE')
		self.assertEqual(testII.items[0].amount, bottleAmount)

	def Step_put_take(self):
		#db = sqlite3.connect(dbFile)
		db = self.db
		testI = PassiveInventory(db, title = "Parse Transaction", charInventory = None)
		testII = PassiveInventory(db, title = "Parse Transaction", charInventory = testI)

		testI.charInventory = testII

		bottleAmount = 100
		whiskeyAmount = 1000
		testI.addItem('0',bottleAmount)
		testI.addItem('1',whiskeyAmount)

		testI.take([bottleAmount, 'bottle'])

		#whiskey only
		self.assertEqual(len(testI.items), 1)
		self.assertEqual(testI.items[0].item.itemName.value.upper(), 'WHISKEY')
		self.assertEqual(testI.items[0].amount, whiskeyAmount)

		#bottles only
		self.assertEqual(len(testII.items), 1)
		self.assertEqual(testII.items[0].item.itemName.value.upper(), 'BOTTLE')
		self.assertEqual(testII.items[0].amount, bottleAmount)

	def test_hero_passive(self):
		self.Step_put_take()
		self.Step_drop()

class ReadWriteTest(DBTest):
	'''
	Ensure that the inventories are faithfully written and read from the database

	Takeaway, dont ever use writeToDB or updateTable except in internal inventory functions
	'''
	def test_readWrite(self):
		testI = Inventory(self.db)
		testII = Inventory(self.db)

		bottleAmount = 100
		whiskeyAmount = 1000
		testI.addItem('0',bottleAmount)
		testI.addItem('1',whiskeyAmount)

		self.db.commit()
		testII.setCode(testI.code)

		#read multiple times
		testII.readFromDB()
		testII.readFromDB()
		testII.readFromDB()

		print(testI.items[0].item.code, testII.items[0].item.code)
		self.valCheck(testI, testII)

if __name__ == "__main__":
	unittest.main(verbosity=2)
