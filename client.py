import socket
import time
import sys

HOST, PORT = "localhost", 8444
#HOST, PORT = "120.26.164.219", 8444
data ="000000331000000000000000000002xx00000004good00000003123"
registerx = "000000742000000000000000000008register00000004test00000009127.0.0.100000004888400000001x00000000"
registery = "000000742000000000000000000008register00000004test00000009127.0.0.100000004888400000001y00000000"
unregister = "000000762000000000000000000010unregister00000004test00000009127.0.0.100000004888400000001x00000000"
getlist = "000000692000000000000000000007getlist00000009127.0.0.100000004844400000001x0000000000000000"
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))
while True:
    # data = sys.stdin.readline()

    # time.sleep(2)
    # sock.send(register)
    # print sock.recv(1024)
    while True:
        sock.send(registerx)
        print sock.recv(1024)
        time.sleep(2)
    break
    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))