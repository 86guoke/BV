#__author__ = 'user'
#coding: utf-8
import os
from ftplib import FTP
if __name__ == "__main__":
    ftp_server = '192.168.2.244'#服务器地址
    username = 'bvandroid'  #用户名 bvandroid
    password = 'bvandroid'  #密码
    address="/bv/setup/v4.2.0"#下载地址 /bv/setup/v4.2.0
    ftp=FTP()
    #ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
    ftp.connect(ftp_server,21) #连接
    ftp.login(username,password) #登录，如果匿名登录则用空串代替即可
    ftp.cwd(address)                #进入远程目录
    print "---------------------------"
    ApkName=ftp.nlst()          #获取目录下所有文件
    print ApkName[1][-3:]
    print ApkName[1].split('_')
    print ApkName[1].split('_')[1].split('.')[-1]
    li=[]
    for i in ApkName:
        if i[-3:]=="exe":
            li.append(0)
        else:
            li.append(int(i.split('_')[1].split('.')[-1]))
    print li
    print max(li)
    print li.index(max(li))
    name=ApkName[li.index(max(li))]

    #判断文件是否存在
    path = 'E:\Android'
    dirs = os.listdir(path)
    if name in dirs:
        print u"没有最新的文件"
        assert True
    else:
        #下载FTP文件
        print "++++++++++++++++++++++++++++++"
        apk=address+"/"+name
        file_handle=open("E://Android//%s"%name,"wb") #以写模式在本地打开文件
        ftp.retrbinary("RETR"+apk,file_handle.write,1024)  #下载FTP文件
        print "---------------------------------------"
        print u"下载成功",name
        ftp.close()
        assert False