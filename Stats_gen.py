import argparse
import subprocess
from scipy import stats
import matplotlib.pyplot as plt
import sys
import os
from tqdm import tqdm
import numpy as np

def getRRT():
    with open("./Part3.log", "r") as f:
        firstline = f.readline()
        numRRT = int(firstline)
        RRT = []
        for i in range(int(numRRT/2)):
            sendtime = float(f.readline())
            recvtime = float(f.readline())
            RRT.append((recvtime-sendtime)/2)
    return RRT



def reject_outliers(data, m=2):
    return data[np.abs(data - np.mean(data)) < m * np.std(data)]

def main():
    parser = argparse.ArgumentParser(description='Calcualte Network Delay')
    parser.add_argument('--m', type=int, help='Iteration for evaluate delay measure accuracy', default = 10)
    parser.add_argument('--n', type=int, help='Iteration for evaluate independent delay', default = 100)
    args = parser.parse_args()
    """
    for n iteration:
        change data size
        calculate average latency
    linear regression, get intercept as latency
    """
    data_size_axis = []
    latency_axis = []
    for j in tqdm(range(args.n)):
        data_size = int(18 + j*((65535-18)/args.n))
        client_cmd = ['./client_num', 'ccnc-01.arc.rice.edu', '18188', f"{data_size}", "100"]
        subprocess.Popen(client_cmd, stdout=subprocess.DEVNULL).wait()
        allRRT = getRRT()
        # avgLat = sum(allRRT)/len(allRRT)
        # print(f"Average Latency {avgLat} for data size {data_size}")
        for i in range(len(allRRT)):
            latency_axis.append(allRRT[i])
            data_size_axis.append(data_size)

    # plt.scatter(data_size_axis, latency_axis)
    # plt.show()



    x , y  = [] , []
    for i in range(len(latency_axis)):
        if latency_axis[i] > 0:
            y.append(latency_axis[i])
            x.append(data_size_axis[i])


    latency_mean = np.mean(y)
    latency_stddev = np.std(y)

    rx, ry = [], []
    for i in range(len(y)):
        if np.abs(y[i] - latency_mean) < 2 * latency_stddev:
            ry.append(y[i])
            rx.append(x[i])
        else:
            print("Remove " + str(y[i]))
    slope, intercept, r, p, std_err = stats.linregress(rx,ry)
    xseq = np.linspace(0, 65535, num=100)
    print(f"Regression to {intercept*1e3}ms")
    plt.scatter(rx, ry)
    plt.plot(xseq, intercept + slope * xseq, color='k', lw=2.5, label='Regression line, Independent Latency = {}ms'.format(intercept*1e3))
    plt.xlabel('Data Size/Bytes')
    plt.ylabel('Total Transmission Time/s')
    plt.legend()
    plt.savefig('result_0.png')
    plt.show()
    with open('ry.npy', 'wb') as f:
        np.save(f, np.array(ry))
    
    with open('rx.npy', 'wb') as f:
        np.save(f, np.array(rx))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')

        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    