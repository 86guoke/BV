#__author__ = 'user'
#coding: utf-8
from Common import *
import unittest,time,os
class Moving(unittest.TestCase):
    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        # 调用公用方法
        self.c = common.common()

    # 动态搜索
    def test_moving(self):
        u'''动态搜索'''
        try:
            time.sleep(3)
            # 点击动态
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_dynamic")
            time.sleep(2)
            self.driver.get_screenshot_as_file(u"E:\\Android\\动态.png")
            # 点击搜索
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn3_topbar")
            # 判断是否进入到搜索页面
            self.assertEqual(".ui.activity.BVSearchActivity", self.driver.current_activity, u"搜索失败")
            self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_search_topbar").send_keys("1")
            # 激活键盘
            self.c.activekeyboard(0)
            (x,y,w,h)=self.c.size()
            w1 = int(x * 0.92)
            h1 = int(y * 0.92)
            self.driver.swipe(w1, h1, w1, h1, 1)

            # self.driver.press_keycode(66)
            # self.driver.press_keycode(66)
            # self.driver.keyevent(84)
            time.sleep(4)
            self.driver.get_screenshot_as_file(u"E:\\Android\\动态搜索.png")
            # 判断搜索到的第一个文件名称是否包含关键字
            if "1" in self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/doc_names")[0].text:
                print u"搜索成功"
            else:
                print u"搜索失败"
            time.sleep(3)
        except Exception as e:
            print e
            raise Exception(e)
        finally:
            self.c.screenshot(6)
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")

    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"
