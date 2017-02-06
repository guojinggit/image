# coding=utf-8
import myQueue
import log

"""作为队列管理者，创建队列和对外提供队列索引"""


class QueueManager():

    def __init__(self, queueNum, queueSize):
        self.myQueues = []
        for index in range(0, queueNum):
            self.myQueues.append(myQueue.MyQueue(index, queueSize))

    def getQueue(self, index=0):
        return self.myQueues[0] if index > len(self.myQueues) - 1 else self.myQueues[index]

