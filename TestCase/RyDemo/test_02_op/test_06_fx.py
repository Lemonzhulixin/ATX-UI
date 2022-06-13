#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import fx

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_fx(unittest.TestCase, BasePage):
    '''特效'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_fx_use(self):
        """特效使用"""
        time.sleep(3)
        fx.fx().enter_edit_page()
        time.sleep(3)

        log.i('逐一使用特效')
        fx_type0 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]'
        fx.fx().fx_switch()
        time.sleep(1)
        fx.fx().fx_use(fx_type0)
        time.sleep(1)
        self.screenshot()

        fx_type1 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]'
        fx.fx().fx_use(fx_type1)
        time.sleep(1)
        self.screenshot()

        fx_type2 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[3]/android.widget.RelativeLayout[1]'
        fx.fx().fx_use(fx_type2)
        time.sleep(1)
        self.screenshot()


        fx_type3 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[4]/android.widget.RelativeLayout[1]'
        fx.fx().fx_use(fx_type3)
        time.sleep(1)
        self.screenshot()

        fx_type4 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[5]/android.widget.RelativeLayout[1]'
        fx.fx().fx_use(fx_type4)
        time.sleep(1)
        self.screenshot()










