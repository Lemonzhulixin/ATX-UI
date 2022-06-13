#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class text(BasePage):
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
    def text_use(self, text_type):
        log.i('进入字幕')
        try:
            self.d.xpath('//*[@text="字幕"]').click(1)
        except Exception:
            log.i('当前已经在字幕页面')

        log.i('选择字幕样式')
        self.d.xpath(text_type).click()

        # log.i('清除文本')
        # self.d(resourceId="com.quvideo.application:id/et_edit", text="字幕").clear_text()
        # time.sleep(0.5)

    @teststeps
    def text_input(self, text="aaaa"):
        log.i('字幕文本输入')
        self.set_fastinput_ime()
        id = 'com.quvideo.application:id/et_edit'
        self.d(resourceId=id).click()
        self.d(resourceId=id).clear_text()
        self.d(resourceId=id).set_text(text)
        self.d.press("back")

    @teststeps
    def text_op_font(self):
        log.i('切换字体')
        self.d(resourceId="com.quvideo.application:id/tvContent", text="字体").click()

        log.i('开启/关闭粗体')
        self.d(resourceId="com.quvideo.application:id/btn_blod").click()
        # try:
        #     self.d(resourceId="com.quvideo.application:id/btn_blod", text="粗体开启").click(1)
        # except:
        #     self.d(resourceId="com.quvideo.application:id/btn_blod", text="粗体关闭").click(1)

        log.i('开启/关闭斜体')
        self.d(resourceId="com.quvideo.application:id/btn_italic").click()
        # try:
        #     self.d(resourceId="com.quvideo.application:id/btn_italic", text="粗体开启").click(1)
        # except:
        #     self.d(resourceId="com.quvideo.application:id/btn_italic", text="粗体关闭").click(1)

    @teststeps
    def text_op_align(self):
        log.i('对齐方式-左对齐')
        self.d(resourceId="com.quvideo.application:id/btn_align_left").click()

        log.i('对齐方式-居中对齐')
        self.d(resourceId="com.quvideo.application:id/btn_align_center").click()

        log.i('对齐方式-右对齐')
        self.d(resourceId="com.quvideo.application:id/btn_align_right").click()

    @teststeps
    def text_op_other(self, number):
        log.i('字幕旋转 %s 次' % number)
        for i in range(number):
            self.d(resourceId="com.quvideo.application:id/btnRotation").click()

        log.i('字幕缩小 %s 次' % number)
        for i in range(number):
            self.d(resourceId="com.quvideo.application:id/btnFitIn").click()

        log.i('字幕放大 %s 次' % number)
        for i in range(number):
            self.d(resourceId="com.quvideo.application:id/btnFitOut").click()

        log.i('字幕镜像 %s 次' % number)
        for i in range(number):
            self.d(resourceId="com.quvideo.application:id/btnMirror").click()


    @teststep
    def select_text_alpha(self, inst=50):
        '''
        设置滤镜程度 除了（0~10） 之间的的任意数字,5左右的数字存在一定的偏差
        :param inst: inst  0—~100之间任意间隔0.2的数字  exp 10、21、46、...67、98
        '''
        log.i('设置颜色区域为 %s' % inst)
        bar = self.d(resourceId="com.quvideo.application:id/colorbar_text_color").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left'] + inst * unit
        self.d.long_click(x, y)



if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    p = '//*[@resource-id="com.quvideo.application:id/subtitle_recyclerview"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]'
    text().text_use(p)
    text().text_input(text='input text test')
    text().text_op_font()
    text().text_op_align()
    text().text_op_other(4)
    text().select_text_alpha(20)