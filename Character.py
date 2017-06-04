from sqlTable import SQLTable, StagedSqlTable
import userInput
import inventory
from menus import Menu, MenuOption

def characterFactory(db, code, stage):
	charObj = Character(db = db, code = code)
	charObj.readFromDB(stage)

	return charObj

class CharacterMenu(Menu):
	def __init__(self, db):
		Menu.__init__(self, db, title=self.charName.value, description="Character Menu", cursor="What do you want to do? ")
		self.addOption(MenuOption(db = db, title = "Talk", description="Talk to {0.charName.value}".format(self), commit = True, clear=True, action = self.talk))
		#self.addOption(MenuOption(db = db, title = "Give/Get Items", description="Transfer items  between you", commit = True, clear=True, action = self.inventory.itemTransfer))
		self.addOption(MenuOption(db = db, title = "Assault", description="", commit = True, clear=True, action=self.assault))

class Character(StagedSqlTable, CharacterMenu):
	'''
	Character is the base class for all characters in the game
	'''
	def __init__(self, db, code = None):
		StagedSqlTable.__init__(self, db)
		self.code = code
		self.stage = self.elementTable.addElement(title = 'Game Stage', name = 'stage', value = 0, elementType = 'INT')
		self.subType = self.elementTable.addElement(title = 'Characters Type', name = 'subType', value = 'standard', elementType = 'STRING', updatable = False)
		self.charName = self.elementTable.addElement(title = 'Characters Name', name = 'charName', value = None, elementType = 'STRING', updatable = False)
		self.money = self.elementTable.addElement(title = 'Characters Net Worth', name = 'money', value = None, elementType = 'FLOAT')
		self.descrip = self.elementTable.addElement(title = 'Character Description', name = 'descrip', value = None, elementType = 'STRING', updatable = False)
		self.jsonConv = self.elementTable.addElement(title = 'Conversation Object', name = 'conv', value = None, elementType = 'STRING', updatable = False)
		self.defaultJsonConv = self.elementTable.addElement(title = 'Conversation Object After Interaction', name = 'defaultConv', value = None, elementType = 'STRING', updatable = False)
		self.interactedFlag = self.elementTable.addElement(title = 'Stage Interaction Flag', name = 'interactedFlag', value = None, elementType = 'BOOL')

		self.table = 'chars'
		self.codeName = 'charCode'
		self.inventoryCode = None
		self.inventory = None
		self.addInventory(inventory.Inventory(self.db))
		CharacterMenu.__init__(self, db)

		self.commands = {
			'describe' : userInput.Command(func=self.describe, takesArgs=False, hide = True),
			'search' : userInput.Command(func=self.search, takesArgs=False, hide = True),
			'talk' : userInput.Command(func=self.runCharMenu, takesArgs=False, hide = True)
			}

	def runCharMenu(self):
		self.title = self.charName.value
		self.runMenu()

	def assault(self):
		userInput.printToScreen("That's just more paper work")

	def talk(self):
		'''
		Pass JSON conversation to self.conversation
		'''
		import json
		if(self.interactedFlag.value in [True, 'True', '1', 1] or self.jsonConv.value is None):
			conv = json.loads(self.defaultJsonConv.value)
		else:
			conv = json.loads(self.jsonConv.value)
			self.interactedFlag.value = True
		self.conversation(conv)

	def conversation(self, conv):
		def printResp(charName, resp):
			userInput.printToScreen("{}: {}".format(charName, resp))
		#print the conversation in an enumerated list
		nextOpts = conv['startOpts']

		while(len(nextOpts) > 0):
			optionZero = conv['options'][nextOpts[0]]
			if (optionZero['ques']) is None:#skip selection if there is no 'ques'
				selection = 0
			else:
				selection = userInput.printSelect(options = [conv['options'][opt]['ques'] for opt in nextOpts], cursor = 'Say Something> ')

			try:
				opt = conv['options'][nextOpts[selection]]
				printResp(self.charName.value, opt['resp'])
				nextOpts = opt['nextOpts']
			except TypeError:
				break

	def listItems(self):
		if self.inventory is None or len(self.inventory.items) < 0:
			userInput.printToScreen('Nothing found')
		else:
			self.inventory.menu.runMenu()

	def search(self):
		self.listItems()

	def describe(self):
		userInput.printToScreen("\n{0.charName.value}\n-------------------\n{0.descrip.value}".format(self))

	def addInventory(self, inventory):
		self.inventory = inventory
		self.inventoryCode = self.inventory.code
		self.inventory.writeToDB()
