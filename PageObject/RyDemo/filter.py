#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class filter(BasePage):
    # ————————————————————————
    # 滤镜相关
    # ————————————————————————
    @teststep
    def enter_edit_page(self):
        log.i('进入帧处理主界面')
        try:
            self.d(resourceId='com.quvideo.application:id/llFrame').click(1)
        except Exception:
            log.i('当前已经在帧处理主界面')

    @teststep
    def filter_use(self,filter_path):
        log.i('进入滤镜')
        try:
           self.d(resourceId="com.quvideo.application:id/tvContent", text="滤镜").click(1)
        except Exception:
            log.i('当前已经在滤镜选择页面')

        log.i('选择滤镜')
        self.d.xpath(filter_path).click()
        time.sleep(0.5)


    @teststep
    def select_filter_alpha(self, inst=50):
        '''
        设置滤镜程度 除了（0~10） 之间的的任意数字,5左右的数字存在一定的偏差
        :param inst: inst  0—~100之间任意间隔0.2的数字  exp 10、21、46、...67、98
        '''
        log.i('设置滤镜程度为 %s' % inst)
        bar = self.d(resourceId="com.quvideo.application:id/seekbar_pop_progress").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def cover_drag(self):
        log.i('滑动到下一个页面')
        cover = self.d.xpath('//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]'
                             '/android.view.ViewGroup[5]/android.widget.RelativeLayout[1]')
        self.swipe_left(cover, 0.8)
        i = 0
        while i < 15:
            self.swipe_left(cover, 0.8)
            i = i + 1


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    p = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[3]/android.widget.RelativeLayout[1]'
    filter().filter_use(p)
    time.sleep(1)
    filter().select_filter_alpha()
    filter().cover_drag()



