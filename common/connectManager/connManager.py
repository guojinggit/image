# coding=utf-8

from common.sock_connect.connect import *
from common.env.env import *

class ConnManager:


    def __init__(self):
        self.ip_port_map_conn = {}

    def addConn(self, conn):
        ip_port = conn.get_ip_port()
        if ip_port not in self.ip_port_map_conn.keys():
            self.ip_port_map_conn[ip_port] = conn

    def getConn(self, ip_port):
        if ip_port in self.ip_port_map_conn.keys():
            return self.ip_port_map_conn[ip_port]
        else:
            conn = ClientConn(ip_port, Env.framework.backLinkHandler)
            self.addConn(conn)
            return conn
