#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import zc

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_zc(unittest.TestCase, BasePage):
    '''转场'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_zc_right(self):
        """应用转场-右移"""
        time.sleep(3)
        zc.zc().enter_edit_page()
        time.sleep(3)

        log.i('右移')
        right = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]'
        zc.zc().zc_use(right)
        time.sleep(3)
        # zc.zc().select_zc_alpha(40)
        self.screenshot()

    @testcase
    def test_02_zc_down(self):
        """应用转场-下移"""
        log.i('下移')
        down = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[3]/android.widget.RelativeLayout[1]'
        zc.zc().zc_use(down)
        time.sleep(3)
        self.screenshot()

    @testcase
    def test_03_zc_up(self):
        """应用转场-上移"""
        log.i('上移')
        up = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[4]/android.widget.RelativeLayout[1]'
        zc.zc().zc_use(up)
        time.sleep(3)
        self.screenshot()

    @testcase
    def test_04_zc_other(self):
        """应用转场-空"""
        log.i('空转场')
        other = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]'
        zc.zc().zc_use(other)
        time.sleep(3)
        self.screenshot()



