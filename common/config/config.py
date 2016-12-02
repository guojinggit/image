# coding=utf-8

import ConfigParser
from common.singleton.singleton import *


class Config(Singleton):

    def read(self, path):
        self.config = ConfigParser.ConfigParser()
        self.config.read(path)

    def sections(self):
        return self.config.sections()

    def options(self, name):
        return self.config.options(name)

    def items(self, name):
        return self.config.items(name)

    def get(self, section, option):
        return self.config.get(section, option)

    def getInt(self, section, option):
        return self.config.getint(section, option)

    def getfloat(self, section, option):
        return self.config.getfloat(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)



# config = Config()
# config.read("test.conf")
# print config.sections()
# print config.options("db")
# print config.items("db")
# print config.get("db", "db_host")


