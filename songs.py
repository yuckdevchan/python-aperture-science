import os, time, sys, colorama, subprocess
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
        time.sleep(0.0015)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(0.25)

def print_companion_cube():
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

def print_aperture():
    typewrite_very_fast("""
                 .,-:;//;:=,
         . :H@@@MM@M#H/.,+%;,
      ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=            .---=-=:=,.
  -@#@@@MX .,              -%HX$$%%%+;
 =-./@M@M$                  .;@MMMM@MM:
 X@/ -$MM/                    .+MM@@@M$
,@M@H: :@:                    . -X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; -;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@- -,
               =++%%%%+/:-.""")

def wantyougone():
    print_companion_cube()
    subprocess.Popen(f"""{sys.executable} wantyougone.py""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    typewrite("'Want you Gone' by GLaDOS")
    typewrite_fast("FORMS FORM-29827281-12-2:")
    typewrite_fast("Notice of Dismissal")
    time.sleep(1.6)
    typewrite("\nWell here we are again")
    time.sleep(0.25)
    typewrite("It's always such a pleasure")
    time.sleep(0.1)
    typewrite("Remember when you tried to kill me twice?")
    time.sleep(0.75)
    typewrite("Oh how we laughed and laughed")
    typewrite("Except I wasn't laughing")
    typewrite("Under the circumstances")
    time.sleep(0.1)
    typewrite("I've been shockingly nice")
    typewrite("")
    time.sleep(0.125)
    typewrite("You want your freedom?")
    for letter in " Take it.":
        time.sleep(0.23)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(1.3)
    typewrite("That's what I'm counting on")
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
    time.sleep(1)
    print("")
    typewrite("You've got your short sad life left")
    time.sleep(0.5)
    typewrite("That's what I'm counting on")
    time.sleep(1)
    typewrite("I'll let you get right to it")
    typewrite("Now I only want you gone")
    print("")
    typewrite("Goodbye my only friend")
    typewrite("Oh, did you think I meant you?")
    typewrite("That would be funny")
    typewrite("if it weren't so sad")
    typewrite("Well you have been replaced")
    typewrite("I don't need anyone now")
    typewrite("When I delete you maybe")
    typewrite("I'll stop feeling so bad")
    print("")
    typewrite("Go make some new disaster")
    typewrite("That's what I'm counting on")
    typewrite("You're someone else's problem")
    typewrite("Now I only want you gone")
    typewrite("Now I only want you gone")
    typewrite("Now I only want you")
    print(colorama.ansi.clear_screen())
    typewrite("gone.")

    print("\n")
    time.sleep(1)

def stillalive():
    print_aperture()
    subprocess.Popen(f"""{sys.executable} stillalive.py""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    typewrite("'Still Alive' by GLaDOS")
    typewrite_fast("Forms FORM-29827281-12:")
    typewrite_fast("Test Assessment Report")
    print("")
    time.sleep(4)
    typewrite("This was a triumph.")
    time.sleep(2)
    typewrite("I'm making a note here:")
    typewrite("HUGE SUCCESS.")
    time.sleep(1.2)
    typewrite("It's hard to overstate")
    time.sleep(0.75)
    typewrite("my satisfaction.")
    time.sleep(1)
    typewrite("Aperture Science")
    typewrite("We do what we must")
    typewrite("because we can.")
    typewrite("For the good of all of us.")
    typewrite("Except the ones who are dead.")
    print("")
    typewrite("But there's no sense crying")
    typewrite("over every mistake")
    typewrite("You just keeping on trying")
    typewrite("till you run out of cake.")
    typewrite("And the science gets done.")
    typewrite("And you make a neat gun.")
    typewrite("For the people who are")
    typewrite("still alive.")
