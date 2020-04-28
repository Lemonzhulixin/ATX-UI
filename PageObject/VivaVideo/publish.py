#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
from Public.Log import Log

log = Log()


class publish_page(BasePage):


    @teststep
    def click_export_btn(self):
        log.i('点击保存')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_publish",text='保存').click()

    @teststeps
    def click_draft_btn(self):
        log.i('点击存草稿按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_draft",text='存草稿' ).click()

    @teststep
    def click_pop_dialog(self):
        log.i('关闭好评弹窗')
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/btnCancel").click(3)
        except:
            log.i('非首次导出，无评价弹窗')


    @teststep
    def select_export(self, inst=1):
        if inst == 1:
            log.i('点击480P导出')
            self.d(resourceId="com.quvideo.xiaoying:id/item480").click()
        elif inst == 2:
            log.i('点击720P导出')
            self.d(resourceId="com.quvideo.xiaoying:id/item720").click()
        elif inst == 3:
            log.i('点击1080P导出')
            self.d(resourceId="com.quvideo.xiaoying:id/item1080").click()
        elif inst == 4:
            log.i('点击GIF导出')
            self.d(resourceId="com.quvideo.xiaoying:id/itemGif").click()
        else:
            log.i('点击4K导出')
            self.d(resourceId="com.quvideo.xiaoying:id/item4K").click()
        time.sleep(1)


    def wait_export(self,timeout=600):
        start = time.time()
        log.i('开始导出 %s' % time.strftime("%H:%M:%S", time.localtime()))
        self.d(resourceId="com.quvideo.xiaoying:id/tvProgress").wait(timeout=2)
        if self.d(resourceId="com.quvideo.xiaoying:id/tvProgress").wait_gone(timeout=timeout):
            end = time.time()
            log.i('导出成功 %s ' % time.strftime("%H:%M:%S", time.localtime()))
            log.i('导出用时 %s' % (end - start))
            time.sleep(2)  # 等待跳转到导出成功页面
        else:
            raise Exception('导出等待超时,导出时长超过%s秒' % timeout)

    @teststep
    def sharePage_back(self,text='返回首页'):
        log.i('从导出页%s' % text)
        self.d.press("back")
        if text == '返回首页':
            self.d(resourceId="com.quvideo.xiaoying:id/menu2",text = '返回首页').click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/menu1",text = '返回编辑').click()





    @teststep
    def select_share_icon(self, text='LINE'):
        log.i('导出页面,底部分享图标 %s 点击 '% text)
        self.d(resourceId="com.quvideo.xiaoying:id/share_list_layout", scrollable=True).scroll.horiz.to(
            resourceId="com.quvideo.xiaoying:id/publish_share_icon_txt", text=text)
        time.sleep(0.5)
        x = self.d(resourceId="com.quvideo.xiaoying:id/publish_share_icon_txt", text=text).center()[0]
        y = self.d(resourceId="com.quvideo.xiaoying:id/publish_share_icon_txt", text=text).center()[1] - \
            self.d.window_size()[
                0] / 9
        log.i(x, y)
        self.d.click(x, y)

    @teststep
    def click_back_btn(self):
        log.i('分享页面,点击返回按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/img_back").click()
        time.sleep(1)


    def cancel_export(self, leave=False):
        log.i('点击导出取消按钮操作')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_cancel").click()
        if leave == True:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_export_dialog_positive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_export_dialog_negative").click()
            time.sleep(1)

    ###GIF导出

    @teststep
    def select_gif_size(self, inst=1):
        '''inst   1:480P 2:320P 3:240P'''
        log.i('点击gif尺寸按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/txtview_gif_size").click()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/popup_item_title", instance=inst - 1)
        log.i('点击%s' % ele.get_text())
        ele.click()

    @teststep
    def select_gif_fps(self, inst=1):
        '''inst   1:15fps 2:10fps 3:5fps'''
        log.i('点击gif FPS按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/txtview_gif_fps").click()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/popup_item_title", instance=inst - 1)
        log.i('点击%s' % ele.get_text())
        ele.click()

    @teststep
    def click_gif_vip_btn(self):
        log.i('点击移除5秒限制按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_vip").click()

    @teststep
    def gif_timeline_swipe(self, status=0):
        ele = self.d(resourceId="com.quvideo.xiaoying:id/gallery_timeline")
        if status == 0:
            log.i('gif timeline左滑')
            self.swipe_left(ele)
        else:
            log.i('gif timeline右滑')
            self.swipe_right(ele)

    @teststep
    def gif_timetrim_swip(self):
        log.i('gif trim操作')
        t_left = self.d(resourceId="com.quvideo.xiaoying:id/imgview_thumbnail").info['bounds']
        r = t_left['right']-t_left['left']
        self.d.swipe(int(t_left['left']), t_left['top'], t_left['right']+r, t_left['top'], duration=0.3)

        t_right = self.d(resourceId="com.quvideo.xiaoying:id/imgview_thumbnail", instance=4).info['bounds']
        self.d.swipe(int(t_right['right']), t_right['top'], t_right['left']-r, t_right['top'], duration=0.3)


    @teststep
    def get_gif_trimed_duration(self):
        log.i('获取gif视频导出trim时长')
        trim = self.d(resourceId="com.quvideo.xiaoying:id/txtview_trimed_duration").get_text().split(":")
        trim_time = float(trim[0]) * 60 + float(trim[1])
        return trim_time



    @teststep
    def gif_export_btn(self):
        log.i('gif 导出按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/share_btn_share").click()

    ## 导出结果页
    @teststep
    def result_info(self):
        log.i('导出结果页信息获取')
        self.d(resourceId="com.quvideo.xiaoying:id/result_page_item_list").wait()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/result_page_item_list")
        tmp_list = []
        for i in range(3):
            text = ele.child(className="android.widget.TextView", instance=i).get_text()
            log.i(text)
            tmp_list.append(text)
        return tmp_list

    @teststep
    def result_home_click(self):
        log.i('导出结果页，点击首页按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_draft_btns").click()
        time.sleep(0.5)

    @teststep
    def result_select_share_icon(self, inst=1):
        log.i('导出结果页，点击分享图标 inst=%s' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/btn_share_img", instance=inst - 1).click()

    @teststep
    def cancle_review(self):
        log.i('弹出点评取消操作/导出崩溃弹出点击取消')
        if self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").exists(timeout=2):
            while not self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").wait_gone(timeout=0.5):
                self.back()
        else:
            pass
        self.d(resourceId="com.quvideo.xiaoying:id/com_dialog_btn_right").click_exists(timeout=2)  # 导出崩溃弹出点击取消


if __name__ == '__main__':
    from Public.Log import Log
    from PageObject import gallery

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)

    # publish_page().cancel_export()
    # publish_page().
    print(publish_page().get_gif_trimed_duration())
