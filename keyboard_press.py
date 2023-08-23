import msvcrt
import time


def kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = msvcrt.getch()
    else:
        ret = False
    return ret

number = 1

while True:
    x = kbfunc()
    if x != False:
        print("keypress:", x.decode())

#kbfunc()

"""
while True:
    x = kbfunc()
    if x != False and x.decode() == 's':
        print("STOPPING, KEY:", x.decode())
        break
    else:
        print(number)
        number += 1
        time.sleep(0.5)
"""

