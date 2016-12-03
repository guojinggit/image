# coding=utf-8

import threading

from common.queue.taskQueue import *
from common.env.env import *

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

    def start(self):
        t = threading.Thread(target=self.worker)
        t.start()


class Threads:

    def __init__(self, config):
        queueindex = 0
        threadnum = config.getint("theadpool", "theadnum")
        self.threads = []
        for index in range(0, threadnum):
            m_thread = Thread()
            m_thread.init(index+1, queueindex)
            self.threads.append(m_thread)

    def start(self):
        for m_thread in self.threads:
            m_thread.start()

