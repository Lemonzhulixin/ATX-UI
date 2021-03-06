#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py


import sys
sys.path.append('..')
from Public.Drivers import Drivers
from Public.Report import *
from TestCase.VivaVideo.test_01_Init import test_init
from Public.Decorator import *
import unittest
from Public.Test_data import *


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
    # back up old report dir 备份旧的测试报告文件夹到TestReport_backup下
    date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    backup_report(date)

    suite = unittest.TestSuite()
    suite.addTest(test_init.app_init('test_01_install'))
    suite.addTest(test_init.app_init('test_02_start'))
    suite.addTest(test_init.app_init('test_03_camera'))

    # 从install页面下载最新版本的测试app
    apk = get_apk(url=ReadConfig().get_APP_URL(), keyword=ReadConfig().get_APP_URL_KEY('XY'))
    download_apk(apk)

    # 调试用
    # apk ='apk/XiaoYing_V8.1.5_1-Abroad-Bv8.1.5-xiaoyingtest-20200420_145037.apk'
    Drivers().run(suite, apk, upload=False)
