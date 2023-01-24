#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <sys/time.h>

/* simple client, takes two parameters, the server domain name,
   and the server port number */

int main(int argc, char **argv)
{

  /* our client socket */
  int sock;

  /* variables for identifying the server */
  unsigned int server_addr;
  struct sockaddr_in sin;
  struct addrinfo *getaddrinfo_result, hints;

  /* convert server domain name to IP address */
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_family = AF_INET; /* indicates we want IPv4 */

  if (getaddrinfo(argv[1], NULL, &hints, &getaddrinfo_result) == 0)
  {
    server_addr = (unsigned int)((struct sockaddr_in *)(getaddrinfo_result->ai_addr))->sin_addr.s_addr;
    freeaddrinfo(getaddrinfo_result);
  }


  /* server port number */
  unsigned short server_port = atoi(argv[2]);
  /* Number of exchange */
  int msgSize = atoi(argv[3]);
  /* Count number of message exchange*/
  int count = atoi(argv[4]);

  char *buffer, *sendbuffer;
  int size = 500;

  /* allocate a memory buffer in the heap */
  /* putting a buffer on the stack like:

         char buffer[500];

     leaves the potential for
     buffer overflow vulnerability */
  buffer = (char *)malloc(size);
  if (!buffer)
  {
    perror("failed to allocated buffer");
    abort();
  }

  sendbuffer = (char *)malloc(size);
  if (!sendbuffer)
  {
    perror("failed to allocated sendbuffer");
    abort();
  }

  /* create a socket */
  if ((sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
  {
    perror("opening TCP socket");
    abort();
  }

  /* fill in the server's address */
  memset(&sin, 0, sizeof(sin));
  sin.sin_family = AF_INET;
  sin.sin_addr.s_addr = server_addr;
  sin.sin_port = htons(server_port);

  /* connect to the server */
  if (connect(sock, (struct sockaddr *)&sin, sizeof(sin)) < 0)
  {
    perror("connect to server failed");
    abort();
  }

  /* everything looks good, since we are expecting a
     message from the server in this example, let's try receiving a
     message from the socket. this call will block until some data
     has been received */
  count = recv(sock, buffer, size, 0);
  if (count < 0)
  {
    perror("receive failure");
    abort();
  }

  /* in this simple example, the message is a string,
     we expect the last byte of the string to be 0, i.e. end of string */
  if (buffer[count - 1] != 0)
  {
    /* In general, TCP recv can return any number of bytes, not
 necessarily forming a complete message, so you need to
 parse the input to see if a complete message has been received.
       if not, more calls to recv is needed to get a complete message.
    */
    printf("Message incomplete, something is still being transmitted\n");
  }
  else
  {
    printf("Here is what we got: %s", buffer);
  }

  struct timeval current_time;

  for (int i = 0; i < count; ++i) {

    /* first byte of the sendbuffer is used to describe the number of
       bytes used to encode a number, the number value follows the first
       byte */

    // tv_sec (8B) + tv_usec (8B)
    // use short (2B) for size
    *(short *)sendbuffer = 16;
    long long* timestampPtr = (long long *)((short *)sendbuffer+1);

    // we choose to send int 
    *(short*)sendbuffer += 4;

    // add timestamp to buffer
    gettimeofday(&current_time, NULL);
    *timestampPtr = (long long) current_time.tv_sec;
    *(timestampPtr+1) = (long long) current_time.tv_usec;
    int* dataPtr = (int *)(timestampPtr+2);

    //append data of our choice
    int num = 1;
    *(int *)(dataPtr) = (int)htonl(num);

    send(sock, sendbuffer, sendbuffer[0] + 2, 0);
  }
    close(sock);
    free(buffer);
    free(sendbuffer);
  return 0;
}
