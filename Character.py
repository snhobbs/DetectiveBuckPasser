from sqlTable import SQLTable
class Character(SQLTable):
	'''
	Character is the base class for all characters in the game
	'''
	def __init__(self, db, code, inventoryCode):
		SQLTable.__init__(self, db)
		self.code = code
		self.charName = self.elementTable.addElement(title = 'Characters Net Worth', name = 'charName', value = None, elementType = 'STRING')
		self.money = self.elementTable.addElement(title = 'Characters Net Worth', name = 'money', value = None, elementType = 'FLOAT')
		self.bac = self.elementTable.addElement(title = 'Blood Alcohol Content', name = 'bac', value = 0, elementType = 'FLOAT')
		self.location = self.elementTable.addElement(title = 'Current Location', name = 'roomCode', value = None, elementType = 'INT')#room code
		self.descrip = self.elementTable.addElement(title = 'Character Description', name = 'descrip', value = None, elementType = 'STRING')

		self.inventoryCode = inventoryCode
		self.table = 'people'
		self.codeName = 'charCode'

	def grab(self):
		pass

	def store(self):
		pass

	def move(self):
		pass

	def look(self):
		pass

	def drink(self):
		pass

	def talk(self):
		pass

class SixDollarMan(Character):
	def __init__(self,db):
		Character.__init__(self,db)
		self.code = 0
		self.charName.value = 'Six Dollar Man'
		self.money.value = 6
		self.bac.value = .6
		self.location.value = 0
		self.descrip.value = "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS."


