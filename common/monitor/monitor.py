# coding=utf-8



class EpollMonitor:

    def __init__(self, epoll):
        self.epoll = epoll

    def getsize_fd_map_handler(self):
        return len(self.epoll.fd_map_handler)


class QueueMonitor:

    def set_taskqueue(self, taskqueue):
        self.taskqueue = taskqueue

    def set_sendqueue(self, sendqueue):
        self.sendqueue = sendqueue

    def getsize_taskqueue(self):
        return self.taskqueue.size()

    def getsize_sendqueue(self):
        return self.sendqueue.size()


class Monitor:

    def set_EpollMonitor(self, epollMonitor):
        self.epollMonitor = epollMonitor

    def set_QueueMonitor(self, queueMonitor):
        self.queueMonitor = queueMonitor

    def show(self):
        print "sizeof epoll fd_map_handler:", self.epollMonitor.getsize_fd_map_handler()
        print "sizeof taskqueue:", self.queueMonitor.getsize_taskqueue()
        print "sizeof sendqueue,", self.queueMonitor.getsize_sendqueue()


