import pytube, os, shutil, subprocess
musicDir = 'music'
ytube = pytube.api.YouTube(input("video url: "))
ytube.set_filename(input('File Name: '))
video = ytube.get(extension='mp4', resolution='360p')
outFile = os.path.join(musicDir, (input('Artist: ').replace(' ', '\ ') + '+' + input('Song Name: ').replace(' ', '\ ') + '.wav'))
video.download('./')
os.system("ffmpeg -i {} {}".format(ytube.filename + '.mp4', outFile))
os.remove("{}.mp4".format(ytube.filename))

