#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/5/6 2:40 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: ATX-UI
#  @File: exportCount.py

from Public.Decorator import *
from PageObject.VivaVideo import edit, home, publish
from Public.Log import Log
log = Log()

class add_Test(BasePage):

    @teststep
    def addClip(self,number):
        self.d.app_start(package_name="com.quvideo.xiaoying",activity="com.quvideo.xiaoying.MainActivity")

        home.home_Page().click_edit_btn()
        time.sleep(0.5)
        log.i('开始添加镜头')
        for i in range(number):
            el = self.d(resourceId='com.quvideo.xiaoying:id/iv_cover')
            el[i].click()

        log.i('点击下一步进入编辑页')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_next", text='下一步').click()

        log.i('点击添加按钮')
        self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/board_container"]'
                     '/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView[3]').click()

        log.i('开始添加新镜头')
        self.d(resourceId='com.quvideo.xiaoying:id/iv_cover').click()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_next", text='下一步').click()

        log.i('判断添加镜头是否成功')
        new_clip = self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/board_container"]'
                        '/android.view.ViewGroup[2]/android.widget.FrameLayout[1]/android.view.ViewGroup[2]')
        try:
            new_clip.click()
            log.i('镜头添加成功')
            self.d.app_stop("com.quvideo.xiaoying")
        except:
            raise Exception("镜头添加失败")


if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    while True:
        add_Test().addClip(1)