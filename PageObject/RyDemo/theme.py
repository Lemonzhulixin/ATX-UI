#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class theme(BasePage):
    # ————————————————————————
    # 主题相关
    # ————————————————————————
    @teststep
    def enter_edit_page(self):
        # log.i('进入帧处理主界面')
        # try:
        #     self.d(resourceId='com.quvideo.application:id/llFrame').click(1)
        # except Exception:
        #     log.i('当前已经在帧处理主界面')


        self.d(description="更多选项").click(1)
        self.d.xpath('//android.widget.ListView/android.widget.LinearLayout[3]').click(1)


    @teststep
    def theme_use(self,theme_path):
        log.i('滑动到下一个页面')
        text = self.d.xpath('//*[@text="字幕"]')
        self.swipe_left(text,0.8)
        time.sleep(0.5)

        try:
           self.d(resourceId="com.quvideo.application:id/tvContent", text="主题").click(1)
        except Exception:
            log.i('当前已经在主题选择页面')

        log.i('选择主题')
        self.d.xpath(theme_path).click()
        time.sleep(5)



if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    p = '//*[@resource-id="com.quvideo.application:id/clip_recyclerview"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]'
    theme().theme_use(p)



