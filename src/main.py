from common.framework.framework import *
from src.register import *
from common.timer.timer import *



if __name__ == "__main__":
    framework = Framework_AN94
    framework.bind_uri(DaemonReq(), Register().on_register_msg)
    framework.start()

