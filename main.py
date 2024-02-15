import os, time, sys, colorama, subprocess, random
from colorama import Back as bg
from songs import wantyougone, stillalive
from getkey import getkey, keys

loading = ["|", "/", "-", "\\"]
loading_message = "// Loading... © Aperture Science 2024"
try:
    if sys.platform.startswith("linux"):
        uname = subprocess.run("uname -r", shell=True, capture_output=True, text=True).stdout
        kernel = uname.rsplit(".", 3)[0].rsplit("-")[0]
    elif sys.platform == "win32":
        kernel = os.uname().release
    elif sys.platform.startswith("darwin"):
        uname = subprocess.run("uname -r", shell=True, capture_output=True, text=True).stdout
        kernel = uname
except:
    kernel = "2.6"
hint = f"ApertureOS v{kernel}\n\n// Press Enter, Space or Right Arrow to Select an Option..."

def menu():
    colorama.init()
    print("\x1b[37;44m")
    # print("\033[48:5:166m%s\033[m\n")
    for i in range(0, 45):
        print(loading_message)
    print(colorama.ansi.clear_screen())
    j = 0
    for i in range(0, 15):
        print(loading_message, loading[j])
        time.sleep(0.1)
        print(colorama.ansi.clear_screen())
        if j == 3:
            j = 0
        else:
            j += 1
    time.sleep(1)
    print(colorama.ansi.clear_screen())

    # game = None
    # print("""1. Portal 1: Still Alive
    # 2. Portal 2: Want you Gone
    # """)

    # while game != 1 or game != 2:
    #     game = input("""
    #     Song Choice (1, 2): """)

    #     if game == "2":
    #         wantyougone()
    #     elif game == "1":
    #         stillalive()
    #     else:
    #         print("\nInvalid Option. Try Again...")

    print(f"""{hint}
        
    \x1b[34;47m1. Portal 1: Still Alive\x1b[37;44m
    2. Portal 2: Want you Gone
    """)

    eek = False

    while True:
        key = getkey()

        if key == keys.DOWN or key == keys.UP or key == keys.LATIN_SMALL_LETTER_S or key == keys.LATIN_SMALL_LETTER_W:
            print(colorama.ansi.clear_screen())
            if eek:
                print(f"""{hint}
                    
    \x1b[34;47m1. Portal 1: Still Alive\x1b[37;44m
    2. Portal 2: Want you Gone
    """)
                eek = False
            else:
                print(f"""{hint}

    1. Portal 1: Still Alive
    \x1b[34;47m2. Portal 2: Want you Gone\x1b[37;44m
    """)
                eek = True
        elif key == keys.ENTER or key == keys.RIGHT or keys.SPACE:
            print("\x1b[37;44m")
            print(colorama.ansi.clear_screen())
            if eek:
                wantyougone()
            else:
                stillalive()

try:
    menu()
except KeyboardInterrupt:
    print(colorama.ansi.clear_screen())
    for i in range(random.randint(40, 85)):
        print(f"\x1b[1;3mQuitting System... (Attempt {i + 1})")
        time.sleep(0.005)
    print(f"\nCompleted Task: 'Quitting System' in '{i + 1}' Attempts")
    print("\n\nRemember - testing is the future! And the future starts with you :D\n\n")
    sys.exit(0)
