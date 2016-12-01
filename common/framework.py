# coding=utf-8

from common.epoll.epoll import *
from common.sock_connect.connect import *
from common.backLinkHandler.backLinkHandler import *
from common.appContext.appContext import *
from common.sock_pack.pack import *
from common.protocol.tespprotocol import *
from common.task.taskbase import *
from common.queue.sendQueue import *
from common.queue.taskQueue import *

def procTaskQueue(context):
    while True:
        task = taskQueue.TaskQueue().getQueue(0).pop()
        log.info("当前处理现场id号：" + str(thread.get_ident()))
        task.getProcFunc()(task.getMessage(), task.getConn())


def print_(message, conn):

    print (message.get_uri(), message.testdata1, message.testdata2)

    task = TaskBase()
    task.setConn(conn)
    msg = TestMessageRsp()
    pk = Pack(msg)
    task.setMessage(pk.get_data())
    SendQueue().getQueue(0).push(task)
    log.info(task.getMessage())
    print SendQueue().getQueue(0).size()


class Framework(Singleton):

    def __init__(self):
        self.init()

    def init(self):
        self.epoll = EpollServer()
        self.backLinkHandler = BackLinkHandler()
        self.tcpserver = TcpServer(('', 8444), Conn, self.backLinkHandler)
        self.epoll.register_with_handler(self.tcpserver)

        # init queue
        self.taskQueue = TaskQueue(1, 1000)
        self.sendQueue = SendQueue(1, 1000)

        # start threadpoll
        argList = [1]
        poolTask = threadpool.ThreadPool(2)
        requestsTask = threadpool.makeRequests(procTaskQueue, argList)
        [poolTask.putRequest(req) for req in requestsTask]

    def start(self):
        self.epoll.server_forever()



