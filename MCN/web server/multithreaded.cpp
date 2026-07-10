#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <thread>

using namespace std;

void handle_client(int client_socket) {
    char buffer[1024] = {0};
    read(client_socket, buffer, 1024);
    
    cout << "Thread ID " << this_thread::get_id() << " handling request." << endl;
    
    string mock_response = "HTTP/1.1 200 OK\n\nIntercepted by Multithreaded Proxy!";
    send(client_socket, mock_response.c_str(), mock_response.length(), 0);
    
    close(client_socket);
}

int main() {
    int proxy_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8888); 

    bind(proxy_fd, (struct sockaddr*)&address, sizeof(address));
    listen(proxy_fd, 10);
    
    cout << "Multithreaded Proxy Server running on port 8888..." << endl;

    while(true) {
        int client = accept(proxy_fd, NULL, NULL);
        
        thread t(handle_client, client);

        t.detach(); 
    }
    
    return 0;
}