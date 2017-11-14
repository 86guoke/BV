#__author__ = 'user'
#coding: utf-8
from Common import *
import os,sys
import unittest,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Project(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Project(self):
        u'''工程'''
        try:
            time.sleep(3)
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
            #点击模型
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_function")[0].click()
            time.sleep(8)
            print u"进入模型页面"
            #等待进入模型页面
            self.driver.wait_activity(".ui.activity.SGDGraphActivity",20,2)
            self.assertEqual(".ui.activity.SGDGraphActivity",self.driver.current_activity,u"点击模型失败")
            #点击返回
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn1_topbar")
            #点击构件
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_function")[1].click()
            # time.sleep(5)
            self.driver.wait_activity(".ui.activity.CompSearchActivity",20,2)
            self.assertEqual(".ui.activity.CompSearchActivity",self.driver.current_activity,u"点击构件失败")
            print u"进入构件列表"
            #点击0层进入状态
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn_self")
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/iv_check")[0].click()
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/ibtn_self")[4].click()
            self.driver.wait_activity(".ui.activity.CompInformationActivity",20,2)
            self.assertEqual(".ui.activity.CompInformationActivity",self.driver.current_activity,u"进入状态失败")
            print u"进入构件状态"
            #创建状态
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn_self")
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            self.driver.wait_activity(".ui.activity.EditStateActivity",20,2)
            self.assertEqual(".ui.activity.EditStateActivity",self.driver.current_activity,u"进入新增状态失败")
            print u"进入新增状态页面"
            #添加状态
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn_select_state")
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_select_state")
            self.driver.wait_activity(".ui.activity.SelectStateActivity",20,2)
            self.assertEqual(".ui.activity.SelectStateActivity",self.driver.current_activity,u"进入选择状态失败")
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/tv_state_name")
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_state_name")[0].click()
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_state_name")[1].click()
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_state_name")[2].click()
            self.driver.wait_activity(".ui.activity.EditStateActivity",20,2)
            self.assertEqual(".ui.activity.EditStateActivity",self.driver.current_activity,u"选择状态失败")
            print u"选择状态挖土"
            #点击提交
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            time.sleep(2)
            self.assertEqual(".ui.activity.CompInformationActivity",self.driver.current_activity,u"新增状态失败")
            ZTname=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/tv_state_name").text
            print u"新增状态：",ZTname
            #编辑状态
            self.driver.find_elements_by_xpath("//android.widget.LinearLayout[@index='0']")[1].click()
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_state_edit")
            time.sleep(2)
            self.c.dianji("com.lubansoft.bimview4phone:id/toggle_btn")
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            time.sleep(2)
            print u"编辑状态成功"
            #完成状态
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_state_finish")
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            print u"完成状态"
            time.sleep(2)
            #删除状态
            self.driver.find_elements_by_xpath("//android.widget.LinearLayout[@index='0']")[1].click()
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_state_delete")
            self.c.dianji("android:id/button1")
            print u"删除状态成功"
            #消耗量
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_comp_consumption")
            print u"点击消耗量"
        except Exception as e:
            print e
            raise Exception(e)
        finally:
            self.c.screenshot(2)
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")


    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"

