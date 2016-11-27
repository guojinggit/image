from common.epoll.epoll import *
from common.sock_connect.connect import *


class Framework(Singleton):

    def __init__(self):
        self.init()

    def init(self):
        self.epoll = EpollServer()
        self.tcpserver = TcpServer(('', 8444), Conn)
        self.epoll.register_with_handler(self.tcpserver)

    def start(self):
        self.epoll.server_forever()


framework = Framework()
framework.start()