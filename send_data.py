
import common.sock_pack.data_top_super_class
import log
import common.sock_pack.pack
class Send_data(common.sock_pack.data_top_super_class.Data_top):


    def pack_me(self, pack):
        pack.pack("xx")
        pack.pack("good")
        pack.pack(123)

    def unpack_me(self, unpack):
        self.data1 = unpack.unpack()
        self.data2 = unpack.unpack()
        self.data3 = unpack.unpack()

send_data = Send_data()
packer = common.sock_pack.pack.Pack(send_data)


log.info(packer.get_data())

send_data1 = Send_data()
unpacker = common.sock_pack.pack.Unpack(packer.get_data(), packer.get_length())
unpacker.load(send_data1)
log.info(send_data1.data2)






