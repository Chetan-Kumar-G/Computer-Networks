import socket
ip="172.19.152.107"
port=12345
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))

while True:
    msg=input("cyn:")
    client.send(msg.encode())
    reply=client.recv(1024).decode()
    print("chetan:",reply)
