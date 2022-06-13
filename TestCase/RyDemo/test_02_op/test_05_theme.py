#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import theme

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_theme(unittest.TestCase, BasePage):
    '''主题'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_theme(self):
        """应用主题"""
        time.sleep(3)
        theme.theme().enter_edit_page()
        time.sleep(3)


        log.i('滑动到下一个页面')
        text = self.d.xpath('//*[@text="字幕"]')
        self.swipe_left(text, 0.8)
        time.sleep(0.5)

        try:
            self.d(resourceId="com.quvideo.application:id/tvContent", text="主题").click(1)
        except Exception:
            log.i('当前已经在主题选择页面')

        log.i('应用主题')
        self.d(resourceId="com.quvideo.application:id/home_template_item_text", text="梦幻爱情").click()
        time.sleep(3)

        self.d(resourceId="com.quvideo.application:id/home_template_item_text", text="冲浪夏日").click()
        time.sleep(3)





