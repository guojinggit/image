# coding=utf-8

# 24字节协议头定义

class Header():

    # 协议起始头，占4字节，分别是assic:1,2,3,4
    header_begin = [1]*4
    for i in range(0, 4):
        header_begin[i] = i + 1
    # 发送方uri,占两字节
    uri_from = b'00'
    # 目的地uri,占两字节
    uri_to = b'00'
    # 数据长度,4字节
    body_length = b'0000'
    # 密码，6字节
    password = b'000000'
    # 状态，2字节
    status = b'00'
    # 保留，4字节
    reserve = b'0000'

    header = header_begin[0] + header_begin[1] + header_begin[2] + header_begin[3] \
             + uri_from + uri_to + body_length + status + reserve
    # 总共24字节
    def set_uri_from(self, uri_from):
        self.uri_from  = b'%02d' % uri_from

    def set_uri_to(self, uri_to):
        self.uri_to = b'%02d' % uri_to

    def set_body_length(self, body_length):
        self.body_length = b'%04d' % body_length

    def set_password(self, password):
        self.password = password

    def set_status(self, status):
        self.status = b'%02d' % status

    def set_reserve(self, reserve):
        self.reserve = b'%02d' % reserve

    def get_header(self):

