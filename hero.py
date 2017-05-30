from Character import Character
class Hero(Character):
	'''
	Hero is the main character who the user plays as
	'''
	def __init__(self, db):
		Character.__init__(self, db = db, code = -1)

