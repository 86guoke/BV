#__author__ = 'user'
#coding: utf-8
from Common import *
import os
import unittest,time
class Project(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Project(self):
        u'''工程'''
        time.sleep(3)
        #点击第一个工程
        self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_all_project_name")[0].click()
        #等待进入工程页面
        self.driver.wait_activity(".ui.activity.ProjNavigationActivity",20,2)
        self.assertEqual(".ui.activity.ProjNavigationActivity",self.driver.current_activity,u"点击工程进入工程页面失败")
        #点击模型
        self.c.dianji("com.lubansoft.bimview4phone:id/iv_modle_function")
        #等待进入模型页面
        self.driver.wait_activity(".ui.activity.SGDGraphActivity",20.2)
        self.assertEqual(".ui.activity.SGDGraphActivity",self.driver.current_activity,u"点击模型失败")
        #点击返回
        self.c.dianji("com.lubansoft.bimview4phone:id/ibtn1_topbar")


    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"
        self.c.screenshot(2)
