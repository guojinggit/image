# coding=utf-8

# 22字节协议头定义

class Header():
    header = b''
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

    def set_uri(self, uri):
        self.uri = b'%02d' % uri

    def set_body_length(self, body_length):
        self.body_length = b'%08d' % body_length

    def set_password(self, password):
        self.password = password

    def set_status(self, status):
        self.status = b'%02d' % status

    def set_reserve(self, reserve):
        self.reserve = b'%04d' % reserve



