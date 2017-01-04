#__author__ = 'user'
#coding: utf-8
from Common import *
import unittest,time
class Opinion(unittest.TestCase):
    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        # 调用公用方法
        self.c = common.common()

    # 意见反馈.ui.activity.FeedbackActivity
    def test_3opinion(self):
        u'''意见反馈'''
        # 点击设置
        self.c.dianji("com.lubansoft.bimview4phone:id/tv_setting")
        # 点击意见反馈
        self.driver.find_element_by_name("意见反馈").click()
        # 激活键盘
        self.c.activekeyboard(2)
        # 判断是否进入意见反馈页面
        self.assertEqual(".ui.activity.FeedbackActivity", self.driver.current_activity, u"没有权限")
        # 输入意见
        self.c.shuru("com.lubansoft.bimview4phone:id/edt_feedback_content", u"爆机")
        # 输入联系方式
        self.c.shuru("com.lubansoft.bimview4phone:id/edt_feedback_contact", "111122223333")
        # 点击反馈类型
        self.c.dianji("com.lubansoft.bimview4phone:id/tv_feedback_type")
        self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_common_list")[6].click()
        # 点击提交
        self.c.dianji("com.lubansoft.bimview4phone:id/btn_feedback_commit")
        self.driver.get_screenshot_as_file("E:\\Android\\commit.png")
        # 判断回到设置页面
        self.driver.wait_activity(".ui.activity.BVMainActivity", 20, 2)
        self.assertEqual(".ui.activity.BVMainActivity", self.driver.current_activity, u"意见反馈提交失败")

    def tearDown(self):
        tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        print "end"