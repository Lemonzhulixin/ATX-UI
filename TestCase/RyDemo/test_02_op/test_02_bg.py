#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import bg

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_bg(unittest.TestCase, BasePage):
    '''背景'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_bg_mh(self):
        """模糊背景"""
        time.sleep(3)
        bg.bg().enter_edit_page()
        time.sleep(3)

        log.i('选择模糊背景')
        bg.bg().bg_use(bg='模糊')
        log.i('缩放')
        for i in range(3):
          self.d(resourceId="com.quvideo.application:id/btnFitIn").click()
        log.i('调节程度')
        time.sleep(1)
        bg.bg().select_bg_alpha(60)
        self.screenshot()

    def test_02_bg_custom(self):
        """自定义背景"""
        log.i('选择自定义背景')
        bg.bg().bg_use(bg='自定义')
        bg.bg().bg_custom()
        self.screenshot()
        bg.bg().bg_op(4)

    def test_03_bg_other(self):
        """纯色/渐变背景"""
        log.i('选择纯色背景')
        bg.bg().bg_use(bg='纯色')
        self.screenshot()
        log.i('选择渐变背景')
        bg.bg().bg_use(bg='渐变')
        self.screenshot()



