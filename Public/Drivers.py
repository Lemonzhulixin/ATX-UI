#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py


import time
import os
import zipfile

from multiprocessing import Pool
import uiautomator2 as u2
from Public.Devices_new import *
# from Public.Devices import *
from Public.RunCases import RunCases
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage
from Public.Log import Log
from Public.ReadConfig import ReadConfig
from Public.chromedriver import ChromeDriver
from Public.Test_data import *
from Public.Report import *
from Public.mysql_operation import *


class Drivers:
    @staticmethod
    def _run_cases(run, cases):
        log = Log()
        log.set_logger(run.get_device()['model'], run.get_path() + '/' + 'client.log')
        log.i('udid: %s' % run.get_device()['udid'])

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        # base_page.set_driver(run.get_device()['ip'])

        if 'ip' in run.get_device():
            base_page.set_driver(run.get_device()['ip'])
        else:
            base_page.set_driver(run.get_device()['serial'])

        try:
            # 运行前准备
            base_page.set_fastinput_ime()  # 设置fastime输入法
            # base_page.d.shell('rm -rf /sdcard/DCIM/XiaoYingLite')   # 删除之前的导出视频
            # base_page.d.shell('rm -rf /sdcard/XiaoYingLite')   # 删除之前的导出视频
            base_page.d.shell('logcat -c')  # 清空logcat
            # 开始执行测试
            run.run(cases)

            # 结束后操作
            base_page.unwatch_device()
            base_page.set_original_ime()
            base_page.identify()

            # 将logcat文件上传到报告
            base_page.d.shell('logcat -d > /sdcard/logcat.log')
            time.sleep(2)
            base_page.d.pull('/sdcard/logcat.log', os.path.join(path.get_path(), 'logcat.log'))
            time.sleep(5)

        except AssertionError as e:
            log.e('AssertionError, %s' % e)

    def run(self, cases, apk, upload=True):

        start_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        # 根据method 获取android设备
        method = ReadConfig().get_method().strip()
        if method == 'SERVER':
            # get ATX-Server Online devices
            # devices = ATX_Server(ReadConfig().get_server_url()).online_devices()
            print('Checking available online devices from ATX-Server...')
            devices = get_online_devices()
            print('\nThere has %s alive devices in ATX-Server' % len(devices))
        elif method == 'IP':
            # get  devices from config devices list
            print('Checking available IP devices from config... ')
            devices = get_devices()
            print('\nThere has %s  devices alive in config IP list' % len(devices))
        elif method == 'USB':
            # get  devices connected PC with USB
            print('Checking available USB devices connected on PC... ')
            devices = connect_devices()
            print('\nThere has %s  USB devices alive ' % len(devices))

        else:
            raise Exception('Config.ini method illegal:method =%s' % method)

        if not devices:
            print('There is no device found,test over.')
            return

        # # 测试前准备
        # generate_test_data(devices)  # 创建测试数据 data.js

        print('Starting Run test >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i]))

        # run on every device 开始执行测试
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(run, cases,))
            time.sleep(2)
        print('Waiting for all runs done........ ')
        pool.close()
        time.sleep(1)
        pool.join()
        print('All runs done........ ')
        ChromeDriver.kill()

        end_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        #  Generate statistics report  生成统计测试报告 将所有设备的报告在一个HTML中展示

        apk_info = get_apk_info(apk['apk_path'])# 获取install apk信息
        title = "ApkUrl: %s<br />PackageName: %s<br /> Version: V%s<br />VersionCode: %s" % (
            apk['html'], apk_info["package"], apk_info["versionName"], apk_info["versionCode"])

        runs_info = create_statistics_report(runs, title=title)
        if upload:
            # 上传报告信息
            for res in runs_info:
                result_tmp = {}
                result_tmp['device_name'] = res['name']
                result_tmp['count'] = res['sum']
                result_tmp['pass'] = res['pass']
                result_tmp['fail'] = res['fail']
                result_tmp['error'] = res['error']
                result_tmp['tag'] = 'Android_' + start_time
                insert_ui_results(result_tmp)

            # 上传apk信息
            task_app_info = {}
            task_app_info['app_name'] = '小影'
            task_app_info['package_name'] = apk_info["package"]
            task_app_info['ver_name'] = apk_info["versionName"]
            task_app_info['ver_code'] = apk_info["versionCode"]
            #
            # task_app_info['channel'] = apk_info['channel']
            # task_app_info['appkey'] = apk_info["appkey"]

            task_app_info['file_name'] = apk['apk_name']
            task_app_info['tag'] = 'Android_' + start_time
            insert_ui_apks_info(task_app_info)

            # 上传task信息
            task_info = {}
            task_info['start_time'] = start_time
            task_info['end_time'] = end_time
            task_info['app_name'] = apk_info["package"]
            task_info['app_version'] = apk_info["versionName"]
            task_info['devices'] = len(runs)
            task_info['tag'] = 'Android_' + start_time
            insert_ui_tasks(task_info)

            # 压缩报告文件夹并上传
            zipname = zip_report(start_time)
            upload_report_zip(zipname)
        else:
            pass

        # 将报告文件剪切到新的目录下
        backup_report(start_time)
