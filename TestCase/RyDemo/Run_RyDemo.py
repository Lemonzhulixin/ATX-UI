#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py


import sys
sys.path.append('..')
from Public.CaseStrategy import CaseStrategy
from Public.Drivers import Drivers
from Public.Report import *
from Public.Test_data import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
    # back up old report dir 备份旧的测试报告文件夹到TestReport_History下
    date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    backup_report(date)

    cs = CaseStrategy()
    cases = cs.collect_cases(suite=False)

    # 从install页面下载最新版本的测试app
    apk = get_apk(url=ReadConfig().get_APP_URL(), keyword=ReadConfig().get_APP_URL_KEY('RY'))
    download_apk(apk)

    # 调试用
    # apk = 'apk/EngineDemo-Bdev_rongyao_20210727_195715.apk'

    # while True:
    #     Drivers().run(cases, apk, upload=False)

    Drivers().run(cases, apk, upload=False)