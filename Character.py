from sqlTable import SQLTable, StagedSqlTable
import userInput
import inventory
from menus import Menu, MenuOption

class CharacterMenu(Menu):
	def __init__(self, db):
		Menu.__init__(self, db, title = self.charName.value, description="Character Menu", cursor = "What do you want to do? ")
		self.addOption(MenuOption(db = db, title = "Talk", description="Talk to {0.charName.value}".format(self), commit = True, clear=True, action = self.talk))
		self.addOption(MenuOption(db = db, title = "Give/Get Items", description="Transfer items  between you", commit = True, clear=True, action = self.inventory.itemTransfer))
		self.addOption(MenuOption(db = db, title = "Assault", description="", commit = True, clear=True, action=self.assault))

class Character(StagedSqlTable, CharacterMenu):
	'''
	Character is the base class for all characters in the game
	'''
	def __init__(self, db = None, code = None, subType = None, charName = None, money = None, bac = None, descrip = None):
		SQLTable.__init__(self, db)
		self.code = code
		self.stage = self.elementTable.addElement(title = 'Game Stage', name = 'stage', value = 0, elementType = 'INT')
		self.subType = self.elementTable.addElement(title = 'Characters Type', name = 'subType', value = subType, elementType = 'STRING')
		self.charName = self.elementTable.addElement(title = 'Characters Name', name = 'charName', value = charName, elementType = 'STRING')
		self.money = self.elementTable.addElement(title = 'Characters Net Worth', name = 'money', value = money, elementType = 'FLOAT')
		self.descrip = self.elementTable.addElement(title = 'Character Description', name = 'descrip', value = descrip, elementType = 'STRING')

		self.table = 'chars'
		self.codeName = 'charCode'
		self.inventoryCode = None
		self.inventory = None
		self.addInventory(inventory.Inventory(self.db))
		CharacterMenu.__init__(self, db)

	def kill(self):
		print("Don't shoot him, what the hell's wrong with you, you gaddamn maniac?")

	def assault(self):
		print("Don't go fighting")

	def talk(self):
		input()
		self.runMenu()
		input()

	def listItems(self):
		if self.inventory == None or len(self.inventory.items) < 0:
			print('Nothing found')
		else:
			self.inventory.listItems()

	def search(self):
		self.listItems()

	def describe(self):
		print("\n{0.charName.value}\n-------------------\n{0.descrip.value}".format(self))

	def addInventory(self, inventory):
		self.inventory = inventory
		self.inventoryCode = self.inventory.code
		self.inventory.writeToDB()
