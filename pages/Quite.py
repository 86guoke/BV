#__author__ = 'user'
#coding: utf-8
import unittest,time
import Common
from appium import webdriver

class Quite(unittest.TestCase):

    #driver = webdriver.Remote('http://localhost:4723/wd/hub', Common.common.dc)
    def setUp(self):
        self.s=Common.common
        self.driver=self.s.driver
        print "21312"
        print "start"
    #注销登录
    def test_5quit(self):
        u'''注销'''
        #点击我的
        self.dianji("com.lubansoft.bimview4phone:id/tv_setting")
        # print w,h,h/2
        # self.driver.swipe(w,h,w,h/2,1000)
        # time.sleep(1)
        #点击设置
        self.driver.find_element_by_name("设置").click()
        time.sleep(1)
        #点击注销登录
        self.driver.find_element_by_name("注销账号").click()
        self.driver.get_screenshot_as_file(u"E:\\Android\\注销成功.png")
        #判断是否注销成功
        self.assertEqual(".ui.activity.LoginActivity",self.driver.current_activity,u"注销失败")




    #点击有id的按钮
    def dianji(self,id):
        self.driver.find_element_by_id(id).click()



if __name__ == "__main__":
    pass