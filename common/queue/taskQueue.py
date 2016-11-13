# coding=utf-8
import log
import queue_manager
import common.singleton.singleton as singleton
"""任务队列，主线程接收到消息后，都会都会放入此队列"""


class TaskQueue(singleton.Singleton, queue_manager.QueueManager):

    """使用单例，保证send_queue这个对象只有一个，但是里面可以有很多队列"""

    def __init__(self, queueIndex=0, queueSize=0):
        queue_manager.QueueManager.__init__(self, queueIndex, queueSize)

