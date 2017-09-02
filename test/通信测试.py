#!/usr/bin/python
#coding:utf8
'for my av'
__author__ = 'Hippo'

import socket
import threading
import time
import struct

def udp_recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 2001))
    while True:
        data, addr = s.recvfrom(1024)
        print data,addr
    s.close()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        data = sock.recv(1024)
        print len(data)
        pad = "!"
        for i in range(0,len(data)):
            pad += 'B'
        ret = struct.unpack(pad,data)
        print ret

threading.Thread(target=udp_recv, name='LoopThread').start()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2001))
s.listen(5)
while True:
    sock, addr = s.accept()
    threading.Thread(target=tcplink, args=(sock, addr)).start()
