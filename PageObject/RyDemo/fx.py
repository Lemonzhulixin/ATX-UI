#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class fx(BasePage):
    # ————————————————————————
    # 特效相关
    # ————————————————————————
    @teststep
    def enter_edit_page(self):
        log.i('进入帧处理主界面')
        try:
            self.d(resourceId='com.quvideo.application:id/llFrame').click(1)
        except Exception:
            log.i('当前已经在帧处理主界面')

    @teststep
    def fx_switch(self):
        log.i('滑动到下一个页面')
        text = self.d.xpath('//*[@text="字幕"]')
        self.swipe_left(text, 0.8)
        i=0
        while i < 15:
            self.swipe_left(text, 0.8)
            i = i + 1

        try:
           self.d(resourceId="com.quvideo.application:id/tvContent", text="特效").click(1)
        except Exception:
            log.i('当前已经在特效页面')

    @teststep
    def fx_use(self, fx_path):
        log.i('选择特效')
        self.d.xpath(fx_path).click()
        time.sleep(5)



if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    p = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[5]/android.widget.RelativeLayout[1]'
    fx().fx_switch()
    fx().fx_use(p)



