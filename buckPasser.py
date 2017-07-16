#!/usr/bin/python3
import os
import buckPasserEngine

def run():
	musicDir = 'music'
	logsAndSaves = "logsAndSaves"

	try:
		os.makedirs(musicDir)
	except FileExistsError:
		pass

	try:
		os.makedirs(logsAndSaves)
	except FileExistsError:
		pass
	
	buckPasserEngine.run()

if __name__=="__main__":
	run()
