#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from Public.Test_data import *
from PageObject.RyDemo import filter

pkg_name = ReadConfig().get_pkg_name(key='RY')

class test_filter(unittest.TestCase, BasePage):
    '''滤镜'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_filter_use(self):
        """滤镜使用"""
        time.sleep(3)
        filter.filter().enter_edit_page()

        time.sleep(3)
        log.i('使用空滤镜')
        kong = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(kong)
        self.screenshot()

        log.i('使用mo11滤镜')
        mo11 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(mo11)
        self.screenshot()

        log.i('使用AN7滤镜')
        AN7 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[3]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(AN7)
        time.sleep(1)
        filter.filter().select_filter_alpha(inst=30)
        self.screenshot()

    @testcase
    def test_02_filter_click(self):
        """逐个点击滤镜"""
        log.i('逐个点击滤镜')
        NA6 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[4]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(NA6)
        self.screenshot()

        MCR1 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[5]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(MCR1)
        self.screenshot()

        filter.filter().cover_drag()
        self.screenshot()

        MCR7 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[4]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(MCR7)
        self.screenshot()

        FM1 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[5]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(FM1)
        self.screenshot()

        FM8 = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[6]/android.widget.RelativeLayout[1]'
        filter.filter().filter_use(FM8)
        self.screenshot()
