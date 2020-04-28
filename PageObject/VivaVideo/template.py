#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/21 2:19 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: template.py


from Public.Decorator import *
from Public.Test_data import *
import random
import re
from PageObject.VivaVideo import gallery, publish

log = Log()

class template_Page(BasePage):

    @teststep
    def is_template_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/tvName", text="模版").wait()
        log.i('是否在拍同款页面，status=%s' % status)
        return status

    @teststep
    def click_template_tab(self):
        log.i('点击模版tab')
        self.d(resourceId="com.quvideo.xiaoying:id/tvName", text="模版").click()

    @teststep
    def click_tutorials_tab(self):
        log.i('点击教程tab')
        self.d(resourceId="com.quvideo.xiaoying:id/tvName", text="教程").click()

    @teststep
    def click_template_banner(self):
        log.i('点击模版tab下banner')
        self.d(resourceId="com.quvideo.xiaoying:id/template_layout_banner").click()

    @teststep
    def swipe_template_banner(self):
        log.i('向左滑动banner')
        banner = self.d(resourceId="com.quvideo.xiaoying:id/template_layout_banner")
        self.swipe_left(element=banner,steps=0.05)

    @teststeps
    def banner_back(self):
        log.i('从banner跳转后的页面返回')
        self.d.press("back")
        if self.d(resourceId="com.quvideo.xiaoying:id/template_layout_banner").exists:
            print("已经返回到模版tab了")
        else:
            log.i('当前是跳转的素材banner,需要再次back返回')
            self.d.press("back")

    @teststeps
    def click_tutorials_banner(self, text='热门', number=2):
        log.i('点击教程%s分类下推荐banner' % text)
        self.d(text=text).click()
        els = self.d(resourceId="com.quvideo.xiaoying:id/templateCover")
        for i in range(number):
            els[i].click()
            time.sleep(0.5)
            self.screenshot()
            self.d.press("back")

    @teststep
    def swipe_tutorials_banner(self):
        log.i('向上滑动banner')
        banner = self.d(resourceId="com.quvideo.xiaoying:id/templateCover")
        self.swipe_up(banner)
        time.sleep(0.5)


    @teststeps
    def click_template_cover(self):
        log.i(' 选择一个小影圈模版')
        cover = self.d(resourceId="com.quvideo.xiaoying:id/template_item_cover")
        n = len(cover)
        print('当前页面有%s个模版' % n)
        m = 0
        while True:# 若当前页面全部是vip模版会出错，需要上滑动再逐个点击
            log.i('点击第%s模版封面并立即使用' % m)
            cover[m].click()
            try:
                self.screenshot()
                self.d(resourceId='com.quvideo.xiaoying:id/card_view').click()
                self.d(resourceId="com.quvideo.xiaoying:id/text_progress", text='立即使用').click(3)
                break
            except:
                if self.d(resourceId="com.quvideo.xiaoying:id/text_progress", text='会员免费使用').exists:
                    self.screenshot()
                    log.i('当前是VIP模版，返回并重新选择')
                    self.d.press("back")
            m += 1

    @teststeps
    def clips_template_add(self):
        log.i('根据模版建议数添加镜头')
        time.sleep(2)
        clips_text = self.d(resourceId="com.quvideo.xiaoying:id/txt_clip_count").get_text()
        print(clips_text)
        n = re.sub("\D","",clips_text)
        gallery.gallery_page().gallery_clip_add(int(n))
        time.sleep(3)



if __name__ == '__main__':
    from Public.Log import Log


    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # for i in range(random.randint(2,5)):
    #    template_Page().swipe_template_banner()
    #    template_Page().click_template_banner()
    #    template_Page().banner_back()


    template_Page().clips_template_add()










