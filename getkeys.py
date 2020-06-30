import msvcrt
import time



def kbfunc():
    #this is boolean for whether the keyboard has bene hit
    x = msvcrt.kbhit()
    if x:
        #getch acquires the character encoded in binary ASCII
        ret = msvcrt.getch()
    else:
        ret = False
    return ret


def on_press():
    while True:
        # counter = 1
        # counter += 1
        x = kbfunc()
        if x:
            key = x.decode()
            key = key.upper()
            print(key)
            return key

on_press()







