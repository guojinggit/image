# coding=utf-8

import queue_manager.py

class Send_queue(queue_manager.Queue_manager):

    """使用单例，保证send_queue这个对象只有一个，但是里面可以有很多队列"""

    def __new__(cls, queue_num, queue_size):
        if not hasattr(cls, '_instance'):
            orig = super(Send_queue, cls)
            cls._instance = orig.__new__(cls, queue_num, queue_size)
        return cls._instance

send_queue = Send_queue()
