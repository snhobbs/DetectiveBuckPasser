#inventory.py
from sqlTable import SQLTable

class Inventory(SQLTable):#when interfacing w/ the db need to loop through all the items and their count as its duplicated
	def __init__(self, db):
		SQLTable.__init__(self, db)
		inventoryCode = None
		itemCount = None
		self.inventory = None#tuple of ((item code, count),)
		self.table = 'Inventory'
		self.codeName = 'inventoryCode'

	def addItem(self):
		pass

	def dropItem(self):
		pass

	def placeItem(self):
		pass
