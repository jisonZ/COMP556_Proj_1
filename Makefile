CC	 	= gcc
LD	 	= gcc
CFLAGS	 	= -Wall -g

LDFLAGS	 	= 
DEFS 	 	=

all:	server_num client_num name_addr test_htoll stupid_client

server_num: server_num.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o server_num server_num.c

client_num: client_num.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o client_num client_num.c

name_addr:	name_addr.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o name_addr name_addr.c

test_htoll: test_htoll.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o test_htoll test_htoll.c

stupid_client: stupid_client.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o stupid_client stupid_client.c

clean:
	rm -f *.o
	rm -f *~
	rm -f core.*.*
	rm -f server_num
	rm -f client_num
	rm -f name_addr
	rm -f test_htoll
	rm -f stupid_client
