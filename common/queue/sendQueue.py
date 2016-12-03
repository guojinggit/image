# coding=utf-8
import log
from common.queue.queue_manager import *
from common.singleton.singleton import *
"""发送消息的队列"""


class SendQueue(Singleton, QueueManager):

    isInit = False

    def __init__(self, config=0):
        if not self.isInit:
            queuenum = config.getint("sendqueue", "queuenum")
            queuemaxsize = config.getint("sendqueue", "queueMaxSize")
            QueueManager.__init__(self, queuenum, queuemaxsize)
            self.isInit = True






