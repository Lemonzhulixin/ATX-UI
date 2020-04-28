#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, gallery, material, edit
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class material_transition(unittest.TestCase, BasePage):
    '''素材中心-转场'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name,
                        activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_transition_display(self):
        """进入转场分类页面"""
        material.material_page().select_material_type("转场")
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_02_transition_use(self):
        """查看并使用转场"""
        material.material_page().click_material_cover()
        material.material_page().select_material_use("转场")
        time.sleep(1)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(2)
        self.screenshot()

    @testcase
    def test_03_transition_change(self):
        """使用其他转场"""
        material.material_page().common_change("经典")
        material.material_page().use_all_clips(all=True)
        time.sleep(2)
        self.screenshot()
        edit.edit_page().edit_back("保存并退出")