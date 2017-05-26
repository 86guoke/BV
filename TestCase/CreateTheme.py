#__author__ = 'user'
#coding: utf-8
from Common import *
import unittest,time,os
timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
class CreateTheme(unittest.TestCase):
    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        # 调用公用方法
        self.c = common.common()

    # 创建协作
    def test_createtheme(self):
        u'''创建协作'''
        try:
            time.sleep(2)
            # 点击协作
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_collaboration")
            # 新建协作
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn2_topbar")

            self.driver.wait_activity(".ui.activity.CreateCooperationActivity",20,2)
            # 判断是否进入到创建协作页面
            self.assertEqual(".ui.activity.CreateCooperationActivity", self.driver.current_activity, u"没有权限")

            # 输入主题
            self.c.shuru("com.lubansoft.bimview4phone:id/et_theme", timestr)
            # 收回键盘
            self.driver.hide_keyboard()
            # self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/tv_title").click()
            # 点击照片
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_add_defect_photo")
            # 选择表单
            self.driver.find_element_by_name("选择表单").click()
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_form_check")
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_confirm_choose")
            # 点击提交
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            # 判断是否创建成功
            self.driver.wait_activity(".ui.activity.BVMainActivity", 20, 2)
            title = self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_item_collaboration_title")[0].text
            print u"标题:" + title
            self.assertEqual(title, timestr, u"创建失败")
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
