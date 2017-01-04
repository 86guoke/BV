#__author__ = 'user'
#coding: utf-8
import time
from appium import webdriver
class drv:
        dc={}
        dc['platformName']='Android'
        dc['deviceName']='dcee06b38c7f'#192.168.76.101:5555  dcee06b38c7f
        dc['platformVersion']='6.0'
        dc['app'] ='E:/Android/bv_v4.0.0.11_20161223_141755.apk'
        dc['appPackage']='com.lubansoft.bimview4phone'
        dc['appActivity']='com.lubansoft.bimview4phone.ui.activity.StartupActivity'  #com.tencent.mobileqq.activity.LoginActivity
        dc["unicodeKeyboard"] = "True"#两行代码 支持中文输入
        dc["resetKeyboard"] = "True"
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',dc)

        #点击有id的按钮
        def dianji(self,id):
                self.driver.find_element_by_id(id).click()




