# coding=utf-8

# 构建完整的发送内容，包含heaer和body

import header
import pack
import log


# 先继承Header,有了header,（感觉用继承不是那么好，组合应该要好点）
class Sender(header.Header):

    # new 一个pack,有了body
    my_pack = pack.Pack()

    # 主动调数据的pack_me函数
    def load(self, data_model_class):
        # 将打包的类传过去
        data_model_class.pack_me(self.my_pack)
        self.set_body_length(len(self.my_pack.body))

    def get_data(self):
        self.header = self.body_length + self.uri \
                     + self.password + self.status + self.reserve
        return self.header + self.my_pack.body

    def get_length(self):
        return len(self.header + self.my_pack.body)

    def show_data(self):
        log.info(self.get_data())



