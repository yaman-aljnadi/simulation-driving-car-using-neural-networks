from directkeys import PressKey , ReleaseKey , A, W, S, D
import numpy
import os
import time
import keyboard
from mouse_clicks import play_back

T = "T"

# def straight():
#     PressKey(W)
#     ReleaseKey(A)
#     ReleaseKey(D)

# def left():
#     PressKey(A)
#     PressKey(W)
#     ReleaseKey(D)
#     #time.sleep(0.05)
#     #ReleaseKey(A)

# def right():
#     PressKey(D)
#     PressKey(W)
#     #time.sleep(0.05)
#     ReleaseKey(A)

for i in list(range(10))[::-1]:
    print(i+1)
    time.sleep(1)


def start():
    PressKey(W)
    time.sleep(17)
    PressKey(A)
    time.sleep(2.4)
    ReleaseKey(A)
def first_turn():
    time.sleep(5.7)
    PressKey(A)
    time.sleep(2.25)
    ReleaseKey(A)
def secound_turn():
    time.sleep(6)
    PressKey(D)
    time.sleep(2.25)
    ReleaseKey(D)
def third_turn():
    time.sleep(8.7)
    PressKey(A)
    time.sleep(2.5)
    ReleaseKey(A)
def fourth_turn():
    time.sleep(6.2)
    PressKey(A)
    time.sleep(2.35)
    ReleaseKey(A)
def fifth_turn():
    time.sleep(16.5)
    PressKey(A)
    time.sleep(2.4)
    ReleaseKey(A)
def last_turn():
    time.sleep(14.5)
    PressKey(A)
    time.sleep(2.35)
    ReleaseKey(A)
def pause():
    keyboard.press(T)
    time.sleep(0.5)
    keyboard.release(T)
    

while True:
    start()
    first_turn()
    secound_turn()
    third_turn()
    fourth_turn()
    fifth_turn()
    last_turn()
    pause()
    play_back()
    time.sleep(7)
    pause()
    print("again")












    # # first corner
    # time.sleep(5.7)
    # PressKey(A)
    # time.sleep(2.25)
    # ReleaseKey(A)
    # #secound corner
    # time.sleep(6)
    # PressKey(D)
    # time.sleep(2.25)
    # ReleaseKey(D)
    # # third corner 
    # time.sleep(8.7)
    # PressKey(A)
    # time.sleep(2.5)
    # ReleaseKey(A)
    # #fourth corner
    # time.sleep(6.2)
    # PressKey(A)
    # time.sleep(2.35)
    # ReleaseKey(A)
    # #fifth corner 
    # time.sleep(16.5)
    # PressKey(A)
    # time.sleep(2.4)
    # ReleaseKey(A)
    # #finla turn
    # time.sleep(14)
    # PressKey(A)
    # time.sleep(2.35)
    # ReleaseKey(A)