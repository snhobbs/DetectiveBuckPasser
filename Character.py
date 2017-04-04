from sqlTable import SQLTable

def characterFactory(db, code):
	charObj = Character(db = db, code = code, inventoryCode = None)
	charObj.readFromDB()
	subType = charObj.subType.value

	if subType in ['SixDollarMan']:
		return SixDollarMan(db)
	elif subType in ['Bear']:
		return SixDollarMan(db)

	raise UserWarning('Unknown Character subType {}'.format(subType))

class Character(SQLTable):
	'''
	Character is the base class for all characters in the game
	'''
	def __init__(self, db, code, inventoryCode):
		SQLTable.__init__(self, db)
		self.code = code
		self.subType = self.elementTable.addElement(title = 'Characters Type', name = 'subType', value = None, elementType = 'STRING')
		self.charName = self.elementTable.addElement(title = 'Characters Net Worth', name = 'charName', value = None, elementType = 'STRING')
		self.money = self.elementTable.addElement(title = 'Characters Net Worth', name = 'money', value = None, elementType = 'FLOAT')
		self.bac = self.elementTable.addElement(title = 'Blood Alcohol Content', name = 'bac', value = 0, elementType = 'FLOAT')
		self.descrip = self.elementTable.addElement(title = 'Character Description', name = 'descrip', value = None, elementType = 'STRING')

		self.inventoryCode = inventoryCode
		self.table = 'chars'
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
		self.code = 0
		self.inventoryCode = 0
		Character.__init__(self,db, self.code, self.inventoryCode)
		self.subType.value = 'SixDollarMan'
		self.charName.value = 'Six Dollar Man'
		self.money.value = 6
		self.bac.value = .6
		self.descrip.value = "Randy Savage except with a viciously failed wrestling career following a failed marriage. Weakness are his ex wife Sharron, alimony, and the IRS."

class Bear(Character):
	def __init__(self,db):
		self.code = 1
		self.inventoryCode = 0
		Character.__init__(self,db, self.code, self.inventoryCode)
		self.subType.value = 'Bear'
		self.charName.value = 'Bear'
		self.money.value = float('inf')
		self.bac.value = 0
		self.descrip.value = "Trust fund animal. Yeah he sucks but his net worth is absurd. Problem is he wouldn't stop calling at dinner. Really his existance was the issue. If you're thinking one shouldn't speak ill of the dead, you clearly didn't know Bear"
