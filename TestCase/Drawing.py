#__author__ = 'user'
#coding: utf-8
from Common import *
import os,sys
import unittest,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
class Drawing(unittest.TestCase):

    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Drawing(self):
        u'''dwg图纸'''
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
            #标注
            b1 = int(x * 0.5)
            b2 = int(y * 0.65)
            #测量长度
            c1 = int(x * 0.5)
            c2 = int(y * 0.76)
            #布局
            b3 = int(x * 0.5)
            b4 = int(y * 0.85)
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
            #点击图纸
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_function")[6].click()
            self.c.wait("com.lubansoft.bimview4phone:id/ibtn_self")
            print u"进入图纸列表"
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            print u"切换到模型页面"
            self.c.wait("com.lubansoft.bimview4phone:id/ll_floor_choice")
            print u"切换到图纸列表"
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/ibtn_self")[0].click()
            #点击第一个文件下载
            title=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/doc_name_txt")[0].text
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/file_status_ic")[0].click()
            time.sleep(3)
            print u"下载图纸："+title+u" 成功"
            #打开预览图纸
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/rlly_dwg_list")[0].click()
            self.c.wait("com.lubansoft.bimview4phone:id/iv_enter_full_screen")
            print u"打开图纸预览"
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_enter_full_screen")
            print u"全屏预览"
            self.c.dianji("com.lubansoft.bimview4phone:id/iv_exit_full_screen")
            print u"退出全屏预览"
            #点击功能
            self.c.dianji("com.lubansoft.bimview4phone:id/rlly_function")
            #点击标注
            self.driver.swipe(b1, b2, b1, b2, 1)
            isElementExist=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_exit_hint")
            if isElementExist:
                self.c.wait("com.lubansoft.bimview4phone:id/tv_exit_hint")
                #选中一个点
                self.driver.swipe(b1, b2, b1, b2, 1)
                #等待
                self.c.wait("com.lubansoft.bimview4phone:id/tv_ok")
                #输入timestr
                self.c.shuru("com.lubansoft.bimview4phone:id/et_marker",timestr)
                #点击确定
                self.c.dianji("com.lubansoft.bimview4phone:id/tv_ok")
                print u"添加标注"+timestr+u"成功"
                #测量长度
                self.c.dianji("com.lubansoft.bimview4phone:id/rlly_function")
                self.driver.swipe(c1, c2, c1, c2, 1)
                #选择第一个点
                self.driver.swipe(b1, b2, b1, b2, 1)
                time.sleep(2)
                #选择第二个点
                self.driver.swipe(b3, b4, b3, b4, 1)
                time.sleep(2)
                print u"长度：",self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/tv_left").text
                print u"角度：",self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/tv_right").text
                #退出测量
                self.c.dianji("com.lubansoft.bimview4phone:id/tv_exit")

                #点击提交
                self.c.dianji("com.lubansoft.bimview4phone:id/ibtn3_topbar")
                time.sleep(2)

                #点击布局
                self.c.dianji("com.lubansoft.bimview4phone:id/rlly_layout")
                #切换布局
                self.driver.swipe(b3, b4, b3, b4, 1)
                print u"切换布局成功"

                #点击返回
                self.c.dianji("com.lubansoft.bimview4phone:id/ibtn1_topbar")
                #再次打开图纸
                self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/rlly_dwg_list")[0].click()
                self.c.wait("com.lubansoft.bimview4phone:id/iv_enter_full_screen")
                print u"再次打开图纸预览"
            else:
                print u"当前处于布局空间，功能不可用"

        except Exception as e:
            print e
            raise Exception(e)
        finally:
            self.c.screenshot(9)
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")


    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"

