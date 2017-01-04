#__author__ = 'user'
#-*-coding:utf-8-*-
import time
from appium import webdriver
import unittest
import HTMLTestRunner


timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
driver=None
#选择设备
class shouji(unittest.TestCase):

    global driver
    #连接设备
    @classmethod
    def setUpClass(cls):
        global dc

        dc={}
        dc['platformName']='Android'
        dc['deviceName']='dcee06b38c7f'#192.168.76.101:5555  dcee06b38c7f
        dc['platformVersion']='6.0'
        dc['app'] ='E:/Android/bv_v4.0.0.11_20161223_141755.apk'
        dc['appPackage']='com.lubansoft.bimview4phone'
        dc['appActivity']='com.lubansoft.bimview4phone.ui.activity.StartupActivity'  #com.tencent.mobileqq.activity.LoginActivity
        dc["unicodeKeyboard"] = "True"#两行代码 支持中文输入
        dc["resetKeyboard"] = "True"
        cls.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',dc)


        w.driver
        d.driver

    def setUp(self):
        print "start"

    def tearDown(self):
        tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        print "end"

    #左滑
    def left(self,x1,y1,x2,y2,t):
        self.driver.swipe(x1,y1,x2,y2,t)
        time.sleep(1)

    #点击有id的按钮
    def dianji(self,id):
        self.driver.find_element_by_id(id).click()

    #获取屏幕尺寸
    def size(self):
        global x,y,w,h
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        w=int(x*0.35)
        h=int(y*0.8)
        print x,y,w,h


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

    #登录pic.ui.activity.NewFunctionNavigationActivity
    def test_1login(self):
        u'''登录'''
        self.size()
        try:
            if self.driver.current_activity==".ui.activity.NewFunctionNavigationActivity":
                self.swippic()
            else:
                time.sleep(4)
                allow=self.driver.find_elements_by_id("com.huawei.systemmanager:id/btn_allow")
                if allow:
                    allow[0].click()
        except Exception as e:
            print e

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
    #     self.upgrade()
    #     self.tuijian()
    #
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
        try:
            self.driver.swipe(w,h,w,h,1)
            #self.dianji("com.lubansoft.bimview4phone:id/btn_recommend_dept_close")
        except Exception as e:
            print e

    #创建协作
    def test_2createtheme(self):
        u'''创建协作'''
        #点击协作
        self.dianji("com.lubansoft.bimview4phone:id/tv_collaboration")
        #新建协作
        self.dianji("com.lubansoft.bimview4phone:id/ibtn2_topbar")
        #判断是否进入到创建协作页面
        self.assertEqual(".ui.activity.CreateCooperationActivity",self.driver.current_activity,u"没有权限")

        #输入主题
        self.shuru("com.lubansoft.bimview4phone:id/et_theme",timestr)
        #收回键盘
        self.driver.hide_keyboard()
        #self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/tv_title").click()
        #点击照片
        self.dianji("com.lubansoft.bimview4phone:id/iv_add_defect_photo")
        #选择表单
        self.driver.find_element_by_name("选择表单").click()
        self.dianji("com.lubansoft.bimview4phone:id/iv_form_check")
        self.dianji("com.lubansoft.bimview4phone:id/tv_confirm_choose")
        #点击提交
        self.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
        #判断是否创建成功
        self.driver.wait_activity(".ui.activity.BVMainActivity",20,2)
        title=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_item_collaboration_title")[0].text
        print u"标题:"+title
        self.assertEqual(title,timestr,u"创建失败")

    #意见反馈.ui.activity.FeedbackActivity
    def test_3opinion(self):
        u'''意见反馈'''
        #点击设置
        self.dianji("com.lubansoft.bimview4phone:id/tv_setting")
        #点击意见反馈
        self.driver.find_element_by_name("意见反馈").click()
        #激活键盘
        self.activekeyboard(2)
        #判断是否进入意见反馈页面
        self.assertEqual(".ui.activity.FeedbackActivity",self.driver.current_activity,u"没有权限")
        #输入意见
        self.shuru("com.lubansoft.bimview4phone:id/edt_feedback_content",u"爆机")
        #输入联系方式
        self.shuru("com.lubansoft.bimview4phone:id/edt_feedback_contact","111122223333")
        #点击反馈类型
        self.dianji("com.lubansoft.bimview4phone:id/tv_feedback_type")
        self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_common_list")[6].click()
        #点击提交
        self.dianji("com.lubansoft.bimview4phone:id/btn_feedback_commit")
        self.driver.get_screenshot_as_file("E:\\Android\\commit.png")
        #判断回到设置页面
        self.driver.wait_activity(".ui.activity.BVMainActivity",20,2)
        self.assertEqual(".ui.activity.BVMainActivity",self.driver.current_activity,u"意见反馈提交失败")

    #动态搜索
    def test_4moving(self):
        u'''动态搜索'''
        time.sleep(3)
        #点击动态
        self.dianji("com.lubansoft.bimview4phone:id/tv_dynamic")
        time.sleep(2)
        self.driver.get_screenshot_as_file(u"E:\\Android\\动态.png")
        #点击搜索
        self.dianji("com.lubansoft.bimview4phone:id/ibtn3_topbar")
        #判断是否进入到搜索页面
        self.assertEqual(".ui.activity.BVSearchActivity",self.driver.current_activity,u"搜索失败")
        self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_search_topbar").send_keys("11AC")
        #激活键盘
        self.activekeyboard(0)
        w1=int(x*0.92)
        h1=int(y*0.92)
        self.driver.swipe(w1,h1,w1,h1,1)

        # self.driver.press_keycode(66)
        # self.driver.press_keycode(66)
        #self.driver.keyevent(84)
        time.sleep(4)
        self.driver.get_screenshot_as_file(u"E:\\Android\\动态搜索.png")
        #判断搜索到的第一个文件名称是否包含关键字
        if "11AC" in self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/doc_names")[0].text:
            print u"搜索成功"
        else:
            print u"搜索失败"

        self.dianji("com.lubansoft.bimview4phone:id/tv_cancel_topbar")
        time.sleep(2)

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

    #激活键盘 0，1代表原始键盘，2代表appium键盘
    def activekeyboard(self,num):
        jianpan=self.driver.available_ime_engines
        # print jianpan
        # print jianpan[2]
        self.driver.activate_ime_engine(jianpan[num])
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        print "down"
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(shouji('test_1login'))
    suite.addTest(shouji('test_2createtheme'))
    #unittest.TextTestRunner(verbosity=2).run(suite)
    # timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    # filename = '/Users/lihui/Documents/PycharmProjects/test/report/'+timestr+'.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='result',
    #     description='report'
    # )
    # runner.run(suite)
    filename="E:\\Android\\myAppiumLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(suite)                 #自动进行测试
    '''协作列表.ui.activity.BVMainActivity
意见反馈.ui.activity.FeedbackActivity
搜索.ui.activity.BVSearchActivity
动态搜索后.ui.activity.BVSearchActivity
    '''