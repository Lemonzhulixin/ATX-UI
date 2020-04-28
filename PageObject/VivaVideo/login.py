#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
from Public.Log import Log
log = Log()


class login_page(BasePage):
    '''登录页面'''

    @teststep
    def Start_app(self):
        log.i("启动小影")
        self.d.app_start("com.quvideo.xiaoying")

    @teststep
    def click_login_btn(self):
        log.i('点击登录tab')
        self.d(resourceId="com.quvideo.xiaoying:id/text_count", text="登录").click()


    @teststep
    def login_QQ(self):
        log.i('QQ登录')
        btn_QQ1 = "//*[@resource-id='com.quvideo.xiaoying:id/user_no_login_list']/android.widget.LinearLayout[2]/android.widget.ImageView[1]"
        btn_QQ2 = "//*[@resource-id='com.quvideo.xiaoying:id/user_no_login_list']/android.widget.LinearLayout[3]/android.widget.ImageView[1]"
        time.sleep(1)
        self.d.xpath(btn_QQ1).click()

        # log.i('QQ授权登录')
        # if self.d.wait_activity("com.tencent.open.agent.PublicFragmentActivityForOpenSDK", timeout=10):
        #     self.d(text="QQ授权登录").click()
        # else:
        #     log.i('已经用其他方式登录过，切换到第三个按钮')
        #     self.d.xpath(btn_QQ2).click()
        #     self.d.wait_activity("com.tencent.open.agent.PublicFragmentActivityForOpenSDK", timeout=10)
        #     self.d(text="QQ授权登录").click()

        try:
            self.d(text="QQ授权登录").click(5)
        except:
            log.i('已经用其他方式登录过，切换到第三个按钮')
            self.d.xpath(btn_QQ2).click()
            self.d(text="QQ授权登录").click()

        log.i('完成QQ授权')
        self.d(text='完成QQ授权').click()
        time.sleep(3)


    @teststep
    def login_WB(self):
        log.i('微博登录')
        btn_WB1 = "//*[@resource-id='com.quvideo.xiaoying:id/user_no_login_list']/android.widget.LinearLayout[4]/android.widget.ImageView[1]"
        btn_WB2 = "//*[@resource-id='com.quvideo.xiaoying:id/user_no_login_list']/android.widget.LinearLayout[3]/android.widget.ImageView[1]"
        try:
            self.d.xpath(btn_WB1).wait(timeout=5).click()
        except:
            log.i('当前app未曾登录过')
            self.d.xpath(btn_WB2).wait(timeout=5).click()

    @teststep
    def is_login_success(self):
        log.i('检查是否登录成功')
        login_status = self.d(resourceId="com.quvideo.xiaoying:id/btn_info_edit").wait(timeout=10)
        log.i('登录状态： status=%s' % login_status)
        return login_status

    @teststep
    def logout(self):
        log.i('点击设置按钮')
        self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/studio_title_layout"]/android.widget.FrameLayout[1]').click()

        log.i("向上滑动直到出现'退出当前账号'")
        BasePage().find_element_by_swipe_up(self.d(text="退出当前帐号"),element=None,steps=0.2,max_swipe=10)

        log.i("点击'退出当前账号'")
        self.d(text = "退出当前帐号").click()

    @teststeps
    def is_logout_success(self):
        log.i('检查是否退出成功')
        logout_status = self.d(text="用此账号登录").wait(timeout=10)
        log.i('退出状态： status=%s' % logout_status)
        return logout_status

if __name__ == '__main__':
    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    login_page().Start_app()
    login_page().click_login_btn()
    login_page().login_QQ()
    # login_page().is_login_success()
    # login_page().logout()
    # login_page().is_logout_success()



