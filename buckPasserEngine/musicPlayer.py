#musicPlayer.py
from multiprocessing import Process, Queue
import os
import random
from menus import Menu, MenuOption
import userInput

def playClip(fileIn):
	import simpleaudio as sa
	wave_obj = sa.WaveObject.from_wave_file(fileIn)
	playObj = wave_obj.play()
	playObj.wait_done()

def music(dirName = './', mode = 'single', repeat = False):
	def play(queue, clipList, repeat):
		if repeat == True:
			while True:
				for clip in clipList:
					playClip(clip)
		else:
			for clip in clipList:
				playClip(clip)

	def prepFiles(dirName, files):
		if type(files) not in [set, tuple, list]:
			files = [files]
		return tuple(os.path.join(dirName,option) for option in files)

	options = [fileName for fileName in os.listdir(dirName) if fileName.split('.')[-1] == 'wav']
	repeat = True
	if mode == 'single':
		optionTitles = [':\t'.join(option.split('/')[-1].split('.')[-2].split('+')) for option in options if option.split('.')[-1] == 'wav']
		fileName = options[userInput.printSelect(options = optionTitles, cursor = 'Select some sultry tunes> ')]
		filesToOpen = prepFiles(dirName, fileName)
	elif mode == 'shuffle':
		random.shuffle(options, random.random)
		filesToOpen = prepFiles(dirName, options)
	elif mode == 'playlist':
		playlists = None
		pass
	queue = Queue()
	p = Process(target=play, args=(queue, filesToOpen, repeat) )
	p.start()
	return p

class Playlist(object):
	def __init__(self, files = None, name = None):
		self.files = files
		self.name = name

class MusicMenu(Menu):
	musicDir = 'music'
	def __init__(self, db, musicProcess):
		Menu.__init__(self, db, title = "Music Menu", description="Sultry Tunes", cursor = " Music> ")
		self.addOption(MenuOption(db = db, title = "Song", description="Infinite Loop", commit = False, clear=False, action = self.song))
		#self.addOption(MenuOption(db = db, title = "Playlist", description="", commit = False, clear=False, action = self.playlist))
		self.addOption(MenuOption(db = db, title = "Shuffle", description="", commit = False, clear=False, action = self.shuffle))
		self.addOption(MenuOption(db = db, title = "Mute", description="", commit = False, clear=False, action = self.mute))
		self.musicProcess = musicProcess

	def song(self):
		self.mute()
		self.musicProcess = music(self.musicDir, mode = 'single')

	def playlist(self):
		self.mute()
		self.musicProcess = music(self.musicDir, mode = 'playlist')

	def shuffle(self):
		self.mute()
		self.musicProcess = music(self.musicDir, mode = 'shuffle')

	def mute(self):
		try:
			self.musicProcess.terminate()
		except:
			#print("Cant mute")
			pass

	def runMenu(self):
		if userInput.checkForPackage('simpleaudio'):
			super().runMenu()
		else:
			userInput.printToScreen("Simpleaudio isn't installed. Install this package to get sound.")
