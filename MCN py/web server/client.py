import socket
from concurrent.futures import ThreadPoolExecutor

HOST = "localhost"
PORT = 8888
REQUEST_COUNT = 5


def make_request(request_id):
    with socket.socket() as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n")
        response = client_socket.recv(1024).decode()
        print(f"Client {request_id}: {response.strip()}")


with ThreadPoolExecutor(max_workers=REQUEST_COUNT) as executor:
    for request_id in range(1, REQUEST_COUNT + 1):
        executor.submit(make_request, request_id)
