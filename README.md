# COMP556 Project_1

PING/PONG server 

## Usage

On local Machine, open two terminals, run the following cmd respectivly:
```shell
./client_num localhost 1025 18 10
```
which follow the format: 
```shell
./client_num hostname portnumber data(18 <= size <= 65535) count
```
```shell
./server_num 1025
```
The two sockets connect over localhost IP(27.0.0.1) and port 1025 (change this if running on CLEAR)

## Latency Model Evaluation
To evaluation the performance and accuracy of our model, we first test it on localhost with simulated latency using the linux `tc` tool.
On local Machine, simulate network latency on localhost using:
```shell
sudo tc qdisc add dev lo root netem delay 100ms
```
Delete restriction:
```shell
sudo tc qdisc del dev lo root
```
The above commands are integrated into the testing script. First start server program, then run `Stats_gen_test.py` to evaluate model.

## Latency Measurement on CLEAR server
Run `Stats_gen.py` to run model.

We measure the latency between ccnc-01 and ccnc-02, the result is approximate 0.05715ms

Details can be seen in Report


## LOG

1/21: server is able to recieve and decode timestamp and message
2/8: Server is able finish All project

## Member

Jinlin Li (jl288@rice.edu)

Haochen Zhang (jz118@rice.edu)

Jiaqi He (jh166@rice.edu)

Ye Zhou (yz202@rice.edu)
