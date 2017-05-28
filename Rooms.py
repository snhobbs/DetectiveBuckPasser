#Rooms.py
from Room import Room

def roomFactory(db, roomCode):
	roomBase = Room(db)
	roomBase.setCode(roomCode)
	roomBase.readFromDB()

	roomType = roomBase.subType.value
	if roomType == 'apartment':
		room = Apartment(db)

	elif(roomType == 'home'):
		room = HomeApt(db)

	elif(roomType == 'murder'):
		room = MurderScene(db)

	else:
		raise UserWarning("Unknown Room Type")

	room.setCode(roomCode)
	room.readFromDB()
	#room.loadRoom()
	return room

class HomeApt(Room):
	'''
	This is the so called heros apartment
	'''
	def __init__(self, db):
		Room.__init__(self, db)
		self.subType.value = 'home'

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
		self.subType.value = 'apartment'

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

class MurderScene(Apartment):
	'''
	bear is ffffuuuuccccckkkkkkkeeeddddd
	'''
	def __init__(self, db):
		Apartment.__init__(self, db)

