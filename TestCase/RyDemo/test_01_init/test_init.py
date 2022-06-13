#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PageObject.RyDemo import filter
from Public.Decorator import *
import unittest
from Public.Test_data import *

# apk = get_apk(url='http://www1.xiaoying.co/Android/vivavideo/install.html',keyword='XiaoYing_V8')
# download_apk(apk)
# apk ='/Users/zhulixin/Desktop/UI/TestCase/VivaVideo/apk/XiaoYing_V8.1.5_1-Abroad-Bv8.1.5-xiaoyingtest-20200420_145037.apk'
pkg_name = ReadConfig().get_pkg_name(key='RY')
apk = get_apk(url=ReadConfig().get_APP_URL(),keyword=ReadConfig().get_APP_URL_KEY('RY'))

class app_init(unittest.TestCase, BasePage):
    '''初始化'''

    @classmethod
    def setUpClass(cls):
        cls.d.app_stop_all()
        cls.d.app_start(pkg_name)

    @classmethod
    def tearDownClass(cls):
        cls.unwatch_device()
        cls.d.app_stop(pkg_name)

    @testcase
    def test_01_install(self):
        '''小影apk安装'''
        self.d.app_stop(pkg_name)
        # print(get_apk_info(apk))
        self.d.app_uninstall(pkg_name)
        # self.local_install(apk)
        # 从install页面下载
        print(get_apk_info(apk['apk_path']))
        self.d.app_uninstall(pkg_name)
        self.local_install(apk['apk_path'])

    @testcase
    def test_02_start(self):
        """启动并消除各种弹窗"""
        self.watch_device('允许|始终允许|取消|立即删除|同意并开始使用|继续使用')   #华为删除app后弹出清理弹窗
        self.d.app_start(pkg_name)
        time.sleep(5)
        self.screenshot()
        filter.filter().enter_edit_page()
        time.sleep(5)
        self.unwatch_device()
