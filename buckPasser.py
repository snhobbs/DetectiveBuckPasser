#!/usr/bin/python3
import os
import buckPasserEngine

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

