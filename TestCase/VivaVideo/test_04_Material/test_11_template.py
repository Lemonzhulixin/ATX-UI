#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PageObject.VivaVideo import home, template, publish, edit
from Public.Decorator import *
import unittest
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class template_template(unittest.TestCase, BasePage):
    '''小影学院模版'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_template_click(self):
        """小影学院模版-选择模版"""
        time.sleep(1)
        home.home_Page().click_template_btn()
        template.template_Page().click_template_tab()
        template.template_Page().click_template_cover()

    @testcase
    def test_02_template_use(self):
        """小影学院模版-使用"""
        time.sleep(1)
        template.template_Page().clips_template_add()
        edit.edit_page().stop_video_play()

    @testcase
    def test_03_template_export(self):
        """小影学院模版-480P导出"""
        publish.publish_page().click_export_btn()
        time.sleep(1)
        self.screenshot()
        publish.publish_page().select_export(inst=1)
        self.screenshot()
        publish.publish_page().wait_export()
        publish.publish_page().sharePage_back('返回首页')
        publish.publish_page().click_pop_dialog()
