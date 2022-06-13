#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class zc(BasePage):
    # ————————————————————————
    # 转场相关
    # ————————————————————————
    @teststep
    def enter_edit_page(self):
        log.i('进入帧处理主界面')
        try:
            self.d(resourceId='com.quvideo.application:id/llFrame').click(1)
        except Exception:
            log.i('当前已经在帧处理主界面')

    @teststep
    def zc_use(self, zc_path):
        log.i('进入转场')
        # self.d(resourceId="com.quvideo.application:id/tvContent", text="背景").click()
        try:
            self.d.xpath('//*[@text="转场"]').click(1)
        except Exception:
            log.i('当前已经在转场选择页面')


        log.i('选择转场')
        self.d.xpath(zc_path).click()
        time.sleep(0.5)

    @teststep
    def select_zc_alpha(self, inst=50):
        '''
        设置滤镜程度 除了（0~10） 之间的的任意数字,5左右的数字存在一定的偏差
        :param inst: inst  0—~100之间任意间隔0.2的数字  exp 10、21、46、...67、98
        '''
        log.i('设置模糊程度为 %s' % inst)
        bar = self.d(resourceId="com.quvideo.application:id/seekbar_pop_progress").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left'] + inst * unit
        self.d.long_click(x, y)



if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    p = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[3]/android.widget.RelativeLayout[1]'
    zc().zc_use(p)
    time.sleep(3)
    zc().select_zc_alpha(40)