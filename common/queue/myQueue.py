# coding=utf-8

try:
    import Queue           # python2
except ImportError:
    import queue as Queue  # python3


"""封装queue"""

class MyQueue():

    queueIndex = 0  # 队列编号
    queueName = 0   # 队列名字
    queueSize = 0   # 队列长度

    def __init__(self, queueIndex, queueSize, queueName="queue"):
        self.queueIndex = queueIndex
        self.queueIndex = queueName
        self.queueSize = queueSize
        self.myQueue = Queue.Queue(queueSize)  # 创建队列

    def pop(self):
        return self.myQueue.get()

    def push(self, dataClass):
        self.myQueue.put(dataClass)

