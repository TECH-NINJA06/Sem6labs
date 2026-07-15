import socket
import threading

def handle_client(conn, addr):
    request = conn.recv(1024).decode()
    print(f"[Thread {threading.get_ident()}] Handling request from {addr}")
    
    response = "HTTP/1.1 200 OK\n\nIntercepted by Python Multithreaded Proxy!"
    conn.send(response.encode())
    conn.close()

s = socket.socket()
s.bind(('localhost', 8888))
s.listen(5)
print("Proxy Server running on port 8888...")

while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()