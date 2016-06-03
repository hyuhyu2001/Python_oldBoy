#!/user/bin/env python
#encoding:utf-8

import socket

client = socket.socket()

ip_port = ('127.0.0.1','9999')
client.connect(ip_port) #连接端口

while True:#保证两个一直接收和发送
    data = client.recv(1024) #客户端接收数据
    inp= raw_input('client:')#客户端发送数据
    client.send(inp)
    if inp == 'exit':
        break
print data
