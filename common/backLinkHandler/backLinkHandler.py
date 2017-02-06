# coding=utf-8
import socket
import log
import send_data as sendData
import common.sock_pack.pack as pack
import common.queue.taskQueue as taskQueue
from common.appContext.appContext import AppContext
from common.protocol.tespprotocol import *
import common.task.taskbase as taskBase
import common.thread.threadpool as threadpool
import thread
import common.queue.sendQueue as sendQueue
"""当主线程接收到数据的时候，将数据发给backLinkHandler"""


class BackLinkHandler():

    def handle(self, toatldata, totaldatasize, conn):
        pos = 0
        # 整理数据,主要是处理遇到粘包的情况，然后发给任务队列去处理
        while totaldatasize != 0:
            data = toatldata[pos:]
            if len(data) < 22:
                break
            datasize = int(data[0:8])       # 获取数据长度
            uri = int(data[8:10])
            if totaldatasize >= datasize + 22:   # 说明该包是完整的，并且后面还有数据
                pos = datasize + 22
                oneFullData = data[0:pos]                   # 获取一个完整的包
                totaldatasize = totaldatasize - pos

                # 然后还得找到对应的处理函数，一起封装好才能送入队列，这样子子线程就能直接处理
                entry = AppContext().getEntryByUri(uri)
                if entry != 0:
                    entry.handle_unpack(oneFullData, datasize+22)
                    task = taskBase.TaskBase()
                    task.setUri(uri)
                    task.setProcFunc(entry.callBackFunc)
                    task.setMessage(entry.messageClass)
                    task.setConn(conn)
                    taskQueue.TaskQueue().getQueue(0).push(task)   # 将完整的消息报送入任务队列0

            else:
                log.info("数据不完整，果断退出")
                break



# HOST, PORT = "localhost", 9999
# server = MyTCPServer((HOST, PORT), BackLinkHandler)
#
# poolSendTask = threadpool.ThreadPool(1)
# requestsSendTask = threadpool.makeRequests(procSendQueue, argList)
# [poolSendTask.putRequest(req) for req in requestsSendTask]
#
# server.serve_forever()