# automates the writing of a conversation
import json

class Conversation(object):
	def __init__(self):
		self.conv = {'startOpts': [], 'options': {}}
		self.optCount = 0
		self.optBase = 'opt{}'
	
	def getOptName(self):
		name = self.optBase.format(self.optCount)
		self.optCount += 1
		return name

	def addStartOpt(self, ques, resp):
		option = self.makeOpt()
		self.conv['options'].update(option)
		self.conv['startOpts'].append(list(option.keys())[0])

	def makeOpt(self, ques, resp):
		return {self.getOptName(): {"ques": ques, "resp": resp}, "nextOpts": []}

	def addOpt(self, attachedOpt, ques, resp):
		option = self.makeOpt()
		self.conv['options'].update(option)
		self.conv['options'][attachedOpt]['nextOpts'].append(list(option.keys())[0])
	
	def printDict(self):
		return json.dumps(self.conv)
