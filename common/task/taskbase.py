

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

    def setContext(self, data):
        self.data = data

    def getContext(self):
        return self.data