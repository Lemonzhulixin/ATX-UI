#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
from Public.Log import Log

log = Log()


class vip_page(BasePage):

    @teststep
    def is_vip_page(self):
        log.i('判断是否在VIP页面')
        status = self.d(text="使用兑换码").wait(timeout=5)
        log.i('status=%s' % status)
        return status

    @teststep
    def vip_back(self):
        log.i('从VIP页面返回首页')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_back").click()

    @teststep
    def click_server_btn(self):
        log.i('vip页面，点击客服按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/vip_home_service_text").click()

