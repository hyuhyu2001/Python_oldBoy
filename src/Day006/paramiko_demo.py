#!/user/bin/env python
#encoding:utf-8

'''
主机的批量管理
'''

import paramiko

#用用户名和密码连接
ssh = paramiko.SSHClient() #实例化SSH
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #第一次连接远程服务器，做一个签名，在SSH下生成key
ssh.connect('localhost', 22, 'admin', '123') #机器、端口号、用户名、密码
stdin, stdout, stderr = ssh.exec_command('df') #输入命令
print stdout.read()
ssh.close()

'''
SSH传输：认证过程是加密的，但是认证后再进行传输默认不加密的
RSA公钥加密算法:
用公钥和私钥,秘钥比密码更安全：秘钥是私有的，是用来解密的；公钥是用来加密的
非对称加密协议：当我想把消息发给aa时，不想被其他人截获和加密，我和aa约定一个公钥，aa想收我的消息时，aa需要把公钥发给我，我解密了发给aa
认证只针对这次登陆：这次认证发12345，下次认证随机发其他数，已经截获的12345已经失效【除非会话劫持，拦截返回的数据】
通过SSH连接服务器
登陆chenchao机器，通过ssh-keygen命令产生密钥对（公钥和私钥），需要把我的公钥copy到chenchao的机器上
ssh-keygen -t rsa
ssh-copy-id -i ~/ssh/id_rsa.pub wupeiqi@192.168.159.129
'''
import paramiko

private_key_path = '/home/auto/.ssh/id_rsa' #声明自己的私钥在哪里
key = paramiko.RSAKey.from_private_key_file(private_key_path) #拿着我的私钥

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('182.92.219.96 ', 22, username = 'alex',pkey = key) #需要写用户名，不需要写密码,用key登陆

stdin, stdout, stderr = ssh.exec_command('df')
print stdout.read()
ssh.close()

#上传和下载文件
import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',password='WOshiniba8')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test.py','/tmp/test.py') 
t.close()


import os,sys
import paramiko

t = paramiko.Transport(('182.92.219.86',22))
t.connect(username='wupeiqi',password='WOshiniba8')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test.py','/tmp/test2.py')
t.close()

