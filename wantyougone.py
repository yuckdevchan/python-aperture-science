from pydub import AudioSegment
from pydub.playback import play
import os

song_path = os.path.join("music", "wantyougone.wav")

song = AudioSegment.from_wav(song_path)
play(song)
