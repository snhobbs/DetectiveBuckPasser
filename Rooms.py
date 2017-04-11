#Rooms.py
from Room import Room

def roomFactory(db, roomCode):
	roomBase = Room(db)
	roomBase.setCode(roomCode)
	roomBase.readFromDB()

	roomType = roomBase.subType.value
	if roomType == 'Apartment':
		room = Apartment(db)

	elif(roomType == 'HomeApt'):
		room = HomeApt(db)

	elif(roomType == 'MurderScene'):
		room = MurderScene(db)

	else:
		raise UserWarning("Unknown Room Type")

	room.setCode(roomCode)
	room.readFromDB()
	room.loadRoom()
	return room

class HomeApt(Room):
	'''
	This is the so called heros apartment
	'''
	def __init__(self, db):
		Room.__init__(self, db)

		self.neighbors.value = '1,2'#apt3b
		self.characterCodeString.value = None
		self.descrip.value = "You're in your garbage apartment. Your goldfish tank festers in the corner. Just another damn day."
		self.inventoryCode.value = '0'
		self.objectCodeString.value = '0,3'
		self.subType.value = 'HomeApt'

		self.code = 0

class Apartment(Room):
	'''
	needs all of the rooms for an apartment, and a couch to search
	bathroom
	bedroom
	living room
	kitchen
	'''
	def __init__(self, db):
		Room.__init__(self, db)
		self.subType.value = 'Apartment'

class Apartment_3B(Apartment):
	def __init__(self, db):
		Apartment.__init__(self, db)
		self.neighbors.value = '0,2'#next to the homeapt
		self.characterCodeString.value = '0'#3dollar man
		self.descrip.value = "Apartment 3B"
		self.inventoryCode.value = '1'
		self.objectCodeString.value = '0'

		self.code = 1

class Hallway(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)

class ParkingLot(Room):
	'''
	This is the home depot parking lot, theres the burnt out pontiac fiero
	'''
	def __init__(self, db):
		Room.__init__(self, db)

class ChachNot(Room):
	'''

	'''
	def __init__(self, db):
		Room.__init__(self, db)

class MurderScene(Room):
	'''
	bear is ffffuuuuccccckkkkkkkeeeddddd
	'''
	def __init__(self, db):
		Apartment.__init__(self, db)
		self.neighbors.value = '0'
		self.characterCodeString.value = '0,1'
		self.descrip.value = "Gruesome murder scene"
		self.objectCodeString.value = '0'

		self.code = 2
