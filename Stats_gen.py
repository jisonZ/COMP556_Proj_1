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

    latency_axis = np.array(latency_axis)
    data_size_axis = np.array(data_size_axis)
    latency_mean = np.mean(latency_axis)
    latency_stddev = np.std(latency_axis)
    print(latency_stddev)
    print(latency_mean)
    x , y  = [] , []
    for i in range(len(latency_axis)):
        if np.abs(latency_axis[i] - latency_mean) < 2 * latency_stddev:
            y.append(latency_axis[i])
            x.append(data_size_axis[i])
        else:
            print("Remove " + str(latency_axis[i]))
    slope, intercept, r, p, std_err = stats.linregress(x,y)
    print(f"Regression to {intercept*1e3}ms")
    plt.scatter(x, y)
    plt.savefig('result.png')
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')

        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    