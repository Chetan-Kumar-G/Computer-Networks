import socket

hostname = "www.google.com"
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP Address:", ip_address)