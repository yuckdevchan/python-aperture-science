from pydub import AudioSegment
from pydub.playback import play
import os

sfx_path = os.path.join("sfx", "menu_select.wav")

sfx = AudioSegment.from_wav(sfx_path)
play(sfx)
