# encoding=utf-8

import select
import socket

"""
	按照解耦的设计思想
	EpollServer只提供注册信号接口，当信号触发后，主动调用注册对象的handle的方法，EpollServer使命完成，周而复始
"""

class EpollServer():

    timeout = 1
    fd_map_handler={}

    def __init__(self):
        self.epoll = select.epoll()
        self.shutdown_request = False

    def server_forever(self):  # 需要主动调用。当此方法运行，epoll服务器正式运行
        try:
            while not self.shutdown_request:
                events = self.epoll.poll(self.timeout)
                for fd, event in events:
                    self.handle_request_noblock(fd, event)
        finally:
            self.shutdown_request = False

    def handle_request_noblock(self, fd, event):
        # 根据fd找到注册时传进来的对象
        handler = self.fd_map_handler[fd]
        # 注意，控制权已经交给注册时传的对象了，怎么处理信号，跟epoll已经没有关系了，是对象自己的事情
        handler.handle(fd, event)

    def register_with_handler(self, handler, eventmask=None):

        self.epoll.register(handler.getfd(), eventmask)
        # 本来在c++里是可以直接传event.data.ptr,这样就能直接回调，
        # 但是python不提供这个接口，所以自己建立一张表映射fd和handler
        self.fd_map_handler[handler.getfd()] = handler




class Handler:  # 需要被继承类，该类相当于一个规则，凡是想注册到epoll里去的类，都必须实现下面两个方法

    def getfd(self):
        pass

    def handle(self, fd, event):
        pass




class Socket(Handler):



    def create_and_bind(self):
        self.listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_fd.bind(('', 8444))
        self.listen_fd.listen(10)

    def getfd(self):
        return self.listen_fd.fileno()

    def handle(self, fd, event):
        if fd == self.listen_fd.fileno():
            conn, addr = self.listen_fd.accept()
            print("accept connection from %s, %d, fd = %d" % (addr[0], addr[1], conn.fileno()))

mysocket = Socket()
mysocket.create_and_bind()
epoll = EpollServer()
epoll.register_with_handler(mysocket, mysocket.getfd())
epoll.server_forever()
