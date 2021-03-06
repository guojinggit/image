# ecoding=utf-8
import socket
import select
from common.epoll.epoll import *

"""总目标：作为一个连接器，负责socket的连接，发送，关闭等(维护一次连接,直至连接结束)"""


class Socket:

    def get_sock(self):
        return self.sock

    def set_sock(self, sock):
        self.sock = sock

    def create_tcpsock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def connect(self, ip_port):
        return self.sock.connect(ip_port)

    def listen(self, maxnum):
        self.sock.listen(maxnum)

    def bind(self, (ip, port)):
        self.sock.bind((ip, port))

    def read(self):
        self.fullData = ""
        while True:
            try:
                data = self.sock.recv(256)
                self.fullData = self.fullData + data
                if len(data) < 256:
                    break
            except:
                break
        return self.fullData

    def write(self, data):
        self.sock.send(data)

class Conn(Socket, SocketHandler):


    def sendbin(self, data):
        self.write(data)

    def getfd(self):
        return self.get_sock().fileno()

    def handle(self, fd, event):
        if event & select.EPOLLERR:
            self.close()
        elif event & select.EPOLLIN:
            try:
                data = self.read()
                if not data:
                    self.close()
                self.backLinkHander.handle(data, len(data), self)
            except socket.error:
                self.close()

    def get_ip_port(self):
        return self.ip_port


    def close(self):
        Epoll().unregister_with_handler(self)


class Tcpsock:
    pass

class ServerConn(Conn):

    def __init__(self, fd, address, backLinkHander):
        self.set_sock(fd)
        self.address = address
        self.ip_port = address
        self.backLinkHander = backLinkHander
        Epoll().register_with_handler(self)

class ClientConn(Conn):

    def __init__(self, ip_port, backLinkHander):
        self.create_tcpsock()
        self.connect(ip_port)
        self.ip_port = ip_port
        self.backLinkHander = backLinkHander
        Epoll().register_with_handler(self, select.EPOLLIN)



class TcpServer(SocketHandler):

    def __init__(self, config, conn, backLinHandler):
        ip = config.get("tcpserver", "ip")
        port = config.getint("tcpserver", "port")
        self.maxnum = 1024
        self.ConnClass = conn
        self.backLinHandler = backLinHandler
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ip, port))
        self.sock.listen(self.maxnum)

    def handle(self, fd, event):
        if event & select.EPOLLIN:
            fd, address = self.sock.accept()
            self.on_accept(fd, address)

    def on_accept(self, fd, address):
        self.ConnClass(fd, address, self.backLinHandler)

    def getfd(self):
        return self.sock.fileno()


