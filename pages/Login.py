#__author__ = 'user'
#coding: utf-8
import unittest,time
import first,Common
from appium import webdriver
class Login(unittest.TestCase):

    #driver = webdriver.Remote('http://localhost:4723/wd/hub', Common.common.dc)
    def setUp(self):
        self.s=Common.common
        self.driver=self.s.driver
        print "21312"

    def test_login(self):
        u'''登录'''
        time.sleep(3)

        #输入用户名
        self.shuru("com.lubansoft.bimview4phone:id/account_edit_txt","haojinggang")
        #输入密码
        self.shuru("com.lubansoft.bimview4phone:id/pwd_edit_txt","111111")
        #点击设置
        self.dianji("com.lubansoft.bimview4phone:id/setting_btn")
        self.dianji("com.lubansoft.bimview4phone:id/clear_serveraddr_iv")
        #激活键盘
        self.activekeyboard(0)
        #输入服务器地址
        server=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/server_edit_txt")
        server.send_keys("192.168.13.200:8080/pds")
        #点击登录
        self.dianji("com.lubansoft.bimview4phone:id/login_btn")
        self.driver.get_screenshot_as_file("E:\\Android\\3.png")
        time.sleep(10)

        self.driver.wait_activity(".ui.activity.BVMainActivity",20,2)
        self.assertEqual(".ui.activity.BVMainActivity",self.driver.current_activity,u"登录失败")
        self.upgrade()
        self.tuijian()

     #关闭升级提示
    def upgrade(self):
        time.sleep(1)
        try:
            self.dianji("android:id/button2")
        except Exception as e:
            print e

    #关闭推荐项目部
    def tuijian(self):
        time.sleep(1)
        self.driver.get_screenshot_as_file("E:\\Android\\4.png")
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        w=int(x*0.35)
        h=int(y*0.8)
        try:
            self.driver.swipe(w,h,w,h,1)
            #self.dianji("com.lubansoft.bimview4phone:id/btn_recommend_dept_close")
        except Exception as e:
            print e


      #左滑
    def left(self,x1,y1,x2,y2,t):
        self.driver.swipe(x1,y1,x2,y2,t)
        time.sleep(1)

    #点击有id的按钮
    def dianji(self,id):
        self.driver.find_element_by_id(id).click()




    #滑动引导图
    def swippic(self):
        x1=int(x*0.95)
        y1=int(y*0.5)
        x2=int(x*0.05)
        print x,y,x1,y1,x2
        time.sleep(4)
        allow=self.driver.find_elements_by_id("com.huawei.systemmanager:id/btn_allow")
        if allow:
            allow[0].click()
        print "pic"+self.driver.current_activity
        self.left(x1,y1,x2,y1,1000)
        self.left(x1,y1,x2,y1,1000)
        self.left(x1,y1,x2,y1,1000)
        print "pic"+self.driver.current_activity
        self.driver.get_screenshot_as_file("E:\\Android\\1.png")
        #点击立即体验按钮
        self.driver.swipe(w,h,w,h,1)
        time.sleep(1)

    #输入框
    def shuru(self,id,content):
        self.driver.find_element_by_id(id).send_keys(content)
        time.sleep(2)

    def tearDown(self):
        print "tear"

    #激活键盘 0，1代表原始键盘，2代表appium键盘
    def activekeyboard(self,num):
        jianpan=self.driver.available_ime_engines
        # print jianpan
        # print jianpan[2]
        self.driver.activate_ime_engine(jianpan[num])
        time.sleep(2)












def run():
    print "hello"


if __name__ == "__main__":
    run()