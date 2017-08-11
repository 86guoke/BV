#__author__ = 'user'
#coding: utf-8
from Common import *
import os
import unittest,time
class Login(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_login(self):
        u'''登录'''
        try:
            if self.driver.current_activity==".ui.activity.NewFunctionNavigationActivity":
                self.c.swippic()
            else:
                #等待元素出现
                self.c.wait("com.huawei.systemmanager:id/btn_allow")
                allow=self.driver.find_elements_by_id("com.huawei.systemmanager:id/btn_allow")
                if allow:
                    allow[0].click()
        except Exception as e:
            print e
            raise Exception(e)

        #输入用户名
        #self.c.shuru("com.lubansoft.bimview4phone:id/account_edit_txt","haojinggang")
        #输入密码
        #self.c.shuru("com.lubansoft.bimview4phone:id/pwd_edit_txt","111111")
        #输入用户名密码，另外一种方式uitest
        for i in [49,49,37,48,33,47,48]:
            self.driver.find_element_by_id('com.lubansoft.bimview4phone:id/account_edit_txt').click()
            self.driver.press_keycode(i)

        for i in range(7):
            self.driver.find_element_by_id('com.lubansoft.bimview4phone:id/pwd_edit_txt').click()
            self.driver.press_keycode(8)


        #点击设置
        self.c.dianji("com.lubansoft.bimview4phone:id/setting_btn")
        self.c.dianji("com.lubansoft.bimview4phone:id/clear_serveraddr_iv")
        #激活键盘
        self.c.activekeyboard(0)
        #输入服务器地址
        server=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/server_edit_txt")
        server.send_keys("192.168.3.70:8080/pds")


        #点击登录
        self.c.dianji("com.lubansoft.bimview4phone:id/login_btn")
        self.driver.get_screenshot_as_file("E:\\Android\\3.png")

        self.driver.wait_activity(".ui.activity.BVMainActivity",20,2)
        self.assertEqual(".ui.activity.BVMainActivity",self.driver.current_activity,u"登录失败")
        self.upgrade()
        self.tuijian()
        #点击返回
        self.c.clickback(".ui.activity.BVMainActivity")


    #关闭升级提示
    def upgrade(self):
        try:
            #等待元素出现
            self.c.wait("android:id/button2")
            self.c.dianji("android:id/button2")
        except Exception as e:
            print e

    #关闭推荐项目部
    def tuijian(self):
        time.sleep(2)
        self.driver.get_screenshot_as_file("E:\\Android\\4.png")
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        w=int(x*0.35)
        h=int(y*0.8)
        try:
            self.driver.swipe(w,h,w,h,1)
            #self.dianji("com.lubansoft.bimview4phone:id/btn_recommend_dept_close")
            time.sleep(2)
        except Exception as e:
            print e



    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"
        self.c.screenshot(1)
