#sqlTable.py
def scrubSql(stringIn):
	if type(stringIn) == str:
		return stringIn.replace(';','\v').replace("'",'|').replace('"','|')
	else:
		return stringIn

def descrubSql(stringIn):
	if type(stringIn) == str:
		return stringIn.replace('\v',';').replace("|","'")
	else:
		return str(stringIn)

class sqlInterface(object):
	def __init__(self,db):
		self.db = db
		self.table = None
		self.codeName = None

	@property
	def tableCode(self):
		return (self.codeName, self.code)

	def assignCode(self):
		code = self.getMaxInTable(self.codeName)
		if code == None:
			self.setCode(0)
		else:
			self.setCode(code + 1)

	def setCode(self, code):
		self.code = code

	def conditionalStatement(self,conditions):
		'''
		sqllite3 has different conditional syntax from mysql/mariadb
		'''
		if(conditions is None):
			return ''
		arg = ['WHERE (']
		if(type(conditions) in [list, tuple]):
			if( not type(conditions[0]) in [list, tuple]):
				conditions = [conditions]
			arg.append(' AND '.join(['{0[0]} = "{0[1]}"'.format(cond) for cond in conditions]))
			#arg.append(','.join(["{}".format(cond[0]) for cond in conditions]) )
			#arg.append(') = (')
			#arg.append(','.join(["'{}'".format(cond[1]) for cond in conditions]) )
			arg.append(')')
		else:
			raise UserWarning('Conditional input must be an array or tuple {}'.format(conditions))
		return ''.join(arg)

	def updateSql(self, inputs, conditions):
		#inputs are a tuple of the form ((variable name, value),)
		#conditions are (table name, value)
		dbCursor = self.db.cursor()
		arg = ['UPDATE %s SET '%(self.table)]
		argString = []
		for inVal in inputs:
			if(str(inVal[1]).upper() == 'NULL'):
				argStr.append(", {0[0]} = NULL ".format(inVal))
			else:
				argString.append(", {0[0]} = '{0[1]}' ".format(inVal))
		arg.append(''.join(argString).strip(','))
		arg.append(self.conditionalStatement(conditions))
		dbCursor.execute(''.join(arg))

	def insertSql(self, inputs):
		dbCursor = self.db.cursor()
		arg = ['INSERT INTO %s ('%(self.table)]
		arg.append(','.join([inVal[0] for inVal in inputs]).strip(','))

		arg.append(") VALUES (")
		argString = []
		for inVal in inputs:
			if(str(inVal[1]).upper() == 'NULL'):
				argString.append(", NULL")
			else:
				argString.append(", '{0[1]}'".format(inVal))
		arg.append(''.join(argString).strip(','))
		arg.append(')')

		dbCursor.execute(''.join(arg))

	def selectSql(self, columnNames = '', conditions=None):
		dbCursor = self.db.cursor()
		arg = ['SELECT ']
		arg.append(','.join(columnNames))
		arg.append(" FROM %s "%(self.table))

		arg.append(self.conditionalStatement(conditions) + ';')
		dbCursor.execute(''.join(arg))
		resp = dbCursor.fetchall()
		if(len(resp) == 0 or resp[0] is None):
			return None
		else:
			return resp

	def deleteSql(self, conditions):
		dbCursor = self.db.cursor()

		arg = 'DELETE FROM {0.table} {1} AND {0.tableCode[0]} = "{0.tableCode[1]}";'.format(self, self.conditionalStatement(conditions))

		dbCursor.execute(arg)

	def getMaxInTable(self, columnName = '', conditions = None):
		condStatment = self.conditionalStatement(conditions)
		dbCursor = self.db.cursor()
		arg = 'SELECT MAX(%s) FROM %s %s'%(columnName, self.table, condStatment)
		dbCursor.execute(arg)
		resp = dbCursor.fetchall()
		if(resp[0][0] is None):
			return None
		else:
			return int(resp[0][0])

	def getCountInTable(self, conditions = None):
		condStatment = self.conditionalStatement(conditions)
		dbCursor = self.db.cursor()
		arg = 'SELECT COUNT(*) FROM %s %s'%(self.table, condStatment)
		dbCursor.execute(arg)
		resp = dbCursor.fetchall()
		if(resp[0][0] is None):
			return None
		else:
			return int(resp[0][0])

