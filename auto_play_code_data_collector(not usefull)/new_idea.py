import keyboard, time
T = "T"
def KeyPressSample(W = 'W', D = "D" , A = "A", pause = "t", Stop = "esc"):
    while True:  # making a inifinte loop
        try:
            # if keyboard.is_pressed(W):
            #     time.sleep(0.1)
            #     #print(W)
            #     return "W"
            if keyboard.is_pressed(D):
                #time.sleep(0.1)
                #print(D)
                return "D"
            elif keyboard.is_pressed(A):
                #time.sleep(0.1)
                #print(A)
                return "A"
            elif keyboard.is_pressed(pause):
                print("paused")
                return "T"
            elif keyboard.is_pressed(Stop):
                print("stoping")
                break
            else:
                time.sleep(0.1)
                return "W"
        except KeyboardInterrupt:
            print('\nDone Reading input. Keyboard Interupt.')
            break
        except Exception as e:
            print(e)
            break


