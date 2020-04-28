#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, gallery, material, edit
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class material_text(unittest.TestCase, BasePage):
    '''素材中心-字幕'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name,
                        activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_text_display(self):
        """进入字幕分类页面"""
        # home.home_Page().click_home_btn()
        # home.home_Page().click_home_more()
        material.material_page().select_material_type("字幕")
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_02_text_use(self):
        """查看并使用字幕"""
        material.material_page().click_material_cover()
        material.material_page().select_material_use("字幕")
        time.sleep(1)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(1)
        self.assertTrue(edit.edit_page().is_addText_page())
        self.screenshot()

    @testcase
    def test_03_text_input(self):
        """输入字幕文本"""
        edit.edit_page().text_input("测试字幕文本输入")
        edit.edit_page().edit_finish()
        time.sleep(2)
        self.screenshot()
        # edit.edit_page().stop_video_play()
        edit.edit_page().edit_back("直接退出")

    @testcase
    def test_04_text_change(self):
        """使用其他字幕样式"""
        self.d.app_start(package_name=pkg_name,
                        activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')
        # home.home_Page().click_home_more()
        material.material_page().select_material_type("字幕")
        material.material_page().text_change('动态')
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(1)
        self.assertTrue(edit.edit_page().is_addText_page())
        self.screenshot()
        edit.edit_page().text_input("动态字幕文本输入")
        edit.edit_page().edit_finish()
        time.sleep(2)
        self.screenshot()
        edit.edit_page().stop_video_play()
        edit.edit_page().edit_back("直接退出")