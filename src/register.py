import log
from common.task.taskbase import *
from common.protocol.commonprotocol import *
from common.queue.sendQueue import *
from common.thread.threads import *
from common.env.env import *

class Register():

    daemon_reg_edit = {}

    def on_register_msg(self, msg, conn):
        local = Env.getThreadLocal()
        print local.test
        reqtype = msg.reqtype
        dmsg = self.dmsg_from_msg(msg)
        if reqtype == "register":
            self.register(dmsg, conn)
        elif reqtype == "unregister":
            self.unregister(dmsg, conn)
        elif reqtype == "getlist":
            self.pushlist(dmsg, conn)

        self.show()

    def on_register_msg_rsp(self, msg, conn):
        print "msg from aliyun:", msg.rsp

    def register(self, dmsg, conn):
        if self.find_srvname(dmsg.name):
            is_repeat = False
            for dmsg_in_edit in self.daemon_reg_edit[dmsg.name]:
                if self.daemon_msg_is_equal(dmsg, dmsg_in_edit):
                    is_repeat = True
                    break
            if not is_repeat:
                self.insert_register_msg(dmsg)
        else:
            self.add_daemon_reg_edit(dmsg)
        msg = DaemonRsp()
        msg.rsp = "success"
        SendQueue().dispatchById(msg, conn)
        msg = DaemonReq()
        msg.reqtype = "getlist"
        SendQueue().dispatchByIp(msg, ("120.26.164.219", 8444))

    def unregister(self, dmsg, conn):
        if self.find_srvname(dmsg.name):
            isremove = False
            for dmsg_in_edit in self.daemon_reg_edit[dmsg.name]:
                if self.daemon_msg_is_equal(dmsg_in_edit, dmsg):
                    self.daemon_reg_edit[dmsg.name].remove(dmsg_in_edit)
                    isremove = True
                    break
            if not isremove:
                log.info("no info from table")
        else:
            log.info("no info from tabel")

    def pushlist(self, dmsg, conn):
        strlist = ""
        for key in self.daemon_reg_edit.keys():
            for msg in self.daemon_reg_edit[key]:
                strlist += self.msg_tostring(msg)
                strlist += "|"
        task = TaskBase()
        task.setConn(conn)
        msg = DaemonRsp()
        msg.init("success", strlist)
        pk = Pack(msg)
        task.setMessage(pk.get_data())
        SendQueue().getQueue(0).push(task)

    def dmsg_from_msg(self, msg):
        dmsg = DaemonMsg()
        dmsg.name = msg.name
        dmsg.ip = msg.ip
        dmsg.port = msg.port
        dmsg.group = msg.group
        dmsg.remark = msg.remark
        return dmsg

    def add_daemon_reg_edit(self, msg):
        key = msg.name
        list = []
        list.append(msg)
        value = list
        self.daemon_reg_edit[key] = value

    def insert_register_msg(self, msg):
        self.daemon_reg_edit[msg.name].append(msg)

    def find_srvname(self, srvname):
        if srvname in self.daemon_reg_edit.keys():
            return True
        else:
            return False

    def daemon_msg_is_equal(self,msg1, msg2):
        if (msg1.name == msg2.name) and (msg1.ip == msg2.ip)  \
                and (msg1.port == msg2.port) and (msg1.group == msg2.group) and (msg1.remark == msg2.remark):
            return True
        else:
            return False

    def msg_tostring(self, msg):
        msgstr = msg.name +" " + msg.ip + " " + \
              msg.port+ " " + msg.group + " " + msg.remark + " "
        return msgstr
    def show(self):
        for key in self.daemon_reg_edit.keys():
            print "srvname:", key
            for msg in self.daemon_reg_edit[key]:
                self.show_msg(msg)


    def show_msg(self, msg):
        print msg.name,msg.ip,msg.port,msg.group,msg.remark


class DaemonMsg():

    def __int__(self):
        self.name = ""
        self.ip = ""
        self.port = ""
        self.group = ""
        self.remark = ""