#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.Decorator import *
from PageObject.VivaVideo import edit
from Public.Log import Log
log = Log()

class gallery_page(BasePage):
    '''gallery页面'''


    @teststep
    def is_gallery_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/iv_cover").wait()
        return status

    @teststep
    def gallery_back(self):
        self.d(resourceId="com.quvideo.xiaoying:id/btn_back").click()


    @teststep
    def gallery_clip_add(self, number):
        time.sleep(0.5)
        log.i('开始添加镜头')
        for i in range(number):
            el =self.d(resourceId='com.quvideo.xiaoying:id/iv_cover')
            el[i].click()
        log.i('点击下一步进入编辑页')
        self.screenshot()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_next", text='下一步').click()


    @teststep
    def select_gallery(self, select=1):
        '''
        点击切换视频 、图片
        :param select: 1-->video  other--> photo
        '''
        log.i('gallery视频 、图片切换')
        if select == 1:
            if self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").wait(3):    # abtest Gallery_Filter_Refine_Android
                self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").click()
                self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_video_tab").click()
            else:
                self.d(resourceId="com.quvideo.xiaoying:id/b_video_tab").click()
            log.i('切换到视频')
        else:
            if self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").wait(3):
                self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").click()
                self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_photo_tab").click()
            else:
                self.d(resourceId="com.quvideo.xiaoying:id/b_photo_tab").click()
            log.i('切换到图片')

        # gallery_title = self.d(resourceId="com.quvideo.xiaoying:id/gallery_title").get_text()
        # log.i('当前gallery在 %s 选择页面' % gallery_title)
        # return gallery_title

    @teststep
    def select_gallery_tab(self, select=1):
        '''
        全部、其他相册点击切换
        :param select: 0-->全部  1&other-->其他相册
        :return:
        '''
        if select == 0:
            log.i('切换到全部')
            self.d(resourceId="com.quvideo.xiaoying:id/tab_gallery_mode_item").click()
        else:
            log.i('切换到其他相册')
            self.d(resourceId="com.quvideo.xiaoying:id/tab_gallery_mode_item", instance=1).click()

    @teststeps
    def click_folder(self, name='AutoTest'):
        '''
        其他相册，点击文件夹
        :param name: folder name textContains exp: '系统' will click folder'系统相册'
        '''
        log.i('其他相册，找到 %s 文件夹 并点击进入' % name)
        if self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager", scrollable=True).exists:
            self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager", scrollable=True).fling.toBeginning()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/gallery_viewpager")
        self.find_element_by_swipe_up(value=self.d(textContains=name), element=ele, steps=0.2, max_swipe=10)
        # self.swipe_up(element=ele)
        # 点击跳转失败重试
        if name == '扫描试试':
            for i in range(4):
                if not self.d(resourceId="com.quvideo.xiaoying:id/btn_edit_photo").wait(timeout=0.5):
                    # y = rect['top'] - self.d.window_size()[0]/3
                    # self.d.click(x, y)
                    self.swipe_up(ele)
                    self.d(text='扫描试试').click()
                    time.sleep(0.5)
                else:
                    break
        else:
            for i in range(4):
                if not self.d(resourceId="com.quvideo.xiaoying:id/gallery_detail_listview").wait(timeout=0.5):
                    self.swipe_up(ele)  # 找到文件夹后 在上滑一次 放在底部banner遮挡
                    rect = self.d(textContains=name).info['bounds']
                    x = rect['right']
                    y = rect['top'] - self.d.window_size()[0] / 4.5
                    self.d.click(x, y)
                    time.sleep(0.5)
                else:
                    pass

    @teststep
    def select_video_clip(self, inst=1, trim=False):
        '''
        clip选择，点击视频缩略图
        :param instance: inst=n 点击第n个clips
        '''
        if trim:
            log.i('视频clips选择，点击第%s 个clip剪刀' % inst)
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_gallery_preview_layout", instance=inst - 1).click()
            time.sleep(1)
        else:
            log.i('视频clips选择，点击第%s 个clip图标' % inst)
            self.d(resourceId="com.quvideo.xiaoying:id/img_icon", instance=inst - 1).click()
            time.sleep(1)

    @teststep
    def select_photo_clip(self, inst=1, preview=False):
        '''
        选择图片
        :param inst: inst=n 点击第n个clips
        :param preview: if True click gallery_preview_button
        :return:
        '''
        log.i('图片clips选择 点击第%s个clip 进入预览=%s' % (inst, preview))
        if not preview:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).sibling(
                className="android.widget.RelativeLayout").click()

    @teststep
    def click_up_down(self):
        log.i('clipboard升起、收回的按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_body").click()

    @teststep
    def delete_clip(self, inst=1):
        log.i('删除clipboard上第%s个clip' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_delete", instance=inst - 1).click()
        time.sleep(0.5)

    @teststep
    def drag_clip(self, start=2, end=1):
        log.i('拖动第%s个clip到第%s个clip的位置' % (start, end))

        start_clip = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=start - 1)
        # start.click()
        end_clip = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=end - 1).info["bounds"]
        if start > end:
            start_clip.drag_to(end_clip["left"], end_clip["top"])
        else:
            start_clip.drag_to(end_clip["right"], end_clip["bottom"])

        # start_center = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=start - 1)
        # end_center = self.d(resourceId="com.quvideo.xiaoying:id/icon", instance=end - 1).center()
        # start_center.drag_to(end_center[0], end_center[1])

    @teststep
    def click_next_btn(self):
        log.i('点击下一步跳转到编辑页面')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_storyboard_next_btn").click()
        time.sleep(2)

    @teststep
    def click_close_btn(self):
        log.i('点击×按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def leave_select(self, leave=True):
        '''是否保存草稿弹窗选择，leave=True 丢弃'''
        log.i('保存草稿弹窗，点击丢弃=%s ' % leave)
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultNegative").click()
        time.sleep(1)

    def try_scan(self):
        log.i('快速扫描视频')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_edit_photo").click()
        self.d(text='完成').wait(timeout=40)
        text = self.d(resourceId="com.quvideo.xiaoying:id/custom_content").get_text()
        log.i(text)
        self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()
        return text


class videotrim_page(BasePage):
    '''视频剪取页面'''

    @teststep
    def is_videotrim_page(self):
        log.i('判断是否在trim页面')
        status = self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_import").exists(timeout=3)
        return status

    @teststep
    def get_trim_time(self):
        log.i('获取trim 时长')
        # t = self.d(resourceId="com.quvideo.xiaoying:id/txtview_trimed_duration").get_text()
        time_text = self.d(resourceId="com.quvideo.xiaoying:id/ve_split_right_time").get_text()
        trim_time = float(time_text[0]) * 60 + float(time_text[1])
        log.i('时长为 %s' % trim_time)
        return trim_time


    @teststeps
    def trim_swipe_new(self):
        log.i('左右滑动trim及微调trim，只有初次进入才能操作成功（trimbar无法定位）')
        log.i('original clip time is：%s 秒' % self.get_trim_time())
        trim = self.d(resourceId="com.quvideo.xiaoying:id/ve_gallery").info['bounds']
        unit = int(trim["right"] - trim["left"]) / 7
        y = int(trim["top"] + (trim["bottom"] - trim["top"]) / 2)
        self.d.swipe(int(trim["left"]) + unit / 4, y, int(trim["left"]) + 3 * unit, y, duration=0.1)
        log.i('after left_trim swipe clip time is：%s 秒' % self.get_trim_time())
        edit.edit_page().preview_swipe_left()
        log.i(self.get_trim_time())
        self.d.swipe(int(trim["right"]) - unit / 4, y, int(trim["right"]) - 3 * unit, y, duration=0.1)
        log.i('after right_trim swipe time is：%s 秒' % self.get_trim_time())
        edit.edit_page().preview_swipe_right()
        log.i(self.get_trim_time())

    @teststep
    def click_ratate_btn(self):
        log.i('点击旋转按钮')
        # self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_ratate").click()
        self.d(resourceId="com.quvideo.xiaoying:id/layout_rotate").click()
        time.sleep(1)

    @teststep
    def click_crop_btn(self):
        log.i('点击crop按钮')
        # self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_crop").click()
        self.d(resourceId="com.quvideo.xiaoying:id/layout_crop").click()
        time.sleep(1)

    @teststep
    def click_start_trim_btn(self):
        log.i('点击剪刀按钮')
        # self.d(resourceId="com.quvideo.xiaoying:id/btn_start_trim").click()
        self.d(resourceId="com.quvideo.xiaoying:id/layout_trim").click()
        time.sleep(1)

    @teststep
    def click_add_btn(self):
        log.i('点击添加按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_import").click_exists()
        time.sleep(1)

    @teststep
    def click_play_btn(self):
        log.i('播放按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/previewview").click()
        time.sleep(2)

    @teststep
    def click_close_btn(self):
        log.i('点击关闭按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def leave_select(self, leave=True):
        log.i('放弃操作弹窗选择 确认放弃=%s' % leave)
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultNegative").click()


class picture_view_page(BasePage):

    @teststep
    def click_seclet_btn(self):
        log.i('点击勾选按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_del_clip").click()
        time.sleep(0.5)

    @teststep
    def click_ratate_btn(self):
        log.i('点击旋转按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_ratate").click()
        time.sleep(0.5)

    @teststep
    def click_add_btn(self):
        log.i('点击添加按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_confirm").click()
        time.sleep(1)


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # gallery_page().select_gallery(1)
    # gallery_page().select_gallery_tab(1)
    # print(gallery_page().is_gallery_page())
    gallery_page().gallery_clip_add(3)
