#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>

using namespace std;

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080); 

    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 3);
    
    cout << "Web Server running... Open browser and go to http://127.0.0.1:8080" << endl;

    while(true) {
        int client_socket = accept(server_fd, NULL, NULL);
        char buffer[2048] = {0};
        
        read(client_socket, buffer, 2048);
        cout << "\n--- Received Request ---\n" << buffer << endl;

        string http_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
                               "<html><body><h1>Hello from C++ Web Server!</h1></body></html>";
                               
        send(client_socket, http_response.c_str(), http_response.length(), 0);
        close(client_socket);
    }
    
    return 0;
}