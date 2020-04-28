#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.Decorator import *
import unittest
from PageObject.VivaVideo import home, login
from Public.Test_data import *


pkg_name = ReadConfig().get_pkg_name(key='XY')

class QQ_login(unittest.TestCase, BasePage):
    '''QQ登录'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_start(package_name=pkg_name, activity='com.quvideo.xiaoying.MainActivity')

    @classmethod
    def tearDownClass(cls):
        cls.d.app_stop(pkg_name)

    @testcase
    def test_QQlogin(self):
        '''QQ登录'''
        home.home_Page().click_me_btn()
        login.login_page().click_login_btn()
        login.login_page().login_QQ()
        time.sleep(0.5)
        self.assertTrue(login.login_page().is_login_success())
        self.screenshot()
        login.login_page().logout()
        self.assertTrue(login.login_page().is_logout_success())
