#include <iostream>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

using namespace std;

int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    
    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(8080);
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1"); 

    connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
    cout << "Connected to the chat server!" << endl;

    char buffer[1024] = {0};
    string message;

    while(true) {
        cout << "Client: ";
        getline(cin, message);
        send(sock, message.c_str(), message.length(), 0);
        
        memset(buffer, 0, 1024);
        
        read(sock, buffer, 1024);
        cout << "Server: " << buffer << endl;
    }
    
    close(sock);
    return 0;
}