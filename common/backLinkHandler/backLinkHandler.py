# coding=utf-8
import socket
import SocketServer as socketserver
import common.sock_pack.sock as MySock
import log
import send_data as sendData
import common.sock_pack.pack as pack
import common.queue.taskQueue as taskQueue

"""当主线程接收到数据的时候，将数据发给backLinkHandler"""

class BackLinkHandler(socketserver.BaseRequestHandler):

    def handle(self):
        mySock = MySock.MySock()
        data = mySock.mySockRead(self.request)
        log.info(data)
        pos = 0
       # 整理数据,主要是处理遇到粘包的情况，然后发给任务队列去处理
        while True:
            data = data[pos:]
            if len(data) < 22:
                break
            dataLength = 33       # 获取数据长度
            uri = 10
            if dataLength >= len(data) - 22:   # 说明该包是完整的，并且后面还有数据
                pos = dataLength + 22
                oneFullData = data[0:pos]                   # 获取一个完整的包
                # 然后还得找到对应的处理函数，一起封装好才能送入队列，这样子子线程就能直接处理
                taskQueue.TaskQueue(1, 10).getQueue(0).push(oneFullData)   # 将完整的消息报送入任务队列0
            else:
                log.info("数据不完成，果断退出")
                break

        log.info(taskQueue.TaskQueue(1,10).getQueue(0).pop())




class MyTCPServer(socketserver.TCPServer):

    def server_bind(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(0)  # 设置非阻塞，主线程无论如何不能堵
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

HOST, PORT = "localhost", 9999

server = MyTCPServer((HOST, PORT), BackLinkHandler)
server.serve_forever()