
import pandas as pd
import numpy as np

for item in range(0,120):
    if item % 3 == 1 and item % 5 == 3:
        print('Cracked')
    elif item % 3 == 1:
        print('Half Cracked')
    elif item % 5 == 0:
        print('High5')
    else :
        print(item)