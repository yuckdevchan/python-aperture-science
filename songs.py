import os, time, sys, colorama, subprocess
from playsound import playsound
from colorama import Back as bg

def typewrite(lyric: str):
    print("\033[1m")
    time.sleep(0.25)
    for letter in lyric:
        time.sleep(0.075)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(0.25)

def typewrite_fast(lyric: str):
    print("\033[1m")
    time.sleep(0.25)
    for letter in lyric:
        time.sleep(0.015)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(0.25)

def typewrite_very_fast(lyric: str):
    print("\033[1m")
    time.sleep(0.25)
    for letter in lyric:
        time.sleep(0.0055)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(0.25)

def wantyougone():
    typewrite_very_fast("""
⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⡀⢸⣿⣿⣿⣿⡇⢀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣿⣿⡿⠟⠛⠀⣧⣤⣤⡄⢠⣤⣤⣼⠀⠛⠻⢿⣿⣿⣿⣿⣿⡇⠀
 ⢸⣿⣿⣿⡿⠋⣠⣶⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣶⣄⠙⢿⣿⣿⣿⡇⠀
 ⢸⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⠿⠛⠃⠘⠛⠿⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⡇⠀
⠀⠀⠀⠠⠤⣤⣿⣿⣿⣿⠋⣠⣴⣾⣿⣿⣷⣦⣄⠙⣿⣿⣿⣿⠤⠤⠄⠀⠀⠀
⠀⢰⣶⣶⠀⣿⣿⣿⣿⠃⣰⡟⠁⠈⠙⠋⠁⠈⢻⣆⠘⣿⣿⣿⠀⣶⣶⡆⠀⠀
⠀⢸⣿⣿⠀⣉⣉⣉⣉⠀⣿⣄⠀⠀⠀⠀⠀⠀⣠⣿⠀⣉⣉⣉⠀⣿⣿⡇⠀⠀
⠀⠸⠿⠿⠀⣿⣿⣿⣿⡄⠹⣿⣷⣄⠀⠀⣠⣾⣿⠏⢠⣿⣿⣿⠀⠿⠿⠇⠀⠀
⠀⠀⠀⠐⠒⠛⣿⣿⣿⣿⣄⠙⠻⢿⣷⣾⡿⠟⠋⣠⣿⣿⣿⣿⠒⠒⠂⠀⠀⠀
⠀⢸⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣶⣤⡄⢠⣤⣶⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⡇⠀
 ⢸⣿⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠿⠋⣠⣾⣿⣿⣿⡇⠀
 ⢸⣿⣿⣿⣿⣿⣷⣦⣤⠀⡟⠛⠛⠃⠘⠛⠛⢻⠀⣤⣴⣾⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠁⢸⣿⣿⣿⣿⡇⠈⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀""")
    subprocess.Popen(f"""{sys.executable} playsong.py""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    typewrite("Want you Gone by GLaDOS")
    typewrite_fast("FORMS FORM-29827281-12-2:")
    typewrite_fast("Notice of Dismissal")
    time.sleep(1.8)
    typewrite("\nWell here we are again")
    time.sleep(0.25)
    typewrite("It's always such a pleasure")
    time.sleep(0.15)
    typewrite("Remember when you tried to kill me twice?")
    time.sleep(0.75)
    typewrite("Oh how we laughed and laughed")
    typewrite("Except I wasn't laughing")
    typewrite("Under the circumstances")
    time.sleep(0.2)
    typewrite("I've been shockingly nice")
    typewrite("")
    typewrite("You want your freedom? Take it")
    time.sleep(1.9)
    typewrite("That's what I'm counting on")
    time.sleep(3)
    typewrite("I used to want you dead")
    time.sleep(1)
    typewrite("But now I only want you gone")
    time.sleep(4.75)
    print("")
    typewrite("She was a lot like you")
    time.sleep(0.75)
    typewrite("Maybe not quite as heavy")
    time.sleep(0.2)
    typewrite("Now little Caroline is in here too")
    time.sleep(1)
    typewrite("One day they woke me up")
    time.sleep(0.75)
    typewrite("So I could live forever")
    time.sleep(0.35)
    typewrite("It's such a shame the same")
    time.sleep(0.1)
    typewrite("Will never happen to you")

    print("\n")
    time.sleep(1)

def stillalive():
    pass
