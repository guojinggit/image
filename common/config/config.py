# coding=utf-8

import ConfigParser
from common.singleton.singleton import *


class Config():

    def init(self):
        return self.openpath("framework.conf")

    def read(self, path):
        self.config = ConfigParser.ConfigParser()
        return self.config.read(path)

    def openpath(self, path):
        self.read(path)
        return self.config



# config = Config()
# config.read("test.conf")
# print config.sections()
# print config.options("db")
# print config.items("db")
# print config.get("db", "db_host")


