import numpy as np
import pandas as pd 
from collections import Counter
from random import shuffle
import cv2

train_data = np.load("training_data_balanced1_colored.npy")

# print(train_data[10][0])
# print(len(train_data))
# df = pd.DataFrame(train_data)
# print(df.head())
# print(Counter(df[1].apply(str)))

# lefts = []
# rights = []
# forwards = []

# shuffle(train_data)

# for data in train_data:
#     img = data[0]
#     choice = data[1]

#     if choice == [1,0,0]:
#         #print("w")
#         lefts.append([img, choice])
#     elif choice == [0,1,0]:
#         #print("s")
#         forwards.append([img, choice])
#     elif choice == [0,0,1]:
#         #print("D")
#         rights.append([img, choice])
#     else:
#         pass
#         #print("no matches")


# forwards = forwards[:len(lefts)][:len(rights)]
# lefts = lefts[:len(forwards)]
# rights = lefts[:len(rights)]

# final_data = forwards + lefts + rights

# shuffle(final_data)
# print(len(final_data))
# np.save("training_data_v2.npy", final_data)

# use this loop if you wana check the data

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow("test", img)
    print(choice)
    if cv2.waitKey(25) & 0xff == ord("q"):
        cv2.destroyAllWindows()
        break


