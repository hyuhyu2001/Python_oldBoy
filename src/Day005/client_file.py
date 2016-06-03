#!/user/bin/env python
#encoding:utf-8


'''
FTP文件上传
'''

import socket
import sys
import os

ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.connect(ip_port)

container = {'key':'','data':''}
while True:
    input = raw_input('path:')
    cmd,path = input.split('|') #cmd put是上传数据，get是下载数据，定义的两个参数
    file_name = os.path.basename(path)#获取文件名
    file_size=os.stat(path).st_size #获取文件大小，有大文件要分批发，服务端一般收一次，存一次（分10次发）；IO速度比内存慢很多
    sk.send(cmd+"|"+file_name+'|'+str(file_size))
    send_size = 0
    f= file(path,'rb')
    Flag = True
    while Flag:
        if send_size + 1024 >file_size:
            data = f.read(file_size-send_size)
            Flag = False #False时表示已发完
        else:
            data = f.read(1024)
            send_size+=1024
        sk.send(data)
    f.close()
    
sk.close()