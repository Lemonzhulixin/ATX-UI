#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2021/3/29 16:29
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: ATX-UI
#  @File: test.py.py

import uiautomator2 as ut2


def main():
    u = ut2.connect('10.0.24.235:20020')
    print(u.info)
    u.app_start(package_name="com.quvideo.xiaoying", activity="com.quvideo.xiaoying.MainActivity")

    u(resourceId="com.quvideo.xiaoying:id/tv_edit_icon_home8_cut").click()

    u(resourceId='com.quvideo.xiaoying:id/iv_cover').click()
    u.app_stop(package_name="com.quvideo.xiaoying")

if __name__ == '__main__':

    while True:
        main()
