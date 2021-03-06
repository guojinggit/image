# encoding=utf-8

import select
import socket
from common.singleton.singleton import *
from common.queue.taskQueue import *
from common.queue.sendQueue import *
from common.task.taskbase import *

"""
	按照解耦的设计思想
	EpollServer只提供注册信号接口，当信号触发后，主动调用注册对象的handle的方法，EpollServer使命完成，周而复始
"""


class Epoll(Singleton):

    isInit = False

    def __init__(self):
        if not self.isInit:
            self.timeout = 1
            self.fd_map_handler = {}
            self.epoll = select.epoll()
            self.shutdown_request = False
            self.isInit = True
            self.handlers = []

    def server_forever(self):  # 需要主动调用。当此方法运行，epoll服务器正式运行
        try:
            while not self.shutdown_request:
                events = self.epoll.poll(self.timeout)
                for fd, event in events:
                    print fd, event
                    self.handle_request_noblock(fd, event)
                self.do_handle()
        finally:
            self.shutdown_request = False

    def handle_request_noblock(self, fd, event):
        # 根据fd找到注册时传进来的对象
        handler = self.fd_map_handler[fd]
        # 注意，控制权已经交给注册时传的对象了，怎么处理信号，跟epoll已经没有关系了，是对象自己的事情
        handler.handle(fd, event)

    def register_with_handler(self, handler, eventmask=select.EPOLLIN):

        self.epoll.register(handler.getfd(), eventmask)
        # 本来在c++里是可以直接传event.data.ptr,这样就能直接回调，
        # 但是python不提供这个接口，所以自己建立一张表映射fd和handler
        self.fd_map_handler[handler.getfd()] = handler

    def modify_with_hanler(self, handler, eventmask):
        self.epoll.modify(handler.getfd(), eventmask)

    def unregister_with_handler(self, handler):
        try:
            self.epoll.unregister(handler.getfd())
            self.fd_map_handler.pop(handler.getfd())
        except IOError:
            print "IOERROR"

    def add_handler(self, handler):
        self.handlers.append(handler)

    def do_handle(self):
        for handler in self.handlers:
            handler.handle()



class Handler:  # 需要被继承类，该类相当于一个规则，凡是想注册到epoll里去的类，都必须实现下面两个方法

    def handle(self, fd, event):
        pass


class SocketHandler(Handler):

    def getfd(self):
        pass


class Socket(SocketHandler):


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

