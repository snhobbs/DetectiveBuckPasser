#gameEvents.py
'''
Events
		-> from  a conversation, giving/getting an item during a conversation
		-> Finding a item
		-> Entering a specific room

		-> Testing for an event -> game tests the room you're moving to and the contents of your inventory, characters have a 'completed' flag for if they have interacted with the player yet. This is save in the database and it changes what they say. A character will only change behavior if they are important in that game stage. The character should return to some default state if this flag is hit.
'''
def checkEvent(charInvent, currRoom):
	'''
	Scan through various variables and decide if an event has happened, return true if one has, false if not. Multiple events cannot happen at the same pass through
	'''

	return False
