import socket
import time
import sys

HOST, PORT = "localhost", 8444
data ="000000331000000000000000000002xx00000004good00000003123"

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))
while True:
    # data = sys.stdin.readline()

    time.sleep(2)
    sock.send(data)
    print sock.recv(1024)
    while True:
        sock.send(data)
        print sock.recv(1024)
        time.sleep(2)
    break
    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))