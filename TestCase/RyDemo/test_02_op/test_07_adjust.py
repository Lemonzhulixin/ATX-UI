#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import adjust

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_adjust(unittest.TestCase, BasePage):
    '''参数调节'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_adjust_use(self):
        """参数调节"""
        time.sleep(3)
        adjust.adjust().enter_edit_page()

        adjust_type1 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[1]/android.widget.SeekBar[1]'
        adjust.adjust().adjust_enter()
        log.i('亮度调节')
        adjust.adjust().select_adjust_alpha(adjust_type1)
        time.sleep(1)
        self.screenshot()

        adjust_type2 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[2]/android.widget.SeekBar[1]'
        log.i('对比度调节')
        adjust.adjust().select_adjust_alpha(adjust_type2)
        time.sleep(1)
        self.screenshot()

        adjust_type3 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[3]/android.widget.SeekBar[1]'
        log.i('锐度调节')
        adjust.adjust().select_adjust_alpha(adjust_type3)
        time.sleep(1)
        self.screenshot()

        adjust_type4 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[4]/android.widget.SeekBar[1]'
        log.i('饱和度调节')
        adjust.adjust().select_adjust_alpha(adjust_type4)
        time.sleep(1)
        self.screenshot()

        adjust_type5 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[5]/android.widget.SeekBar[1]'
        log.i('色温调节')
        adjust.adjust().select_adjust_alpha(adjust_type5)
        time.sleep(1)
        self.screenshot()

        adjust_type6 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[6]/android.widget.SeekBar[1]'
        log.i('暗角调节')
        adjust.adjust().select_adjust_alpha(adjust_type6)
        time.sleep(1)
        self.screenshot()

        adjust_type7 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[7]/android.widget.SeekBar[1]'
        log.i('阴影调节')
        adjust.adjust().select_adjust_alpha(adjust_type7)
        time.sleep(1)
        self.screenshot()

        adjust_type8 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[8]/android.widget.SeekBar[1]'
        log.i('褪色调节')
        adjust.adjust().select_adjust_alpha(adjust_type8)
        time.sleep(1)
        self.screenshot()

        adjust_type9 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[9]/android.widget.SeekBar[1]'
        log.i('色相调节')
        adjust.adjust().select_adjust_alpha(adjust_type9)
        time.sleep(1)
        self.screenshot()

        adjust_type11 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[10]/android.widget.SeekBar[1]'
        log.i('高光调节')
        adjust.adjust().select_adjust_alpha(adjust_type11)
        time.sleep(1)
        self.screenshot()

        adjust_type12 = '//*[@resource-id="com.quvideo.application:id/recycler_adjust"]/android.view.ViewGroup[11]/android.widget.SeekBar[1]'
        log.i('颗粒调节')
        adjust.adjust().select_adjust_alpha(adjust_type12)
        time.sleep(1)
        self.screenshot()









