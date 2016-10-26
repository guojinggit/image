# coding=utf-8

# 对消息进行打包，功能是构建数据的body,并不是一条完整的数据(缺少header)

import log


class Pack():

    body = b''

    def pack(self, data):
        data_length = len(data)
        self.push(data_length, data)

    def push(self, data_length, data):
        if data_length > 9999:
            log.info("data is too long")
            raise
        # 存4字节长度,不够用0补充
        byte_length = b'%04d' % data_length
        self.body = self.body + byte_length + data






