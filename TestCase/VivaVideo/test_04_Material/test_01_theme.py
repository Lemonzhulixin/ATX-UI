#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import gallery, material, edit, publish
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class material_theme(unittest.TestCase, BasePage):
    '''素材中心-主题'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name,
                         activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_theme_display(self):
        """进入主题分类页面"""
        material.material_page().select_material_type("主题")
        time.sleep(1)
        self.screenshot()

    @testcase
    def test_02_theme_use(self):
        """查看并使用主题"""
        self.watch_device("我知道了|取消")
        material.material_page().click_material_cover()
        material.material_page().select_material_use("主题")
        time.sleep(1)
        self.assertTrue(gallery.gallery_page().is_gallery_page())
        self.screenshot()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(1)
        self.assertTrue(edit.edit_page().is_preview_page())
        self.screenshot()
        edit.edit_page().close_pop_dialog()
        self.unwatch_device()


    @testcase
    def test_03_theme_material(self):
        """从素材中心更换带字幕主题"""
        time.sleep(2)
        edit.edit_page().stop_video_play()
        edit.edit_page().click_store_icon()
        material.material_page().material_theme_change(themelist='热门',theme='落日飞车',text=True)
        edit.edit_page().edit_finish()

    @testcase
    def test_04_theme_preview(self):
        """从预览页面更换主题"""
        time.sleep(1)
        material.material_page().preview_theme_change(themelist='日常')
        edit.edit_page().stop_video_play()
        publish.publish_page().click_draft_btn()