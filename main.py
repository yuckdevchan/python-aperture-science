import os, time, sys, colorama, subprocess
from colorama import Back as bg
from songs import wantyougone, stillalive
from getkey import getkey, keys

loading = ["|", "/", "-", "\\"]
loading_message = "// Loading... © Aperture Science 2024" 

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

print("""\x1b[34;47m1. Portal 1: Still Alive\x1b[37;44m
2. Portal 2: Want you Gone
""")

eek = False

while True:
    key = getkey()

    if key == keys.DOWN or key == keys.UP:
        print(colorama.ansi.clear_screen())
        if eek:
            print("""\x1b[34;47m1. Portal 1: Still Alive\x1b[37;44m
2. Portal 2: Want you Gone
""")
            eek = False
        else:
            print("""1. Portal 1: Still Alive
\x1b[34;47m2. Portal 2: Want you Gone\x1b[37;44m
""")
            eek = True
    elif key == keys.ENTER:
        print(colorama.ansi.clear_screen())
        if eek:
            wantyougone()
        else:
            stillalive()
