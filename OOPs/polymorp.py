class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid filename format")

class MP3File(AudioFile):

    ext= "mp3"
    def play(self):
        print("Playing MP3 file")

class WaveFile(AudioFile):
    ext = 'wav'
    def play(self):
        print("Playing Wav file")

mp = MP3File("song.mp3")
mp.play()

wv = WaveFile("song.wav")
wv.play()

wv_incorrect = WaveFile("song.wa")
wv_incorrect.play()
