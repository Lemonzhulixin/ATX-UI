#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import gallery, material, edit, home
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class material_font(unittest.TestCase, BasePage):
    '''素材中心-字体'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name,
                        activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_font_display(self):
        """进入字体分类页面"""
        material.material_page().select_material_type("字体")
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_02_font_use(self):
        """查看并使用字体"""
        material.material_page().click_material_cover()
        material.material_page().select_material_use("字体")
        time.sleep(1)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(2)
        self.screenshot()

    @testcase
    def test_03_font_change(self):
        """下载并使用字体"""
        edit.edit_page().edit_font_enter()
        edit.edit_page().edit_font_use()
        time.sleep(3)
        self.d.click(0.5,0.5)
        self.screenshot()