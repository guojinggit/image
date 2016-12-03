# coding=utf-8
import log
from common.queue.queue_manager import *
from common.singleton.singleton import *
"""任务队列，主线程接收到消息后，都会都会放入此队列"""


class TaskQueue(Singleton, QueueManager):

    """使用单例，保证send_queue这个对象只有一个，但是里面可以有很多队列"""
    isInit = False

    def __init__(self, config=0):
        if not self.isInit:
            queuenum = config.getint("taskqueue", "queuenum")
            queueMaxSize = config.getint("taskqueue", "queueMaxSize")
            QueueManager.__init__(self, queuenum, queueMaxSize)
            self.isInit = True