class SQLTable(sqlInterface):
	'''
	This is the top wrapper for a generic sql table
	'''
	def __init__(self, db):
		sqlInterface.__init__(self,db)
		self.elementTable = TableDataElements()

	@property
	def columnNames(self):
		return self.elementTable.getNames

	@property
	def getVals(self):
		return self.elementTable.getValues

	def writeToDB(self):
		inserts = [self.tableCode]
		inserts.extend((element.name, scrubSql(element.value)) for element in self.elementTable.elements)
		self.insertSql(inputs = inserts)

	def readFromDB(self):
		resp = self.selectSql(columnNames = self.columnNames, conditions = self.tableCode)
		if(resp is None):
			raise UserWarning("No information for this {0.tableCode[0]} = {0.tableCode[1]} in table {0.table}".format(self))
		self.formatInput(resp[0])#returns a tuple of ((),)

		for element in self.elementTable.elements:
			if(element.value is None):
				element.value = ''
			element.value = str(element.value)

	def updateTable(self):
		updates = [(element.name, scrubSql(element.value)) for element in self.elementTable.elements if element.updatable]

		if len(updates) > 0:
			self.updateSql(inputs = updates, conditions = self.tableCode)

	def formatInput(self, inVals):
		for element, value in zip(self.elementTable.elements, inVals):
			element.value = descrubSql(value)

class TableElement(object):
	elementTypes = ['FILE', 'STRING', 'INT', 'FLOAT', 'BOOL']
	def __init__(self, title, name, value, elementType, options, updatable=True):
		self.title = title
		self.name = name
		self.value = value
		self.elementType = elementType#for the UI
		self.options = options
		self.updatable = updatable
		self.typeCheck()
	@property
	def sqlPair(self):
		return (self.name, self.value)

	@property
	def titlePair(self):
		return (self.title, self.value)

	def typeCheck(self):
		if(self.elementType not in self.elementTypes):
			raise UserWarning('Element Type %s is Unknown'%(self.elementType))

class TableDataElements(object):
	def __init__(self):
		self.elements = []
		self._titles = []
		self._names = []
		self._values = []

	@property
	def getValues(self):
		self._values = [element.value for element in self.elements]
		return self._values

	@property
	def getNames(self):
		return self._names

	@property
	def getTitles(self):
		return self._titles

	def addElement(self, title = None, name = None, value = '', elementType = 'STRING', options = None, updatable=True):
		element = TableElement(title=title, name=name, value=value, elementType=elementType, options = options, updatable=updatable)
		self.elements.append(element)
		self._names.append(element.name)
		self._titles.append(element.title)
		self._values.append(element.value)
		return element

class StagedSqlTable(SQLTable):
	'''
	Loads sql data based off of a stage value. The highest stage less than or equal to the current game stage is loaded
	'''
	def __init__(self, db):
		SQLTable.__init__(self, db)

	def getCurrentStage(self, stage):
		dbCursor = self.db.cursor()
		arg = 'SELECT MAX(stage) from {0.table} where stage between "0" and "{1}" and {2[0]} = {2[1]}'.format(self, stage, self.tableCode)
		dbCursor.execute(arg)
		resp = dbCursor.fetchall()
		if(len(resp) == 0 or resp[0] is None):
			return None
		else:
			return resp[0][0]

	def readFromDB(self, stage):
		self.stage.value = self.getCurrentStage(stage)
		resp = self.selectSql(columnNames = self.columnNames, conditions = (self.stage.sqlPair, self.tableCode))
		if(resp is None):
			raise UserWarning("No information for this {0.tableCode[0]} = {0.tableCode[1]} in table {0.table}".format(self))
		self.formatInput(resp[0])#returns a tuple of ((),)

		for element in self.elementTable.elements:
			if(element.value is None):
				element.value = ''
			element.value = str(element.value)

	def updateTable(self):
		'''
		same as update table in SQLTable except the conditional has the stage added
		'''
		updates = [(element.name, scrubSql(element.value)) for element in self.elementTable.elements if element.updatable]

		if len(updates) > 0:
			self.updateSql(inputs = updates, conditions = (self.tableCode, self.stage.sqlPair))
