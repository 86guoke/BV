#__author__ = 'user'
#-*-coding:utf-8-*-
import unittest,time
import HTMLTestRunner
import subprocess,os
from TestCase import *
timestr = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
if __name__ == "__main__":
    # deviceId = 'dcee06b38c7f'
    # subprocess.Popen("adb uninstall com.lubansoft.bimview4phone")
    # appiumServer = subprocess.Popen("appium -U%s --no-reset"%deviceId,shell=True)
    # time.sleep(5)

    testunit=unittest.TestSuite()        #定义一个单元测试容器

    #登录
    testunit.addTest(unittest.makeSuite(Login.Login))#将测试用例加入到测试容器中
    #创建协作
    testunit.addTest(unittest.makeSuite(CreateTheme.CreateTheme))
    #意见反馈
    testunit.addTest(unittest.makeSuite(Opintion.Opinion))
    #动态搜索
    testunit.addTest(unittest.makeSuite(Moving.Moving))
    #退出
    testunit.addTest(unittest.makeSuite(Quit.Quite))


    filename="Report\\%s.html"%timestr        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)                 #自动进行测试
    #os.system('taskkill /f /im node.exe')
    os.system('adb uninstall com.lubansoft.bimview4phone')