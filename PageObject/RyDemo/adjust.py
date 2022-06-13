#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class adjust(BasePage):
    # ————————————————————————
    # 参数调节相关
    # ————————————————————————
    @teststep
    def enter_edit_page(self):
        log.i('进入帧处理主界面')
        try:
            self.d(resourceId='com.quvideo.application:id/llFrame').click(1)
        except Exception:
            log.i('当前已经在帧处理主界面')

    @teststep
    def adjust_enter(self):
        log.i('滑动到下一个页面')
        text = self.d.xpath('//*[@text="字幕"]')
        self.swipe_left(text, 0.8)
        i = 0
        while i < 15:
            self.swipe_left(text, 0.8)
            i = i + 1

        try:
           self.d(resourceId="com.quvideo.application:id/tvContent", text="参数调节").click(1)
        except Exception:
            log.i('当前已经在参数调节页面')

    @teststep
    def select_adjust_alpha(self, adjust_type, inst=50):
        '''
        设置滤镜程度 除了（0~10） 之间的的任意数字,5左右的数字存在一定的偏差
        :param inst: inst  0—~100之间任意间隔0.2的数字  exp 10、21、46、...67、98
        '''
        log.i('设置滤镜程度为 %s' % inst)
        bar = self.d.xpath(adjust_type).info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left']
        self.d.long_click(x, y)



if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    p = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[9]/android.widget.SeekBar[1]'
    adjust().adjust_enter()
    time.sleep(1)
    adjust().select_adjust_alpha(adjust_type=p)