

class TaskBase():

    uri = 0

    def setUri(self, uri):
        self.uri = uri
    def getUri(self):
        return self.uri

    def setProcFunc(self, callBackFunc):
        self.procFunc = callBackFunc

    def getProcFunc(self):
        return self.procFunc

    def setMessage(self, data):
        self.data = data

    def getMessage(self):
        return self.data

    def setConn(self, conn):
        self.conn = conn

    def getConn(self):
        return self.conn