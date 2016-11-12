# coding=utf-8
import log
import queue_manager

"""任务队列，主线程接收到消息后，都会都会放入此队列"""

class TaskQueue(queue_manager.QueueManager):

    """使用单例，保证send_queue这个对象只有一个，但是里面可以有很多队列"""

    def __new__(cls, queue_num=0, queue_size=0):
        if not hasattr(cls, '_instance'):
            orig = super(TaskQueue, cls)
            cls._instance = orig.__new__(cls, queue_num, queue_size)
        return cls._instance
