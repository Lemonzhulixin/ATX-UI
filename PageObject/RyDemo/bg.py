#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class bg(BasePage):
    # ————————————————————————
    # 背景相关
    # ————————————————————————
    @teststep
    def enter_edit_page(self):
        log.i('进入帧处理主界面')
        try:
            self.d(resourceId='com.quvideo.application:id/llFrame').click(1)
        except Exception:
            log.i('当前已经在帧处理主界面')


    @teststep
    def bg_use(self, bg):
        log.i('进入背景')
        # self.d(resourceId="com.quvideo.application:id/tvContent", text="背景").click()
        try:
            self.d.xpath('//*[@text="背景"]').click(1)
            time.sleep(0.5)
        except Exception:
            log.i('当前已经在背景选择页面')


        log.i('选择背景')
        if bg == '模糊':
         self.d.xpath('//*[@resource-id="com.quvideo.application:id/btnBlur"]/android.widget.ImageView[1]').click()

        elif bg == '纯色':
            self.d.xpath('//*[@resource-id="com.quvideo.application:id/btnColor1"]/android.view.View[1]').click()

        elif bg == '渐变':
            self.d.xpath('//*[@resource-id="com.quvideo.application:id/btnGradual"]/android.widget.ImageView[1]').click()

        elif bg == '自定义':
            self.d.xpath('//*[@resource-id="com.quvideo.application:id/btnCustom"]/android.widget.ImageView[1]').click()



    @teststep
    def select_bg_alpha(self, inst=50):
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

    @teststep
    def bg_custom(self):
        log.i('选择一张图片')
        self.d(resourceId="com.quvideo.application:id/iv_cover").click()

        log.i('点击下一步进入编辑页')
        self.d(resourceId="com.quvideo.application:id/btn_next", text='下一步').click()

    @teststep
    def bg_op(self, number):
        log.i('旋转')
        for i in range(4):
          self.d(resourceId="com.quvideo.application:id/btnRotation").click()

        log.i('缩小 %s 次' % number)
        for i in range(number):
          self.d(resourceId="com.quvideo.application:id/btnFitIn").click()

        log.i('放大 %s 次' % number)
        for i in range(number):
            self.d(resourceId="com.quvideo.application:id/btnFitOut").click()




if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    bg().bg_use(bg='模糊')
    time.sleep(1)
    bg().select_bg_alpha(60)
    bg().bg_use(bg='自定义')
    bg().bg_custom()
    bg().bg_op(4)
