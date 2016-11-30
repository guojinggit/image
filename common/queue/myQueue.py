# coding=utf-8

try:
    import Queue           # python2
except ImportError:
    import queue as Queue  # python3


"""封装queue"""

class MyQueue():


    def __init__(self, queueIndex, queueMaxSize, queueName="queue"):
        self.queueIndex = queueIndex
        self.queueIndex = queueName
        self.queueMaxSize = queueMaxSize
        self.myQueue = Queue.Queue(queueMaxSize)  # 创建队列

    def pop(self):
        return self.myQueue.get()

    def push(self, dataClass):
        self.myQueue.put(dataClass)

    def size(self):
        return self.myQueue.qsize()

