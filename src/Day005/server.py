#!/user/bin/env python
#encoding:utf-8

import socket

sk = socket.socket() #创建socket对象,socket模块里有socket类
ip_port = ('127.0.0.1','9999')
sk.bind(ip_port) #绑定IP
sk.listen(5) #监听

while True:
    conn,address = sk.accept() #接收请求，可以获取客户端的IP、端口和socket对象
    #sk.accept()为元组类型， ,result=sk.accept(),上述语句相当于conn = result[0],address=result[1]
    conn.send('hello')#给客户端发信息
    flag = True
    while flag:
        data = conn.recv(1024) #接收数据，最多只能拿1024字节
        print data
        if data == 'exit':
            flag = False
        else:
            conn.send('OK') #接收数据解答问题
    conn.close()  #关闭连接


#如何支持异步和多线程：处理多个请求的服务端（客户端不用变）
import SocketServer

class  MyServer(SocketServer.BaseRequestHandler): #继承了BaseRequestHandler类
    
    def setup(self):
        pass

    def handle(self): #定义handle方法
        print self.request,self.client_address,self.server
        conn = self.request
        conn.send('hello')#给客户端发信息
        flag = True
        while flag:
            data = conn.recv(1024) #接收数据，最多只能拿1024字节
            print data
            if data == 'exit':
                flag = False
            else:
                conn.send('OK') #接收数据解答问题
        conn.close()  #

    def finish(self):
        pass
        
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer) #接收两个参数（bind方法）
    server.serve_forever()
