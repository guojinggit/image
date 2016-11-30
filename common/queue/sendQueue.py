# coding=utf-8
import log
from common.queue.queue_manager import *
from common.singleton.singleton import *
"""发送消息的队列"""


class SendQueue(Singleton, QueueManager):

    isInit = False

    def __init__(self, queueNum=0, queueSize=0):
       if not self.isInit:
            QueueManager.__init__(self, queueNum, queueSize)
            self.isInit = True






