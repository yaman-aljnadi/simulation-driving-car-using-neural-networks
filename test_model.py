import numpy as np
import cv2
import time
import pyautogui
#from grapscreen import grab_screen
from getkeys import on_press
import os
from PIL import ImageGrab
from numpy import ones,vstack
from numpy.linalg import lstsq
from statistics import mean
from alexnet import alexnet
from models import inception_v3
from new_idea import KeyPressSample
from directkeys import PressKey, ReleaseKey , W,S,A,D

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCH = 8

MODEL_NAME = "unity_sim-0.001-alexnetv2-10-epochs-120K-data.model"


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    # time.sleep(0.1)
    # time.sleep(0.05)
    # ReleaseKey(A)

def right():
    PressKey(D)
    PressKey(W)
    # time.sleep(0.05)
    ReleaseKey(A)
    # ReleaseKey(D)


model = alexnet(WIDTH,HEIGHT,lr=LR)
model.load(MODEL_NAME)

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()

    paused = False

    while True:
        if not paused:
            screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160,120))
            #print('Frame took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            prediction = model.predict([screen.reshape(WIDTH, HEIGHT,1)])[0]
            moves = list(np.around(prediction))
            print(moves, prediction)

            if moves == [1,0,0]:
                left()
            elif moves == [0,1,0]:
                straight()
            elif moves == [0,0,1]:
                right()
 
        keys = KeyPressSample()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                ReleaseKey(A)
                ReleaseKey(D)
                ReleaseKey(W)
                time.sleep(1)
                paused = True

        cv2.imshow('window', screen)
        #cv2.imshow('window2',cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
main()