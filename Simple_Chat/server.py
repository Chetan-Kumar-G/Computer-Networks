import socket

host = "0.0.0.0"
port = 12345

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
server.listen(1)

print("Waiting for Cynthia...")

conn,addr = server.accept()

print("connected to Cynthia")

while True:
    msg = conn.recv(1024).decode()
    if not msg:
        break
    print("Cynthia: ",msg)

    reply = input("Chetan: ")
    conn.send(reply.encode())
conn.close()
