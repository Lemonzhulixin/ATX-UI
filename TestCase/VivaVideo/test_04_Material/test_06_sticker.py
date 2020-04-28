#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, gallery, material, edit
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class material_sticker(unittest.TestCase, BasePage):
    '''素材中心-贴纸'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name,
                        activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_sticker_display(self):
        """进入贴纸分类页面"""
        material.material_page().select_material_type("贴纸")
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_02_sticker_use(self):
        """查看并使用贴纸"""
        material.material_page().click_material_cover()
        material.material_page().select_material_use("贴纸")
        time.sleep(1)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_03_sticker_change(self):
        """使用其他贴纸"""
        material.material_page().sticker_change("可爱")
        edit.edit_page().edit_back("保存并退出")