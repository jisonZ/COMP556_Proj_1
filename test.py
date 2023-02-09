import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

if __name__ == '__main__':

    with open('rx.npy', 'rb') as f:
        rx = np.load(f)
    
    with open('ry.npy', 'rb') as f:
        ry = np.load(f)
    
    x = rx.searchsorted(60000)
    print(x)
    print(len(ry))
    y = 0
    for i in range(x, len(ry)):
        # print(ry[i])
        if ry[i] >= 0.0025:
            y = i
    test_set = ry[4662:-1]
    ma = np.max(test_set)
    print(ma)
