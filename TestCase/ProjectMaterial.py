#__author__ = 'user'
#coding: utf-8
from Common import *
import os
import unittest,time
class ProjectMaterial(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Project(self):
        u'''工程资料'''
        time.sleep(3)
        #点击资料
        self.c.dianji("com.lubansoft.bimview4phone:id/iv_doc_function")
        #点击创建资料
        self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
        #点击关联标签
        self.c.dianji("com.lubansoft.bimview4phone:id/rlly_conn_label")
        #点击+号
        self.c.dianji("com.lubansoft.bimview4phone:id/iv_add_defect_photo")
        #点击从相册中选择
        self.driver.find_element_by_name("从相册中选择").click()
        #选择照片
        self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/id_item_select")[0].click()
        #点击完成
        self.c.dianji("com.lubansoft.bimview4phone:id/tv_confirm_choose")
        #点击开始上传
        self.c.dianji("com.lubansoft.bimview4phone:id/upLoad_bt")
        #点击返回
        time.sleep(3)
        self.c.dianji("com.lubansoft.bimview4phone:id/ibtn1_topbar")

    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"
        self.c.screenshot(3)
