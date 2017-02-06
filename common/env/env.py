# coding=utf-8


class Env:


    @classmethod
    def setThreadLocal(cls, threadlocal):
        cls.threadlocal = threadlocal

    @classmethod
    def getThreadLocal(cls):
        return cls.threadlocal

    @classmethod
    def setFramework(cls, framework):
        cls.framework = framework

    @classmethod
    def getFramework(cls):
        return cls.framework



