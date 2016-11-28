# encoding=utf-8

import select

import log

class EpollServer():

    timeout=1
    def __int__(self):
        self.epool = select.epoll()

    def serverForever(self):
        try:
            while not self.__shutdown_request:
                events = self.epoll.poll(self.timeout)
        finally:
            log.info("epoll")
