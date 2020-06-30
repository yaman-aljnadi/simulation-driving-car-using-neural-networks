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
from new_idea import KeyPressSample
from playsound import playsound



def keys_to_output(keys):
    #[A,W,D,S]
    output = [0,0,0]

    if "A" in keys:
        output[0] = 1
    elif "D" in keys:
        output[2] = 1
    elif "W" in keys:
        output[1] = 1

    return output
    
file_name = "training_data3_color.npy"
if os.path.isfile(file_name):
    print('file exists loading previous data!')
    training_data = list(np.load(file_name))
else:
    print("file doesn't exist, starting fresh")
    training_data = []

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

            keys = KeyPressSample()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            #print('Frame took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            if len(training_data) % 40000 == 0:
                print(len(training_data))
                np.save(file_name, training_data)
                print("saved")
                playsound("Alarm.mp3")
            elif len(training_data) % 500 == 0:
                print(len(training_data))
        
        keys = KeyPressSample()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
        cv2.imshow('window', screen)
        #cv2.imshow('window2',cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
main()
