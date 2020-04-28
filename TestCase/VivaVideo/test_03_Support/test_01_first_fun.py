#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, gallery, studio, material, vip
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class first_fun(unittest.TestCase, BasePage):
    '''主要功能位跳转检查'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name, activity='com.quvideo.xiaoying.MainActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_first_fun_edit(self):
        """视频编辑跳转"""
        home.home_Page().click_edit_btn()
        time.sleep(0.5)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_back()

    @testcase
    def test_02_first_fun_mv(self):
        """相册MV跳转"""
        home.home_Page().click_mv_btn()
        time.sleep(0.5)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_back()

    @testcase
    def test_03_first_fun_draft(self):
        """草稿跳转"""
        home.home_Page().click_draft_btn()
        time.sleep(1)
        self.screenshot()
        home.home_Page().click_home_btn()

    @testcase
    def test_04_first_fun_material(self):
        """素材中心跳转"""
        home.home_Page().click_home_more()
        time.sleep(1)
        self.assertTrue(material.material_page().is_material_page())
        self.screenshot()
        material.material_page().material_back()

    @testcase
    def test_05_first_fun_vip(self):
        """VIP跳转"""
        home.home_Page().click_vip_btn()
        time.sleep(0.5)
        self.assertTrue(vip.vip_page().is_vip_page())
        self.screenshot()
        vip.vip_page().vip_back()