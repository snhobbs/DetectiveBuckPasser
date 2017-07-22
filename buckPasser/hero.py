from buckPasser.Character import Character
from buckPasser.inventory import HeroInventory, PassiveInventory
class Hero(Character):
	'''
	Hero is the main character who the user plays as
	'''
	def __init__(self, db):
		Character.__init__(self, db = db, code = -1)
		self.inventory = HeroInventory(db = db)
		self.inventory.code = 0
		self.inventoryCode = 0
		self.inventory.readFromDB()
		self.inventory.refreshList()

