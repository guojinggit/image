# coding=utf-8
import log
from common.task.taskbase import *
from common.sock_pack.pack import *
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

    def dispatchById(self, msg, conn):
        task = SendMsgTask()
        task.setConn(conn)
        task.sendtype = "sendById"
        pk = Pack(msg)
        task.setMessage(pk.get_data())
        SendQueue().getQueue(0).push(task)


    def dispatchByIp(self, msg, ip_port):
        task = SendMsgTask()
        task.sendtype = "sendByIp"
        task.set_ip_port(ip_port)
        pk = Pack(msg)
        task.setMessage(pk.get_data())
        SendQueue().getQueue(0).push(task)




