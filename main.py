import os, time, sys, colorama, subprocess
from playsound import playsound
from colorama import Back as bg
from songs import wantyougone, stillalive

colorama.init()
print("\x1b[37;44m")
print(colorama.ansi.clear_screen())

game = input("""1. Portal 1: Still Alive
2. Portal 2: Want you Gone

Song Choice (1, 2): """)

if game == "2":
    wantyougone()
elif game == "1":
    stillalive()
