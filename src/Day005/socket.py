#!/user/bin/env python
#encoding:utf-8

'''
什么是socket
    socket默认是基于TCP协议的
　　所谓socket通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，应用程序通常通过"套接字"向网络发出请求或者应答网络请求。
　　socket起源于Unix，而Unix/Linux基本哲学之一就是“一切皆文件”，都可以用“打开open –> 读写write/read –> 关闭close”模式来操作。
    Socket就是该模式的一个实现，socket即是一种特殊的文件，一些socket函数就是对其进行的操作（读/写IO、打开、关闭）
流程：服务端bind（绑定IP），listen（监听），accept（等待某个客户端接受），客户端连接之后，客户端和服务端就开始接数据、收数据各种交互操作
'''

import socket

def handle_request(client):
    buf = client.recv(1024)  
    client.send("HTTP/1.1 200 OK\r\n\r\n") #05 给某个客户端发消息，cilent是某个客户端
    client.send("Hello, world") #05 给客户端发消息

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',8080)) #02 监听地址和端口
    sock.listen(5)

    while True:
        connection, address = sock.accept() #03 接口客户端请求（等待）  07#断开之后继续等待下次的请求
        handle_request(connection) #04 登陆客户端，客户端输入请求，connection是客户端对象
        connection.close() #06 与客户端连接断开

if __name__ == '__main__': #01 如果是主函数，执行main函数
    main()
    
    