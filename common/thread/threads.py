# coding=utf-8

import threading
import time
from common.queue.taskQueue import *
from common.env.env import *
from common.monitor.monitor import *
from common.queue.sendQueue import *
from common.queue.taskQueue import *
class Thread:

    def init(self, theadindex, queueindex):
            self.threadindex = theadindex
            self.queueindex = queueindex
            self.localval = Env.getThreadLocal()

    def worker(self):
        self.localval.test = self.threadindex
        while True:
            task = TaskQueue().getQueue(self.queueindex).pop()
            log.info("当前处理id号：" + str(self.threadindex))
            task.getProcFunc()(task.getMessage(), task.getConn())

    def monitor(self):
        print "monitor thread start"

        epollMonitor = EpollMonitor(Env.framework.epoll)
        queueMonitor = QueueMonitor()
        queueMonitor.set_taskqueue(TaskQueue().getQueue(0))
        queueMonitor.set_sendqueue(SendQueue().getQueue(0))

        monitor = Monitor()
        monitor.set_EpollMonitor(epollMonitor)
        monitor.set_QueueMonitor(queueMonitor)

        while True:
            time.sleep(2)
            monitor.show()



    def start(self, worker):
        t = threading.Thread(target=worker)
        t.start()


class Threads:

    def __init__(self, config):
        self.queueindex = 0
        self.threadnum = config.getint("theadpool", "theadnum")
        self.threads = []
        for index in range(0, self.threadnum):
            m_thread = Thread()
            m_thread.init(index+1, self.queueindex)
            self.threads.append(m_thread)

    def start(self):
        # start work thread
        for m_thread in self.threads:
            m_thread.start(m_thread.worker)
        # start monitor thread
        monitor_thread = Thread()
        monitor_thread.init(self.threadnum+1, self.queueindex)
        monitor_thread.start(monitor_thread.monitor)


