#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PageObject.VivaVideo import home, gallery, publish, edit
from Public.Decorator import *
import unittest
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class op_project(unittest.TestCase, BasePage):
    '''工程文件操作'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)


    @testcase
    def test_01_project_create(self):
        """工程文件操作-创建工程"""
        home.home_Page().click_edit_btn()
        gallery.gallery_page().gallery_clip_add(3)
        edit.edit_page().stop_video_play()

    @testcase
    def test_02_project_export(self):
        """工程文件操作-720P导出"""
        publish.publish_page().click_export_btn()
        time.sleep(1)
        self.screenshot()
        publish.publish_page().select_export(inst=2)
        self.screenshot()
        publish.publish_page().wait_export()
        # publish.publish_page().sharePage_back('返回首页')
        # publish.publish_page().click_pop_dialog()