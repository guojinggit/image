import common.sock_pack.sender
import common.sock_pack.data_top_super_class
import log

class Send_data(common.sock_pack.data_top_super_class.Data_top):
    data1 = "hello"
    data2 = "ok"
    data3 = 122

    def pack_me(self, pack):
        pack.pack(self.data1)
        pack.pack(self.data2)
        pack.pack(self.data3)

sender = common.sock_pack.sender.Sender()
send_data = Send_data()
sender.load(send_data)
sender.set_uri(21)
sender.set_password('522409')

sender.show_data()







