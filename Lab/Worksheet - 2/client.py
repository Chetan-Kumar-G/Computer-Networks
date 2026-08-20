import socket
ip="127.0.0.1"
port=12345
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))
while True:
    msg=input("chetan2:")
    client.send(msg.encode())
    reply=client.recv(1024).decode()
    if (reply.lower() == "thank you"):
        print("Connection closed by server.")
        break
    print("chetan:",reply)
