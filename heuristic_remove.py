import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
if __name__ == '__main__':

    with open('rx.npy', 'rb') as f:
        rx = np.load(f)
    
    with open('ry.npy', 'rb') as f:
        ry = np.load(f)

    fx, fy = [], []
    real_max = ry[-1]
    for i in range(len(ry)):
        if ry[i] <= ry[-1]:
            fy.append(ry[i])
            fx.append(rx[i])
    
    slope, intercept, r, p, std_err = stats.linregress(fx,fy)
    xseq = np.linspace(0, 65535, num=100)
    print(f"Regression to {intercept*1e3}ms")
    plt.scatter(fx, fy)
    plt.plot(xseq, intercept + slope * xseq, color='k', lw=2.5, label='Regression line, Independent Latency = {}ms'.format(intercept*1e3))
    plt.xlabel('Data Size/Bytes')
    plt.ylabel('Total Transmission Time/s')
    plt.legend()
    plt.savefig('result_1.png')
    plt.show()