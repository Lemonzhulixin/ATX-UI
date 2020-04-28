#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, gallery, edit, camera
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class sec_fun(unittest.TestCase, BasePage):
    '''次要功能位跳转检查'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name, activity='com.quvideo.xiaoying.MainActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_sec_fun_addText(self):
        """加字幕跳转"""
        self.watch_device("取消")
        home.home_Page().click_sec_addText()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(0.5)
        self.assertTrue(edit.edit_page().is_addText_page())
        self.screenshot()
        edit.edit_page().edit_back("保存并退出")
        self.unwatch_device()

    @testcase
    def test_02_sec_fun_mixer(self):
        """画中画跳转"""
        home.home_Page().click_sec_Mixer()
        time.sleep(0.5)
        self.assertTrue(edit.edit_page().is_mixer_page())
        self.screenshot()
        self.d.press("back")

    def test_03_sec_fun_mosaic(self):
        """马赛克跳转"""
        time.sleep(0.5)
        home.home_Page().click_sec_Mosaic()
        gallery.gallery_page().gallery_clip_add(3)
        time.sleep(0.5)
        self.assertTrue(edit.edit_page().is_maosaic_page())
        self.screenshot()
        self.d.press("back")
        edit.edit_page().edit_back("直接退出")

    def test_04_sec_fun_FAQ(self):
        """新手教程跳转"""
        home.home_Page().click_sec_FAQ()
        time.sleep(5)
        self.screenshot()
        self.d.press("back")

    def test_05_sec_fun_capture(self):
        """拍摄跳转"""
        home.home_Page().click_camera_btn()
        time.sleep(0.5)
        self.screenshot()
        camera.camera_page().click_close_btn()

    def test_06_sec_fun_musicExtraction(self):
        """音频提取跳转"""
        home.home_Page().click_sec_musicExtraction()
        gallery.gallery_page().gallery_clip_add(1)
        time.sleep(0.5)
        self.assertTrue(edit.edit_page().is_musicExitraction_page())
        self.screenshot()
        self.d.press("back")
        gallery.gallery_page().gallery_back()