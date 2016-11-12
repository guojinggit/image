# coding=utf-8

import log

class MySock():

    def mySockRead(self, sock):
        self.fullData = ""
        while True:
            try:
                data = sock.recv(256)
                self.fullData = self.fullData + data
                if len(data) < 256:
                    break
            except:
                log.info("未正确读到有效数据，返回空")
                break
        return self.fullData

    def mySockWrite(self, sock, data):
        sock.send(data)