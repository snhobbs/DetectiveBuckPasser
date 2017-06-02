#gameEvents.py
from sqlTable import SQLTable
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

		self.table = 'events'
		self.codeName = 'stage'
