#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2021/11/9 15:16
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: ATX-UI
#  @File: testDemo.py


#
import time
import uiautomator2 as u2

def main():

    d = u2.connect_usb('CLB7N18808001922')

    print('启动小影')
    d.app_start('com.quvideo.xiaoying')

    print('创建新工程')
    d(resourceId="com.quvideo.xiaoying:id/ll_new_project").click()

    print('选择镜头')
    d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/recycler_view"]/android.widget.RelativeLayout[2]').click()

    print('下一步')
    d(resourceId="com.quvideo.xiaoying:id/btn_next", text='下一步').click()

    print('导出')
    d(resourceId="com.quvideo.xiaoying:id/llDraftSave").click()

    print('480p')
    d(resourceId="com.quvideo.xiaoying:id/item480").click()

    time.sleep(5)

    # print('关闭小影')
    # d.app_clear('com.quvideo.xiaoying')

    print('测试结束')

if __name__ == '__main__':
    main()
