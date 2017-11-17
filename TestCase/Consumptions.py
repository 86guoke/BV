#__author__ = 'user'
#coding: utf-8
from Common import *
import os,sys
import unittest,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Consumptions(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Consumptions(self):
        u'''消耗量'''
        try:
            time.sleep(3)
            # 点击工程
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_project")
            #搜索工程test-pythonbv-hjg
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn2_topbar")
            self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_search_topbar").send_keys("test-pythonbv-hjg")
            # 激活键盘
            self.c.activekeyboard(0)
            (x,y,w,h)=self.c.size()
            w1 = int(x * 0.92)
            h1 = int(y * 0.92)
            self.driver.swipe(w1, h1, w1, h1, 1)
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/tv_all_project_name")
            #点击第一个工程
            name=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_all_project_name")[0].text
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_all_project_name")[0].click()
            print u"点击工程:"+name
            #等待进入工程页面
            self.driver.wait_activity(".ui.activity.ProjNavigationActivity",20,2)
            self.assertEqual(".ui.activity.ProjNavigationActivity",self.driver.current_activity,u"点击工程进入工程页面失败")
            #点击消耗量
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_function")[5].click()
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn_self")
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            print u"选择新增类型"
            #选择人工
            self.c.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_item_choose_consumption_type")[0].click()
            self.c.wait("com.lubansoft.bimview4phone:id/tv_add_consumption")
            self.c.shuru("com.lubansoft.bimview4phone:id/edt_consumption_num","123.123")
            #点击键盘返回和完成
            self.driver.swipe(w1, h1, w1, h1, 1)
            self.driver.swipe(w1, h1, w1, h1, 1)
            #点击确定
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_commit_consumption")
            self.c.wait("com.lubansoft.bimview4phone:id/tv_info")
            #点击第一个
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_info")[0].click()
            self.c.wait("com.lubansoft.bimview4phone:id/edt_consumption_num")
            print u"实际消耗量数量：",self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_consumption_num").text
            #编辑实际消耗量
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn3_topbar")
            self.c.wait("com.lubansoft.bimview4phone:id/iv_consumption_delete")
            self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_consumption_num").clear()
            self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_consumption_num").send_keys("456.456")
            #点击键盘返回和完成
            self.driver.swipe(w1, h1, w1, h1, 1)
            self.driver.swipe(w1, h1, w1, h1, 1)
            #点击确定
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_commit_consumption")
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn3_topbar")
            print u"编辑后实际消耗量数量：",self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_consumption_num").text
            #查看消耗量编辑记录
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn2_topbar")
            name=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_operater")[0].text
            date=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_date")[0].text
            tim=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_time")[0].text
            describe=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_describe")[0].text
            print name+" "+date+" "+tim+" "+describe

        except Exception as e:
            print e
            raise Exception(e)
        finally:
            self.c.screenshot(5)
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")


    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"

