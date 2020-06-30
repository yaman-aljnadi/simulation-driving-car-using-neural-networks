from directkeys import PressKey , ReleaseKey , W
import time
from new_idea import KeyPressSample

paused = False
keys = KeyPressSample()

while True:
    if not paused:
        PressKey(W)
    keys = KeyPressSample()
    if 'T' in keys:
        if paused:
            paused = False
            print('unpaused!')
            time.sleep(1)
        else:
            print('Pausing!')
            ReleaseKey(W)
            paused = True
            time.sleep(1)

