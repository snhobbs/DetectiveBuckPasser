#userInput.py
try:
	import readline
except ImportError:
	try:
		import pyreadline
	except ImportError:
		pass

global gameFiles
gameFiles = 'gameFiles'

def pythonVersion():
	'''
	return the python version
	'''
	import sys
	return sys.version.split(' ')[0]

def checkForPackage(packageName):
	'''
	returns true if a package is installed
	'''
	import pip
	installed_packages = pip.get_installed_distributions()
	flat_installed_packages = [package.project_name for package in installed_packages]
	if packageName in flat_installed_packages:
		return True
	else:
		return False

def inputUniversal(arg = None):
	'''
	uses the appropriate form of input or raw_input
	'''
	version = (pythonVersion().split('.')[0])
	if version == '3':
		return input(arg)
	else:
		return raw_input(arg)

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

def genInsult():
	import random, os
	lines = []
	lineCount = 0
	with open(os.path.join(gameFiles, "insults.txt"), 'r') as f:
		for line in f:
			lineCount += 1
			lines.append(line.strip())
	insultLine = random.randint(0,lineCount-1)
	return lines[insultLine]	

def printSelect(options = None, cursor = ''):
	#options are an array of strings
	uniqueOptions = set(options)
	if(len(uniqueOptions) != len(options)):
		print(uniqueOptions, options)
		raise UserWarning("None unique options")

	for i in range(len(options)):
		printToScreen("\t%d) %s"%(i, options[i]))

	while True:
		resp = inputUniversal(cursor)
		if(resp.isdigit() and int(resp) < len(uniqueOptions) and int(resp) >= 0):
			return int(resp)
		else:
			try:
				float(resp)
				printToScreen("Look at the options you {}".format(genInsult()))
			except:
				printToScreen("You gotta type a number you {}".format(genInsult()))
def printSelectGetOption(options = None, cursor = '', exitPrompt = 'Exit'):
	'''
	uses print select to return the actual option chosen, returns None if exit selected
	'''
	listOptions = [exitPrompt] + options

	selection = printSelect(options = listOptions, cursor = cursor)
	if(selection == 0):
		return None
	else:
		return options[selection - 1]

def clearScreen():
	cols, rows = getTerminalSize()
	clearLines(rows)

def getTerminalSize():
	'''
	returns columns, rows
	'''
	import shutil
	return shutil.get_terminal_size((80, 20))

def clearLines(lines):
	printToScreen("\033[F\033[K" * lines + '\033[F\033[K', end = '')

def printToScreen(text, color='green', end = None): 	
	import textwrap, colorama, os, sys
	#colorama.ansi()

	width = getTerminalSize()[0]
	lines = 0
	colorama.init()
	ansiWin = colorama.ansitowin32.AnsiToWin32(sys.stdout)
	for par in text.split('\n'):
		wrappedLines = (textwrap.wrap(par, width=width, tabsize=4))
		lines += len(wrappedLines)
		if(os.name != 'posix'):
			print('\n'.join(wrappedLines), end = end)
			#ansiWin.write_and_convert('\n\r'.join(wrappedLines))
		else:
			print('\n'.join(wrappedLines), end = end)
	return lines
