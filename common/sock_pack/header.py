# coding=utf-8

# 22字节协议头定义

class Header():
    header = [1] * 22
    # 数据长度,8字节
    body_length = b'00000000'
    # 消息编号uri,2字节
    uri = b'00'
    # 密码，6字节
    password = b'000000'
    # 状态，2字节
    status = b'00'
    # 保留，4字节
    reserve = b'0000'

    header = body_length + uri + password + status + reserve

    def set_body_length(self, body_length):
        self.header = b'%08d' % body_length + self.header[8:]

    def set_uri(self, uri):
        self.header = self.header[0:8] + b'%02d' % uri + self.header[10:]

    def set_password(self, password):
        self.header = self.header[0:10] + password + self.header[16:]

    def set_status(self, status):
        self.header = self.header[0:16] + b'%02d' % status + self.header[18:]

    def set_reserve(self, reserve):
        self.header = self.header[0:18] + b'%04d' % reserve



