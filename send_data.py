
import common.sock_pack.data_top as data_top
import log
import common.sock_pack.pack as pack

class Send_data(data_top.Data_top):


    def pack_me(self, m_packer):
        m_packer.pack("xx")
        m_packer.pack("good")
        m_packer.pack(123)

    def unpack_me(self, m_unpacker):
        self.data1 = m_unpacker.unpack()
        self.data2 = m_unpacker.unpack()
        self.data3 = m_unpacker.unpack()

# send_data = Send_data()
# packer = pack.Pack(send_data)
#
#
# log.info(packer.get_data())
#
# send_data1 = Send_data()
# unpacker = pack.Unpack(packer.get_data(), packer.get_length())
# unpacker.load(send_data1)
# log.info(send_data1.data2)






