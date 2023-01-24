# COMP556 Project_1

PING/PONG server 

## Usage

On local Machine, open two terminals, run the following cmd respectivly:
```shell
./client_num localhost 1025 0 10
```
which follow the format: 
```shell
./client_num hostname portnumber data count
```
```shell
./server_num 1025
```
The two sockets connect over localhost IP(27.0.0.1) and port 1025 (change this if running on CLEAR)

## LOG

1/21: server is able to recieve and decode timestamp and message