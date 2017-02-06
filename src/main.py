from common.framework.framework import *
from src.register import *


if __name__ == "__main__":
    framework = Framework_AN94
    framework.bind_uri(DaemonReq(), Register().on_register_msg)
    framework.bind_uri(DaemonRsp(), Register().on_register_msg_rsp)
    framework.start()

