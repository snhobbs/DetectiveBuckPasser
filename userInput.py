#userInput.py
class Command(object):
	def __init__(self, func):
		self.func = func

	def run(self):
		try:
			self.func()
		except UserWarning as uw:
			print(uw)

def userInput(commands, userIn):
	'''
	take user input, conditions it, returns the command instance
	'''
	userIn = userIn.lower().strip().split(' ')
	#check inspect commands
	#check game commands
	try:
		command = commands[userIn[0]]
	except:
		return False
	return command
