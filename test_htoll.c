#include <stdio.h>
#include <arpa/inet.h>

#define htonll(x) ((1==htonl(1)) ? (x) : ((uint64_t)htonl((x) & 0xFFFFFFFF) << 32) | htonl((x) >> 32))
#define ntohll(x) ((1==ntohl(1)) ? (x) : ((uint64_t)ntohl((x) & 0xFFFFFFFF) << 32) | ntohl((x) >> 32))


int main() {
    int test = 1;
    int test_endian = htonl(test);
    printf("network order of %i is: %i\n", test, test_endian);

    if (test==test_endian) {
        printf("Machine is Big Endian\n");
    } else {
        printf("Machine is little Endian\n");
    }

    long long nettest = 1;
    long long nettest_endian = htonll(nettest);
    printf("Converting long long %lld to network order: %lld\n", nettest, nettest_endian);
    long long local = ntohll(nettest_endian);
    printf("Converting long long network %lld to machine order: %lld\n", nettest_endian, local);

}