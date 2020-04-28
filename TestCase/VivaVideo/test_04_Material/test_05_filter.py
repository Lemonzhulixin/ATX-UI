#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, gallery, material, edit
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class material_filter(unittest.TestCase, BasePage):
    '''素材中心-调色滤镜'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name,
                        activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_filter_display(self):
        """进入调色滤镜分类页面"""
        material.material_page().select_material_type("调色滤镜")
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_02_filter_use(self):
        """查看并使用调色滤镜"""
        material.material_page().click_material_cover()
        material.material_page().select_material_use("调色滤镜")
        time.sleep(1)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_03_filter_change(self):
        """使用其他调色滤镜"""
        material.material_page().common_change("去旅行")
        material.material_page().use_all_clips(all=False)
        time.sleep(2)
        self.screenshot()
        edit.edit_page().edit_back("保存并退出")