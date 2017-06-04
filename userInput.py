#userInput.py
class Command(object):
	def __init__(self, func= None, takesArgs = False, descrip = '', hide = False):
		self.func = func
		self.takesArgs = takesArgs
		self.descrip = descrip
		self.hide = hide

	def run(self, *args, **kwargs):
		try:
			self.func(*args, **kwargs)
		except UserWarning as uw:
			print(uw)

def userInput(commands, userIn):
	'''
	take user input, conditions it, returns the command instance
	'''
	userIn = userIn.replace('to ','').replace('with ','').replace('the ','').strip().split(' ')
	#check inspect commands
	#check game commands
	try:
		command = commands[userIn[0]]
		if len(userIn) == 1 or command.takesArgs == False:
			command.run()
		else:
			command.run(userIn[1:])
	except UserWarning as uw:
		print(uw)
		return False
	except KeyError:
		return False

def parseCSVNumString(stringIn):
	if stringIn in [None, '', 'None','NULL','Null','null']:
		return None
	ret = []
	for entry in stringIn.strip().split(','):
		try:
			ret.append(int(entry))
		except ValueError:
			raise UserWarning("CSV number String passed to parseCSVNumString is not just numbers ", stringIn)
	return ret

def loadObjList(db, codeString, stage, factory):
	if codeString != None:
		codes = parseCSVNumString(codeString)
		if codes is None:
			return
		objList = []
		for code in codes:
			objList.append(factory(db, code, stage))
		return objList

def printSelect(options = None, cursor = ''):
	#options are an array of strings
	uniqueOptions = set(options)
	if(len(uniqueOptions) != len(options)):
		print(uniqueOptions, options)
		raise UserWarning("None unique options")

	for i in range(len(options)):
		print("\t%d) %s"%(i, options[i]))

	while True:
		resp = input(cursor)
		if(resp.isdigit() and int(resp) < len(uniqueOptions) and int(resp) >= 0):
			return int(resp)

def getTerminalSize():
	import shutil
	return shutil.get_terminal_size((80, 20))

def printToScreen(text):
	import textwrap
	width = getTerminalSize()[0] - 10
	for par in text.split('\n'):
		print('\n'.join(textwrap.wrap(par, width=width, tabsize=8)))
