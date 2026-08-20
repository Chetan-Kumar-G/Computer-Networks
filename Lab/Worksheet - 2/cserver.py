import socket
import threading
host = "127.0.0.1"
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("Server is running...")
def handle_client(conn, addr):
    print("Connected:", addr)
    message = conn.recv(1024).decode()
    print(f"{addr}: {message}")
    conn.send("Message received".encode())
    conn.close()
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()