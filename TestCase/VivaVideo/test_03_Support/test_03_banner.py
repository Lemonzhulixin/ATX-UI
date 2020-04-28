#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, template, material
from Public.Test_data import *
import random

pkg_name = ReadConfig().get_pkg_name(key='XY')

class banner(unittest.TestCase, BasePage):
    '''banner跳转检查'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name, activity='com.quvideo.xiaoying.MainActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)



    @testcase
    def test_01_template_banner(self):
        """拍同款页面模版banner跳转"""
        home.home_Page().click_template_btn()
        time.sleep(1)
        self.assertTrue(template.template_Page().is_template_page())
        self.screenshot()
        template.template_Page().click_template_tab()

        for i in range(random.randint(2,5)):
            template.template_Page().swipe_template_banner()
            time.sleep(0.5)
            self.screenshot()
            template.template_Page().click_template_banner()
            time.sleep(1)
            self.screenshot()
            template.template_Page().banner_back()

    @testcase
    def test_02_tutorials_banner(self):
        """拍同款页面教程banner跳转"""
        template.template_Page().click_tutorials_tab()
        time.sleep(1)
        self.screenshot()
        template.template_Page().click_tutorials_banner(text='热门',number=3)

    @testcase
    def test_03_material_banner(self):
        """素材中心banner跳转"""
        home.home_Page().click_home_btn()
        home.home_Page().click_home_more()
        material.material_page().click_material_banner()
        time.sleep(1)
        self.screenshot()


