# coding=utf-8
import log
import queue_manager
import common.singleton.singleton as singleton
"""发送消息的队列"""

class SendQueue(singleton.Singleton, queue_manager.QueueManager):

   def __init__(self, queueIndex=0, queueSize=0):
       queue_manager.QueueManager.__init__(self,queueIndex,queueSize)



