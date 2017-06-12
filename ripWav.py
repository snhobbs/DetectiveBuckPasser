import pytube, os, shutil, readline, sys
musicDir = '../music'
ytube = pytube.api.YouTube(raw_input("video url: "))
ytube.set_filename(raw_input('File Name: '))
video = ytube.get(extension='mp4', resolution='360p')
outFile = os.join(musicDir, (raw_input('Artist: ').replace(' ', '\ ') + '+' + raw_input('Song Name: ').replace(' ', '\ ') + '.wav'))
video.download('./')
sys.call(["ffmpeg", "-i {} {}".format(ytube.filename + '.mp4', outFile)])
os.remove("{}.mp4".format(ytube.filename))

