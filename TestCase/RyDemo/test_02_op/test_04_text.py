#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import text

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_text(unittest.TestCase, BasePage):
    '''字幕'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_text_choose(self):
        """应用字幕-字幕类型"""
        time.sleep(3)
        text.text().enter_edit_page()
        time.sleep(3)


        log.i('选择字幕类型')
        text_type = '//*[@resource-id="com.quvideo.application:id/subtitle_recyclerview"]/' \
                    'android.view.ViewGroup[2]/android.widget.RelativeLayout[1]'
        text.text().text_use(text_type)
        self.screenshot()

    @testcase
    def test_02_text_input(self):
        """应用字幕-输入"""

        log.i('文本输入')
        text.text().text_input(text='input text test')
        self.screenshot()

    @testcase
    def test_03_text_font(self):
        """应用字幕-字体"""
        log.i('修改字体')
        text.text().text_op_font()
        self.screenshot()
        log.i('对齐方式')
        text.text().text_op_align()
        self.screenshot()

    @testcase
    def test_04_text_font(self):
        """应用字幕-其他设置"""
        log.i('其他操作-旋转、缩小、放大、镜像')
        text.text().text_op_other(4)
        self.screenshot()
        log.i('调节字体颜色')
        text.text().select_text_alpha(20)
        self.screenshot()


