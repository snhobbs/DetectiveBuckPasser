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
	userIn = userIn.lower().replace('to','').replace('with','').replace('the','').strip().split(' ')
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

import csv
def parseCSVNumString(stringIn):
	if stringIn in [None, '', 'None','NULL','Null','null']:
		return None
	csv_reader = csv.reader(stringIn)
	ret = []
	for row in csv_reader:
		ret += [int(entry) for entry in row if entry.isdigit()]
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
