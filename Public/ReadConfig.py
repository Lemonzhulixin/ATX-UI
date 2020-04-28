#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py


import configparser
import os


proDir = os.path.split(os.path.realpath(__file__))[0]
#将path分割成路径名和文件名
configPath = os.path.join(proDir, "config.ini")
#将多个路径组合后返回

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_method(self):
        value = self.cf.get("DEVICES", 'method')
        return value

    def get_server_url(self):
        value = self.cf.get("DEVICES", "server")
        return value

    def get_server_udid(self):
        value = self.cf.get("DEVICES", "udid")
        return value.split('|')

    def get_devices_ip(self):
        value = self.cf.get("DEVICES", "IP")
        return value.split('|')

    def get_server_token(self):
        value = self.cf.get("DEVICES", "token")
        return value

    def get_apk_url(self):
        value = self.cf.get("APP", "apk_url")
        return value

    def get_apk_path(self):
        value = self.cf.get("APP", "apk_path")
        return value

    def get_pkg_name(self, key):
        if key == 'XY':
           value = self.cf.get("APP", "pkg_name_XY")
           return value
        elif key =='SP':
           value = self.cf.get("APP", "pkg_name_SP")
           return value
        elif key == 'TP':
            value = self.cf.get("APP", "pkg_name_TP")
            return value
        elif key == 'VC':
            value = self.cf.get("APP", "pkg_name_TP")
            return value

    def get_APP_URL(self):
        value = self.cf.get("APP", "URL")
        return value

    def get_APP_URL_KEY(self, key):
        if key == 'XY':
            value = self.cf.get("APP", "KEY_XY")
            return value
        elif key =='SP':
             value = self.cf.get("APP", "KEY_SP")
             return value
        elif key == 'TP':
             value = self.cf.get("APP", "KEY_TP")
             return value
        elif key == 'VC':
             value = self.cf.get("APP", "KEY_VC")
             return value

    def get_testdata(self, name):
        value = self.cf.get("TESTDATA", name)
        return value.split('|')


if __name__ == '__main__':
    print(ReadConfig().get_pkg_name('VC'))
    print(ReadConfig().get_testdata('userName'))
    print(ReadConfig().get_testdata('PWD'))