import argparse
import subprocess
from scipy import stats
import matplotlib.pyplot as plt
import sys
import os
from tqdm import tqdm

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

def main():
    parser = argparse.ArgumentParser(description='Calcualte Network Delay')
    parser.add_argument('--m', type=int, help='Iteration for evaluate delay measure accuracy', default = 10)
    parser.add_argument('--n', type=int, help='Iteration for evaluate independent delay', default = 10)
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
        client_cmd = ['./client_num', 'localhost', '1025', f"{data_size}", "100"]
        subprocess.Popen(client_cmd, stdout=subprocess.DEVNULL).wait()
        allRRT = getRRT()
        avgLat = sum(allRRT)/len(allRRT)
        # print(f"Average Latency {avgLat} for data size {data_size}")
        latency_axis.append(avgLat)
        data_size_axis.append(data_size)

    # plt.scatter(data_size_axis, latency_axis)
    # plt.show()

    slope, intercept, r, p, std_err = stats.linregress(data_size_axis, latency_axis)
    regression_delay.append(intercept*1e3)
    print(f"Regression to {intercept*1e3}ms")

    plt.scatter(data_size_axis, latency_axis)
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
    