# coding=utf-8

# 构建完整的发送内容，包含heaer和body

import header
import pack
import log

# 先继承Header,有了header
class Sender(header.Header):

    # new 一个pack,有了body
    my_pack = pack.Pack()

    # 主动调数据的pack_me函数
    def load(self, data_model_class):
        # 将打包的类传过去
        data_model_class.pack_me(self.my_pack)
        self.set_body_length(len(self.my_pack.body))
    def show_data(self):
        log.info(self.hself.my_pack.body)



