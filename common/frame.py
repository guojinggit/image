from common.epoll.epoll import *
from common.sock_connect.connect import *
from common.backLinkHandler.backLinkHandler import *

class Framework(Singleton):

    def __init__(self):
        self.init()

    def init(self):
        self.epoll = EpollServer()
        self.backLinkHandler = BackLinkHandler()
        self.tcpserver = TcpServer(('', 8444), Conn, self.backLinkHandler)
        self.epoll.register_with_handler(self.tcpserver)

    def start(self):
        self.epoll.server_forever()


framework = Framework()
framework.start()