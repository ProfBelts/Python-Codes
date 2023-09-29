# Generate a number 0 or 1
# 0 is head, 1 is tail
import numpy as np


coin = np.random.randint(0,2)



def toin_coss():
    if coin == 0:
        print("Head")
    else:
        print("Tail")


toin_coss()