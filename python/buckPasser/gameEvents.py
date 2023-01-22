#gameEvents.py
from buckPasser.sqlTable import SQLTable
'''
Events
		-> Events are either getting an item or completing a conversation
		-> Testing for an event -> game tests the room you're moving to and the contents of your inventory, characters have a 'completed' flag for if they have interacted with the player yet. This is save in the database and it changes what they say. A character will only change behavior if they are important in that game stage. The character should return to some default state if this flag is hit.
'''
def checkEvent(charInvent, currRoom):
	'''
	Scan through various variables and decide if an event has happened, return true if one has, false if not. Multiple events cannot happen at the same pass through
	'''

	#1) Get the next stage which will contain item number, amount, character code. if item number is none, check character code. Both cannot be none. A character event thus has a character code and none for the item cocde, and an item event has item code and amount bit none for the character code
	#2) Game is linear, so the events can be saved in a sql table w/ stage, itemCode, amount, characterCode and tested against the hero inventory and the current room characters

	return False

class Event(SQLTable):
	def __init__(self, db):
		SQLTable.__init__(self, db)
		self.itemCode = self.elementTable.addElement(title = 'Event Item Code', name = 'itemCode', value = None, elementType = 'INT')
		self.amount = self.elementTable.addElement(title = 'Event Item Amount', name = 'amount', value = None, elementType = 'FLOAT')
		self.charCode = self.elementTable.addElement(title = 'Character Interaction Code', name = 'charCode', value = None, elementType = 'INT')
		self.objCode = self.elementTable.addElement(title = 'Object interaction code', name = 'objCode', value = None, elementType = 'INT')
		self.roomCode = self.elementTable.addElement(title = 'current room code', name = 'roomCode', value = None, elementType = 'INT')
		self.table = 'events'
		self.codeName = 'stage'

		self.nextEvent = None


class EventManager(object):
	def __init__(self, db):
		self.event = Event(db)
		self.nextEvent = None
		self.stage = None# this has to be set by the game

	def getNextEvent(self):
		'''
		Load the next event requirements into self.nextEvent
		'''
		if(self.stage == self.nextEvent):
			self.nextEvent = self.stage + 1
			self.event.setCode(self.nextEvent)
			self.event.readFromDB()

	def checkEvent(self, inventory, room):
		#get event type
		if self.event.charCode.value not in [None, 'None','', 'NULL']:
			try:
				for character in room.characters:
					if(int(character.code) == int(self.event.charCode.value)):
						if(int(character.interactedFlag.value)):
							return True
						else:
							return False
			except TypeError:#no characters in room
				pass

		elif self.event.itemCode.value not in [None, 'None', '', 'NULL']:
			entry =	inventory.getItemEntry(self.event.itemCode.value)
			if entry is None:
				return False
			elif float(entry.amount) >= float(self.event.amount.value):
				return True
			else:
				return False

		elif self.event.objCode.value not in [None, 'None','','NULL']:
			try:
				for obj in room.objects:
					if(int(obj.code) == int(self.event.objCode.value)):
						if(obj.interactedFlag.value in [True, '1', 1, 'True']):
							return True
						else:
							return False
			except TypeError:#no objects
				pass
		
		elif self.event.roomCode.value not in [None, 'None','','NULL']:
			if(int(room.code) == int(self.event.roomCode.value)):
				return True	
			else:
				return False

		else:
			raise Exception("Event {} has bad values".format(self.event.code))

	def checkGameEvent(self, inventory, room):
		self.getNextEvent()
		if self.checkEvent(inventory, room):
			self.stage += 1
			return self.stage
