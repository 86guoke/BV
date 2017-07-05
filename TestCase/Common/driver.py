#__author__ = 'user'
#coding: utf-8
import time
from appium import webdriver
import os
#取最新下载下来的apk包名
path = 'E:\Android'
def compare(x, y):
    stat_x = os.stat(path + "/" + x)
    stat_y = os.stat(path + "/" + y)
    if stat_x.st_ctime < stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return 1
    else:
        return 0

iterms = os.listdir(path)
iterms.sort(compare)
apkname=iterms[-1]
print apkname
os.system('adb uninstall com.lubansoft.bimview4phone')
class drv:
        dc={}
        dc['platformName']='Android'
        dc['deviceName']='dcee06b38c7f'#192.168.76.101:5555  dcee06b38c7f
        dc['platformVersion']='6.0'
        dc['app'] ='E:/Android/%s'%apkname
        dc['appPackage']='com.lubansoft.bimview4phone'
        dc['appActivity']='com.lubansoft.bimview4phone.ui.activity.StartupActivity'  #com.tencent.mobileqq.activity.LoginActivity
        dc["unicodeKeyboard"] = "True"#两行代码 支持中文输入
        dc["resetKeyboard"] = "True"
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',dc)

        #点击有id的按钮
        def dianji(self,id):
                self.driver.find_element_by_id(id).click()




