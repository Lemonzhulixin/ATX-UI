#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py


import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')
from Public.Drivers import Drivers
from Public.Report import *
import unittest
from TestCase.VivaVideo.test_01_Init import test_init
from TestCase.VivaVideo.test_04_Material import test_01_theme, test_12_export

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
    # back up old report dir 备份旧的测试报告文件夹到TestReport_backup下
    date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    backup_report(date)

    suite = unittest.TestSuite()
    suite.addTest(test_01_theme.material_theme('test_01_theme_display'))
    suite.addTest(test_01_theme.material_theme('test_02_theme_use'))
    suite.addTest(test_01_theme.material_theme('test_03_theme_material'))
    suite.addTest(test_01_theme.material_theme('test_04_theme_preview'))

    # apk = get_apk(url='http://www1.xiaoying.co/Android/vivavideo/install.html',keyword='XiaoYing_V8')
    # download_apk(apk)

    apk ='apk/XiaoYing_V8.1.5_1-Abroad-Bv8.1.5-xiaoyingtest-20200420_145037.apk'
    Drivers().run(suite, apk, upload=False)
