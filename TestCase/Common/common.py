#__author__ = 'user'
#coding: utf-8
import time
import driver
from selenium.webdriver.support.ui import WebDriverWait
from functools import wraps
class common:
    d= driver.drv
    driver=d.driver
    #隐式等待

    png_file='E:\\Testreport\\png\\'

    def __init__(self):
        pass

    def retry(attempt):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kw):
                att = 0
                while att < attempt:
                    try:
                        return func(*args, **kw)
                    except Exception as e:
                        att += 1
            return wrapper
        return decorator


    #左滑
    def left(self,x1,y1,x2,y2,t):
        self.driver.swipe(x1,y1,x2,y2,t)
        time.sleep(1)

    #点击有id的按钮
    @retry(attempt=3)
    def dianji(self,id):
        self.driver.find_element_by_id(id).click()

    #获取屏幕尺寸
    def size(self):
        global x,y,w,h
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        w=int(x*0.35)
        h=int(y*0.8)
        siz=(x,y,w,h)
        return siz

    #多个返回时
    @retry(attempt=3)
    def clickback(self,activity):
        i=0
        while i<10:
            if self.driver.current_activity==activity:
                break
            else:
                #点击返回键
                self.driver.press_keycode(4)
                i=i+1
                time.sleep(1)



    #滑动引导图
    def swippic(self):
        (x,y,w,h)=self.size()
        x1=int(x*0.95)
        y1=int(y*0.5)
        x2=int(x*0.05)
        print x,y,x1,y1,x2
        time.sleep(4)
        allow=self.driver.find_elements_by_id("com.huawei.systemmanager:id/btn_allow")
        if allow:
            allow[0].click()
        print "pic"+self.driver.current_activity
        self.left(x1,y1,x2,y1,1000)
        self.left(x1,y1,x2,y1,1000)
        self.left(x1,y1,x2,y1,1000)
        print "pic"+self.driver.current_activity
        self.driver.get_screenshot_as_file("E:\\Android\\1.png")
        #点击立即体验按钮
        self.driver.swipe(w,h,w,h,1)
        time.sleep(1)

    #输入框
    @retry(attempt=3)
    def shuru(self,id,content):
        self.driver.find_element_by_id(id).send_keys(content)
        time.sleep(2)


    #激活键盘 0，1代表原始键盘，2代表appium键盘
    def activekeyboard(self,num):
        jianpan=self.driver.available_ime_engines
        # print jianpan
        # print jianpan[2]
        self.driver.activate_ime_engine(jianpan[num])
        time.sleep(2)

    #截图
    def screenshot(self,index):
        timestr=time.strftime('%Y%m%d',time.localtime(time.time()))
        img_name= timestr  + '_' +str(index)+'.png'
        self.driver.get_screenshot_as_file('%s%s' % (self.png_file,img_name))
        return img_name

    #等待元素出现
    def wait(self,id):
        WebDriverWait(self.driver,15).until(lambda x:x.find_element_by_id(id))

    #等待元素消失
    def waitpass(self,id):
        WebDriverWait(self.driver,15).until_not(lambda x:x.find_element_by_id(id))