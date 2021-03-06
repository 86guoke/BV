#__author__ = 'user'
#coding: utf-8
from Common import *
import os
import unittest,time
from appium.webdriver.common.touch_action import TouchAction
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
times = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
class ProjectMaterial(unittest.TestCase):
    def setUp(self):
        self.s=driver.drv
        self.driver=self.s.driver
        #调用公用方法
        self.c=common.common()

    def test_Project(self):
        u'''工程资料上传和下载、下载管理页面'''
        try:
            time.sleep(3)
            #搜索工程test-pythonbv-hjg
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn2_topbar")
            self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_search_topbar").send_keys("test-pythonbv-hjg")
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

            #点击资料
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/tv_function")[3].click()
            #点击上传资料
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            print u"点击上传资料"
            #点击上传目录
            self.c.dianji("com.lubansoft.bimview4phone:id/rlly_conn_folder")
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/label_tv")
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/label_tv")[0].click()
            self.c.dianji("com.lubansoft.bimview4phone:id/ensure_ly")
            #点击关联标签
            self.c.dianji("com.lubansoft.bimview4phone:id/rlly_select_tag")
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/label_content")
            #添加标签
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn3_topbar")
            self.c.wait("android:id/button1")
            self.driver.find_element_by_name("最长支持10个字符").send_keys(times)
            self.c.dianji("android:id/button1")
            print u"创建标签："+times+u" 成功"
            time.sleep(1)
            self.c.waitpass("com.lubansoft.bimview4phone:id/pull_to_refresh_text")
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/label_content")[0].click()
            print u"选择标签：",self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/label_tv")[0].text
            self.c.dianji("com.lubansoft.bimview4phone:id/btn_confirm")
            #点击附件
            self.c.dianji("com.lubansoft.bimview4phone:id/add_attachment_iv")
            #点击从相册中选择
            self.driver.find_element_by_name("从相册中选择").click()
            #选择照片
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/id_item_select")[0].click()
            #点击完成
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_confirm_choose")
            #获取图片列表控件的location和size
            location=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/attach_name").location
            x=location.get("x")
            y=location.get("y")
            print x,y
            size=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/attach_name").size
            w=size["width"]
            h=size["height"]
            print w,h
            self.driver.swipe(x+w,y+h,x,y,1000)
            #点击编辑
            self.c.dianji("com.lubansoft.bimview4phone:id/edit_name")
            time.sleep(1)
            self.driver.find_element_by_class_name("android.widget.EditText").clear()
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys("test")
            #点击确定
            self.c.dianji("android:id/button1")
            print u"把图片名称改成test"
            print u"开始上传"
            #点击开始上传
            self.c.dianji("com.lubansoft.bimview4phone:id/upLoad_bt")
            #等待元素出现
            self.c.wait("android:id/button1")
            #点击关闭当前页面
            self.c.dianji("android:id/button1")
            print u"上传成功"
            #----------------------------------------------下载资料并做一个验证
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/label_tv")[0].click()
            #获取资料名称
            title1=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/doc_name_txt")[0].text
            print u"上传资料成功："+title1
            #点击下载资料
            self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/file_status_ic")[0].click()
            #删除刚才创建的标签
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn_self")
            #点击关联标签
            self.c.dianji("com.lubansoft.bimview4phone:id/rlly_select_tag")
            #等待元素出现
            self.c.wait("com.lubansoft.bimview4phone:id/label_content")
            #获取标签控件的location和size
            location1=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/label_tv").location
            x1=location1.get("x")
            y1=location1.get("y")
            print x1,y1
            size1=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/label_tv").size
            w1=size1["width"]
            h1=size1["height"]
            print w1,h1
            name1=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/label_tv")[0].text
            self.driver.swipe(x1+w1,y1+h1,x1,y1,1000)
            self.c.dianji("com.lubansoft.bimview4phone:id/delete")
            self.c.wait("android:id/button1")
            self.c.dianji("android:id/button1")
            print u"删除标签："+name1+u" 成功"
            time.sleep(1)
            print u"第一个标签现在是：",self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/label_tv")[0].text
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")

            #点击我的
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_setting")
            # if u"1份资料"==self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/tv_extra").text:
            #     print u"下载管理成功"
            # else:
            #     print u"下载管理失败"
            #点击下载管理
            self.driver.find_element_by_name("文件管理").click()
            #判断是否进入
            self.driver.wait_activity(".ui.activity.DownloadManageActivity",20,2)
            self.assertEqual(".ui.activity.DownloadManageActivity",self.driver.current_activity,u"点击下载管理失败")

            title3=self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/doc_name_txt")[0].text
            if title1==title3:
                print u"下载成功"
            else:
                print u"下载失败"

            #点击搜索
            self.c.dianji("com.lubansoft.bimview4phone:id/ibtn3_topbar")
            self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/edt_search_topbar").send_keys("test")
            (x,y,w,h)=self.c.size()
            w1 = int(x * 0.92)
            h1 = int(y * 0.92)
            self.driver.swipe(w1, h1, w1, h1, 1)
            time.sleep(3)
            #判断是否搜索成功
            if title1==self.driver.find_elements_by_id("com.lubansoft.bimview4phone:id/doc_name_txt")[0].text:
                print u"搜索成功"
            else:
                print u"搜索失败"
            #点击取消
            self.c.dianji("com.lubansoft.bimview4phone:id/tv_cancel_topbar")
            time.sleep(2)
            #长按
            action1=TouchAction(self.driver)
            el=self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/doc_name_txt")
            action1.long_press(el).wait(2000).perform()
            #点击全选
            self.c.dianji("com.lubansoft.bimview4phone:id/all_select_tv")
            #点击删除
            self.c.dianji("com.lubansoft.bimview4phone:id/all_delect_tv")
            #点击确定删除
            # self.c.dianji("android:id/button1")
            # time.sleep(2)
            #判断是否出现“没有已下载资料”
            if u"你的下载列表为空哦~"==self.driver.find_element_by_id("com.lubansoft.bimview4phone:id/error_view_text").text:
                print u"删除成功"
            else:
                print u"删除失败"
        except Exception as e:
            print e
            raise Exception(e)
        finally:
            self.c.screenshot(3)
            #点击返回
            self.c.clickback(".ui.activity.BVMainActivity")




    def tearDown(self):
        # tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # #self.driver.get_screenshot_as_file(u"E:\\Android\\pass\\%s.png"%tm)
        # filepath=os.path.join(os.path.dirname(__file__) + "/../Pic/%s.png"%tm)
        # self.driver.get_screenshot_as_file(filepath)
        print "end"

