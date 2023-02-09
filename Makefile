CC	 	= gcc
LD	 	= gcc
CFLAGS	 	= -Wall -g

LDFLAGS	 	= 
DEFS 	 	=

all:	server_num client_num stupid_client

server_num: server_num.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o server_num server_num.c

client_num: client_num.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o client_num client_num.c

stupid_client: stupid_client.c
	$(CC) $(DEFS) $(CFLAGS) $(LIB) -o stupid_client stupid_client.c

clean:
	rm -f *.o
	rm -f *~
	rm -f core.*.*
	rm -f server_num
	rm -f client_num
	rm -f stupid_client
