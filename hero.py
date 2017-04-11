from Character import Character
class Hero(Character):
	'''
	Hero is the main character who the user plays as
	'''
	def __init__(self, db):
		Character.__init__(self, db, code = -1)

	def listItems(self):
		print("Items in your inventory:")
		super().listItems()
