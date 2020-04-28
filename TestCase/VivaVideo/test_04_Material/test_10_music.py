#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PageObject.VivaVideo import home, studio, music
from Public.Decorator import *
import unittest
from Public.Test_data import *

pkg_name = ReadConfig().get_pkg_name(key='XY')

class edit_music(unittest.TestCase, BasePage):
    '''剪辑页-配乐'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_music_display(self):
        """进入配乐分类页面"""
        time.sleep(1)
        home.home_Page().click_draft_btn()
        studio.studio_page().select_draft()
        music.music_page().music_enter('添加音乐')
        time.sleep(0.5)
        self.screenshot()

    @testcase
    def test_02_music_download(self):
        """下载配乐"""
        music.music_page().audio_download('配乐')
        time.sleep(0.5)
        self.screenshot()

    @testcase
    def test_03_music_use(self):
        """使用配乐"""
        music.music_page().music_click(inst=1)
        music.music_page().music_add()
        time.sleep(0.5)
        self.screenshot()

    @testcase
    def test_04_sound_display(self):
        """进入音效分类页面"""
        time.sleep(1)
        music.music_page().music_enter('添加音效')
        time.sleep(0.5)
        self.screenshot()

    @testcase
    def test_05_sound_download(self):
        """下载音效"""
        music.music_page().audio_download('音效')
        time.sleep(0.5)
        self.screenshot()

    @testcase
    def test_06_sound_use(self):
        """使用音效"""
        music.music_page().audio_click()
        music.music_page().music_add()
        time.sleep(0.5)
        self.screenshot()