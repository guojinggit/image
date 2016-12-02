from common.framework import *
from common.protocol.commonprotocol import *
from src.register import *

if __name__ == "__main__":
    framework = Framework()
    Entry().bind_uri(AppContext(), DaemonReq(), Register().on_register_msg)


    framework.start()

