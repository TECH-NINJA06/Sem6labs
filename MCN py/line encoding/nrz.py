import socket

s= socket.socket()
s.bind(('localhost', 8080))
s.listen(1)
conn, addr = s.accept()
print("Connected to client!\n")

conn.send("Enter binary string (e.g., 10110): ".encode())

while True:
    data = conn.recv(1024).decode()

    nrz_l = [1 if b == '1' else -1 for b in data]
    conn.send(str(nrz_l).encode())
    




