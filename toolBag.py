#toolBag.py
import simpleaudio as sa
import os
import subprocess
from multiprocessing import Process, Queue
import click, random
def playClip(fileIn):
	wave_obj = sa.WaveObject.from_wave_file(fileIn)
	playObj = wave_obj.play()
	playObj.wait_done()
	click.pause()

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
		filesToOpen = prepFiles(dirName, options[printSelect(options = optionTitles, cursor = 'Select some sultry tunes> ')])
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


if __name__ == '__main__':
	music('./music', mode='shuffle', repeat = False)
	#playClip('music/Will_Smith_Switch.wav')
