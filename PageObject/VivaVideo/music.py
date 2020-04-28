#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
from Public.Log import Log

log = Log()


class music_page(BasePage):
    '''音乐下载页面'''

    @teststeps
    def music_enter(self,text = '添加音乐'):
        """
        :param text: 添加音乐、者添加音效、添加录音
        :return:
        """
        addMusic = self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/board_container"]//*/android.view.View[2]')
        addRecord = self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/board_container"]//*/android.view.View[3]')
        addSound = self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/board_container"]//*/android.view.View[4]')

        log.i('进入音乐tab')
        self.d(text='音乐').click()
        if text == '添加音乐':
            addMusic.click()
        elif text == '添加录音':
            addRecord.click()
        else:
            addSound.click()


    @teststeps
    def audio_download(self, text="配乐"):
        log.i('下载配乐或者音效')
        if text =='配乐':
            self.d(resourceId='com.quvideo.xiaoying:id/music_item_download_btn').click()
        elif text =='音效':
            self.d(resourceId='com.quvideo.xiaoying:id/music_item_download').click()
        else:
            log.i('当前页面没有未下载的音频')
            pass
        time.sleep(5)


    @teststep
    def music_click(self, inst=1):
        log.i('点击音乐列表第%s个音乐' % inst)
        layout = self.d(resourceId="com.quvideo.xiaoying:id/mussic_item_top_layout", instance=inst - 1)
        name = layout.child(resourceId="com.quvideo.xiaoying:id/music_item_title").get_text()
        log.i('%s' % name)
        layout.click()
        return name

    @teststep
    def audio_click(self):
        log.i('点击音效列表第1个音效')
        el = self.d.xpath('//*[@resource-id="com.quvideo.xiaoying:id/music_recycle_view"]/android.widget.LinearLayout[1]')
        el.click()


    @teststep
    def music_add(self):
        self.watch_device('我知道了')
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/music_item_use_btn",text='使用').click(3)
        except:
            log.i('当前添加的是音效')
            self.d(resourceId="com.quvideo.xiaoying:id/music_item_use",text='添加').click()
        self.unwatch_device()

    @teststep
    def click_download_btn(self, inst=1):
        log.i('点击第%s个下载按钮' % inst)
        time.sleep(1)
        self.d(resourceId="com.quvideo.xiaoying:id/music_item_download", instance=inst - 1).click()
        time.sleep(5)

    @teststep
    def click_play_btn(self):
        log.i('点击播放/暂停按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/music_item_play_state").click()

    @teststep
    def delete_music(self, inst=1):
        log.i('删除列表中第%个音乐文件')
        self.d(resourceId="com.quvideo.xiaoying:id/music_rubbish_icon").click()
        self.music_click(inst)
        log.i('点击删除按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/music_rubbish_icon").click()
        time.sleep(0.5)

    @teststep
    def click_use_btn(self):
        log.i('点击添加')
        self.d(resourceId="com.quvideo.xiaoying:id/music_item_use").click()

    @teststep
    def scan_local_music(self):
        log.i('扫描本地音乐')
        self.d(resourceId="com.quvideo.xiaoying:id/list_item_music_local_scan_layout").click()
        self.d(resourceId="com.quvideo.xiaoying:id/select_all").click()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_scan").click()
        self.d(text='完成').wait(timeout=20)
        text = self.d(resourceId="com.quvideo.xiaoying:id/custom_content").get_text()
        log.i(text)
        self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()


class theme_music_page(BasePage):
    '''主题 更改配乐页面'''

    @teststep
    def click_video_audiotrack_btn(self):
        log.i('点击视频原音静音按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_video_audiotrack").click()
        time.sleep(0.5)
        message = self.get_toast_message()
        log.i('toast:%s' % message)
        return message

    @teststep
    def click_bgm_audiotrack_btn(self):
        log.i('点击背景原音静音按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_bgm_audiotrack").click()
        time.sleep(0.5)
        message = self.get_toast_message()
        log.i('toast:%s' % message)
        return message

    @teststep
    def select_audio_track_bar(self, inst=80):
        log.i('音量调节bar 设定为 百分之%s' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_audio_track_mix").info['bounds']
        y = (bar['top'] + bar['bottom']) / 2
        unit = (bar['right'] - bar['left']) / 100
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def click_reset_btn(self):
        log.i('点击重置按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_reset_music").click()
        time.sleep(0.5)

    def click_delete_btn(self):
        log.i('点击删除按')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_del_music").click()

    @teststep
    def get_music_name(self):
        log.i('获取当前音乐名称')
        name = self.d(resourceId="com.quvideo.xiaoying:id/txtview_bgm_name").get_text()
        log.i('音乐名称[%s]' % name)
        return name

    @teststep
    def click_music_name(self):
        log.i('点击音乐名称，跳转到音乐选择页面')
        self.d(resourceId="com.quvideo.xiaoying:id/txtview_bgm_name").click()
        time.sleep(1)

    @teststep
    def click_confirm_btn(self):
        log.i('点击√按钮，确认配乐设定')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_2lev_hide").click()
        time.sleep(0.5)




if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)

    music_page().music_enter('添加音效')
    music_page().audio_download('音效')
    music_page().audio_click()
    music_page().music_add()







