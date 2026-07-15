import socket

s = socket.socket()
s.bind(('localhost', 8080))
s.listen(1)
print("Web Server running... Go to http://localhost:8080")

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    print("\n--- Request --- \n", request)
    
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>Hello from Python Web Server!</h1>"
    conn.send(response.encode())
    conn.close()