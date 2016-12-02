# coding=utf-8
import sys
sys.path.append("..")

from common.epoll.epoll import *
from common.sock_connect.connect import *
from common.backLinkHandler.backLinkHandler import *
from common.appContext.appContext import *
from common.sock_pack.pack import *
from common.protocol.tespprotocol import *
from common.task.taskbase import *
from common.queue.sendQueue import *
from common.queue.taskQueue import *
from common.config.config import *
from common.mysql.mysql import *

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

        # init config
        self.config = Config()
        self.config.read("common/config/framework.conf")

        #init mysql
        self.mysql = Mysql()
        mysqlIp = self.config.get("mysql", "ip")
        mysqlPort = self.config.getInt("mysql", "port")
        mysqlUser = self.config.get("mysql", "user")
        mysqlPwd = self.config.get("mysql", "passwd")

        self.mysql.init(mysqlIp, mysqlPort, mysqlUser, mysqlPwd)

        # init epoll
        self.epoll = EpollServer()

        # init backlinkhandler
        self.backLinkHandler = BackLinkHandler()

        # init tcpserver
        IP = self.config.get("tcpserver", "ip")
        PORT = self.config.getInt("tcpserver","port")
        self.tcpserver = TcpServer((IP, PORT), Conn, self.backLinkHandler)
        self.epoll.register_with_handler(self.tcpserver)

        # init taskqueue
        queuenum = self.config.getInt("taskqueue", "queuenum")
        queueMaxSize = self.config.getInt("taskqueue", "queueMaxSize")
        self.taskQueue = TaskQueue(queuenum, queueMaxSize)

        # init sendqueue
        queuenum = self.config.getInt("sendqueue", "queuenum")
        queueMaxSize = self.config.getInt("sendqueue", "queueMaxSize")
        self.sendQueue = SendQueue(queuenum, queueMaxSize)

        # start threadpool
        theadnum = self.config.getInt("theadpool", "theadnum")
        argList=[]
        for i in range(0, theadnum):
            argList.append(i+1)
        poolTask = threadpool.ThreadPool(theadnum)
        requestsTask = threadpool.makeRequests(procTaskQueue, argList)
        [poolTask.putRequest(req) for req in requestsTask]

    def start(self):
        self.epoll.server_forever()



