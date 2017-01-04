#__author__ = 'user'
#coding: utf-8
from Common import *
import unittest
import time
class Quite(unittest.TestCase):
    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        # 调用公用方法
        self.c = common.common()

    #注销登录
    def test_5quit(self):
        u'''注销'''
        #点击我的
        self.c.dianji("com.lubansoft.bimview4phone:id/tv_setting")
        #点击设置
        self.driver.find_element_by_name("设置").click()
        time.sleep(1)
        #点击注销登录
        self.driver.find_element_by_name("注销账号").click()
        self.driver.get_screenshot_as_file(u"E:\\Android\\注销成功.png")
        #判断是否注销成功
        self.assertEqual(".ui.activity.LoginActivity",self.driver.current_activity,u"注销失败")



    def tearDown(self):
        tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        print "end"
