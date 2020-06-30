import numpy as np
import cv2
import time
import os
import pandas as pd
from tqdm import tqdm
from collections import deque
from models import inception_v3 as googlenet
from random import shuffle


FILE_I_END = 3


WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 30

MODEL_NAME = 'unity_sim-{}-{}-{}-epochs-120K-data_v2.model'.format(LR, 'inception_v3',EPOCHS)
PREV_MODEL = ''
LOAD_MODEL = False

w = [0,1,0]
d = [0,0,1]
a = [1,0,0]


model = googlenet(WIDTH, HEIGHT, 3, LR, output=3, model_name=MODEL_NAME)

if LOAD_MODEL:
    model.load(PREV_MODEL)
    print('We have loaded a previous model!!!!')
else:
    pass
    

# iterates through the training files


for e in range(EPOCHS):
    #data_order = [i for i in range(1,FILE_I_END+1)]
    data_order = [i for i in range(1, FILE_I_END + 1)]
    shuffle(data_order)
    for count, i in enumerate(data_order):
        try:
            file_name = 'training_data_balanced{0}.npy'.format(i)
            # full file info
            train_data = np.load(file_name)
            print('training_data-{0}.npy'.format(i), len(train_data))

##            # [   [    [FRAMES], CHOICE   ]    ]
##            train_data = []
##            current_frames = deque(maxlen=HM_FRAMES)
##
##            for ds in data:
##                screen, choice = ds
##                gray_screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
##
##
##                current_frames.append(gray_screen)
##                if len(current_frames) == HM_FRAMES:
##                    train_data.append([list(current_frames),choice])

            # always validating unique data:
##            shuffle(train_data)
            train = train_data[:-50]
            test = train_data[-50:]

            X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
            Y = [i[1] for i in train]

            test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
            test_y = [i[1] for i in test]

            model.fit({'input': X}, {'targets': Y}, n_epoch = 1, validation_set = ({'input': test_x}, {'targets': test_y}),
                snapshot_step = 2500, show_metric = True, run_id = MODEL_NAME)

            if count % 50 == 0:
                print('SAVING MODEL!')
                model.save(MODEL_NAME)

        except Exception as e:
            print(e)
            print("why")