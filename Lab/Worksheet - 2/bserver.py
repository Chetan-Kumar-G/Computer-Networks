import socket
host = "127.0.0.1"
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("Server is listening on port", port)
while True:
    conn, addr = server.accept()
    print("Connected to:", addr)
    message = conn.recv(1024).decode()
    print("Client:", message)
    conn.send("Message received".encode())
    conn.close()