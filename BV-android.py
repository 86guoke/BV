#__author__ = 'user'
#-*-coding:utf-8-*-
import unittest,time
import HTMLTestRunner,ToEmail
# import socket
# import time
# timeout = 20
# socket.setdefaulttimeout(timeout)
from TestCase import *
#timestr = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
print timestr
if __name__ == "__main__":
    deviceId = 'dcee06b38c7f'
    # subprocess.Popen("adb uninstall com.lubansoft.bimview4phone")
    # appiumServer = subprocess.Popen("appium -U%s --no-reset"%deviceId,shell=True)
    # time.sleep(5)
    #os.system('adb uninstall com.lubansoft.bimview4phone')
    # os.system("appium -a 127.0.0.1 -p 4723 –U  dcee06b38c7f  --no-reset")
    testunit=unittest.TestSuite()        #定义一个单元测试容器

    try:
        #登录
        testunit.addTest(unittest.makeSuite(Login.Login))#将测试用例加入到测试容器中

        #工程
        testunit.addTest(unittest.makeSuite(Project.Project))

        #工程资料
        testunit.addTest(unittest.makeSuite(ProjectMaterial.ProjectMaterial))

        #创建协作
        testunit.addTest(unittest.makeSuite(CreateTheme.CreateTheme))

        #意见反馈
        testunit.addTest(unittest.makeSuite(Opintion.Opinion))

        #动态搜索
        testunit.addTest(unittest.makeSuite(Moving.Moving))

        #退出
        testunit.addTest(unittest.makeSuite(Quit.Quite))
    except Exception as e:
        print e
    finally:
        #filename="Report\\%s.html"%timestr        #定义个报告存放路径，支持相对路径。
        filename="Report\\bv.html"        #定义个报告存放路径，支持相对路径。
        fp=file(filename,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
        runner.run(testunit)                 #自动进行测试
        fp.close()
        #ToEmail.sendmail(timestr)            #发送自动化测试报告
        #os.system('taskkill /f /im node.exe')
        os.system('adb uninstall com.lubansoft.bimview4phone')
