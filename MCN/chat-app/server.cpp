#include <iostream>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

using namespace std;

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);  

    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    
    listen(server_fd, 3);
    cout << "Waiting for client to connect..." << endl;
    
    int client_socket = accept(server_fd, NULL, NULL);
    cout << "Client connected!" << endl;

    char buffer[1024] = {0};
    string message;

    while(true) {
        memset(buffer, 0, 1024); 
        
        read(client_socket, buffer, 1024);
        cout << "Client: " << buffer << endl;
        
        cout << "Server: ";
        getline(cin, message);
        send(client_socket, message.c_str(), message.length(), 0);
    }
    
    close(server_fd);
    return 0;
}