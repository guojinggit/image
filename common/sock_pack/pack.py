# coding=utf-8

# 对消息进行打包，功能是构建数据的body,并不是一条完整的数据(缺少header)


import log
import header


class Pack(header.Header):

    body = b''

    def __init__(self, data_class):
        self.load(data_class)

    def load(self, data_class):
        """必须主动调用的方法，顺便将自己的对象传过去"""
        data_class.pack_me(self)
        self.set_body_length(len(self.body))

    def pack(self, data):
        """打包动作，在数据类内部调用"""
        if isinstance(data, int):
            data = b'%d' % data
        data_length = len(data)
        self.push(data_length, data)

    def push(self, data_length, data):
        if data_length > 99999999:
            log.info("data is too long")
            raise
        # 存8字节长度,不够用0补充
        byte_length = b'%08d' % data_length
        self.body = self.body + byte_length + data

    def get_data(self):
        return self.header + self.body

    def get_header(self):
        return self.header

    def get_body(self):
        return self.body

    def get_length(self):
        return len(self.header + self.body)

    def show_data(self):
        return self.get_data()

class Unpack():

    def __init__(self, data, length):
        self.data = data
        self.length = length

    # 表示数据长度的字节数
    num_data_length = 8
    pos = 22


    def load(self, data_class):
        data_class.unpack_me(self)

    def unpack(self):
        data_length = int(self.data[self.pos:self.pos + self.num_data_length])
        self.pos = self.pos + self.num_data_length + data_length
        return self.data[self.pos-data_length:self.pos]

    def get_header_length(self):
        return int(self.data[0:8])

    def get_header_uri(self):
        return int(self.data[8:10])

    def get_header_password(self):
        return self.data[10:16]

    def get_header_status(self):
        return int(self.data[16:18])

    def get_header_reserve(self):
        return self[18:22]






