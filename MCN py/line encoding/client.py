import socket

s = socket.socket()
s.connect(('localhost', 8080))
print("Connected to server!\n")

init = s.recv(1024).decode()
print("Server:", init)

while True:
    msg = input("Client: ")
    s.send(msg.encode())
    print("Server:", s.recv(1024).decode())
    if msg.strip().lower() == 'exit':
        break

s.close()