#__author__ = 'user'
#coding: utf-8
from Common import *
import os,sys
import unittest,time
class Inspection(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Project(self):
        u'''巡检'''
        try:
            time.sleep(3)
            #点击工程
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
            #点击巡检
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_patrol_function")
            self.c.wait("com.lubansoft.bimview4phone:id/iv_patrol_child_add")
            print u"进入巡检页面"
            print u"巡检任务名称：",self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_patrol_group_name")[0].text
            print u"巡检点名称：",self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_patrol_child_name")[0].text
            #添加巡检记录
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/iv_patrol_child_add")[0].click()
            self.c.wait("com.lubansoft.bimview4phone:id/btn_submit")
            #切换appium键盘
            self.c.activekeyboard(2)
            # 输入详情
            self.c.shuru("com.lubansoft.bimview4phone:id/et_patrol_detail", "ok")
            #选择照片
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_add_photo")
            #点击从相册中选择
            self.driver.find_element_by_name("从相册选择").click()
            #选择照片
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/id_item_select")[0].click()
            #点击完成
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_confirm_choose")
            #点击提交
            self.c.dianji("com.lubansoft.bimview4phone:id/btn_submit")
            self.c.wait("com.lubansoft.bimview4phone:id/iv_patrol_child_add")
            print u"检查结果正常时添加成功"
            #添加异常巡检记录并发起协作
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/iv_patrol_child_add")[0].click()
            self.c.wait("com.lubansoft.bimview4phone:id/btn_submit")
            #选择异常
            self.c.dianji("com.lubansoft.bimview4phone:id/rlly_patrol_state")
            self.driver.find_element_by_name("异常").click()
            # 输入详情
            self.c.shuru("com.lubansoft.bimview4phone:id/et_patrol_detail", "ok")
            #选择照片
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_add_photo")
            #点击从相册中选择
            self.driver.find_element_by_name("从相册选择").click()
            #选择照片
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/id_item_select")[0].click()
            #点击完成
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_confirm_choose")
            #点击提交
            self.c.dianji("com.lubansoft.bimview4phone:id/btn_submit")
            self.driver.find_element_by_name("立即提交并发起协作").click()
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn_self")
            # 输入主题
            self.c.shuru("com.lubansoft.bimview4phone:id/et_theme", "ok")
            #点击提交
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            self.c.wait("com.lubansoft.bimview4phone:id/iv_patrol_child_add")
            print u"立即提交并发起协作成功"
            #判断协作是否创建成功
            self.c.clickback(".ui.activity.BVMainActivity")
            #点击协作
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_collaboration")
            self.c.wait("com.lubansoft.bimview4phone:id/tv_item_collaboration_title")
            title = self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_item_collaboration_title")[0].text
            print u"标题:" + title
            self.assertEqual(title, "ok", u"创建失败")
        except Exception as e:
            print e
            raise Exception(e)
        finally:
            self.c.screenshot(4)
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")


    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"

