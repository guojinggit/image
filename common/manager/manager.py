# coding=utf-8

from common.epoll.epoll import *
from common.queue.sendQueue import *


class Manager(Handler):

    def __init__(self, config):
        self.config = config
        self.taskQueue = TaskQueue(self.config)
        self.sendQueue = SendQueue(self.config)

    def handle(self):
        while SendQueue().getQueue(0).size() > 0:
            SendQueue().getQueue(0).pop().sendmsg()
