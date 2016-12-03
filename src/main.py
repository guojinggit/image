from common.framework.framework import *
from src.register import *

if __name__ == "__main__":
    framework = Framework_AN94
    Entry().bind_uri(AppContext(), DaemonReq(), Register().on_register_msg)
    framework.start()

