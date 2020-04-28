#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.Decorator import *
from Public.Log import Log
log = Log()


class camera_page(BasePage):
    @teststep
    def click_close_btn(self):
        log.i('点击关闭按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/cam_btn_cancel").click()

    @teststep
    def leave_select(self, leave=True):
        log.i('保存草稿弹窗点击 leave=%s' % leave)
        if leave:
            self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultNegative").click()

    @teststep
    def click_cam_ratio_btn(self):
        log.i('相机比例切换按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/cam_btn_ratio").click()

    @teststep
    def click_cam_switch_btn(self):
        log.i('点击前后摄像头切换按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/img_switch").click()
        time.sleep(2)  # waite camera load

    @teststep
    def click_cam_setting_btn(self):
        log.i('相机设置按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/cam_btn_setting").click()
        time.sleep(1)


    @teststep
    def get_aelock_tip(self):
        log.i('获取曝光锁定tip的文字')
        if self.d(resourceId="com.quvideo.xiaoying:id/layout_aelock_tip").exists:
            tip = self.d(resourceId="com.quvideo.xiaoying:id/layout_aelock_tip")
            return tip.get_text()
        else:
            raise Exception('aelock tip not found')

    @teststep
    def click_filter_btn(self):
        log.i('滤镜按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/cam_btn_filter_effect").click()

    @teststep
    def click_effect_btn(self):
        log.i('点击人脸贴纸按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/cam_btn_fb_effect").click()

    ## 小影无法定位
    @teststep
    def swipe_filter(self):
        '''
        滑动屏幕切换滤镜
        :return: 滑动后切换滤镜的名称
        '''
        self.swipe_left(steps=0.03)
        # if self.d(resourceId="com.quvideo.xiaoying:id/txt_effect_name").exists:
        #         #     effect_name = self.d(resourceId="com.quvideo.xiaoying:id/txt_effect_name").get_text()
        #         # else:
        #         #     effect_name = None
        #         # log.i('左滑后，滤镜切换为: %s ' % effect_name)
        #         # return effect_name
        self.screenshot()
        time.sleep(1)

    @teststep
    def select_filter(self, text="经典"):
        log.i('找到滤镜卷 %s 并点击'% text)
        ele = self.d(resourceId="com.quvideo.xiaoying:id/effect_listview")
        self.find_element_by_swipe_left(self.d(text=text), ele)
        time.sleep(1)
        self.d(resourceId="com.quvideo.xiaoying:id/item_fitler_parent_name", text=text).click()
        time.sleep(3)  # 等待下载完成

    @teststeps
    def choose_filter(self, text="樱花"):
        log.i('找到滤镜 %s 并点击' % text)
        ele = self.d(resourceId="com.quvideo.xiaoying:id/effect_listview")
        self.find_element_by_swipe_left(self.d(text=text), ele)
        time.sleep(1)  # 等待主题馆展开
        self.d(resourceId="com.quvideo.xiaoying:id/item_fitler_child_name", text=text).click()



    @teststep
    def select_camera_modes(self, inst=1):
        '''
        相机模式选择 0-->自拍美颜  1&other-->高清相机 2-->音乐视频
        :param inst:
        '''
        if inst == 0:
            self.d(text='自拍美颜').click()
            log.i('点击自拍美颜')
        elif inst == 2:
            self.d(text='音乐视频').click()
            log.i('点击音乐视频')
        else:
            self.d(text='高清相机').click()
            log.i('点击高清相机')
        time.sleep(4)  # waite camera load

    @teststep
    def select_fb_level(self, inst=2):
        '''
        设置美颜程度
        :param inst: inst  0~4之间任意间隔0.2的数字  exp 0.2、0.4、...1.8、2.0
        '''
        log.i('设置美颜程度为 %s' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/txtseekbar_fb_level").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 22
        x = unit + bar['left'] + inst * unit * 5
        self.d.long_click(x, y)

    @teststep
    def select_effect_bar(self, inst=2):
        '''人脸贴纸 底部bar的选择
        :param inst: 1、2、3、4、5
        '''
        log.i('人脸贴纸 底部bar选择第%s个tab' % inst)
        # self.d(className="android.support.v7.app.ActionBar$b", instance=inst - 1).click()
        self.d(resourceId="com.quvideo.xiaoying:id/img_tab_icon", instance=inst - 1).click()

    @teststep
    def effect_img_click(self, inst=1):
        log.i('点击人脸贴纸第 %s 个贴纸内容' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_filter_thumb", instance=inst - 1).click()

    # @teststep
    # def effect_downloaded(self, inst=1):
    #     a = self.d(resourceId="com.quvideo.xiaoying:id/main_layout", instance=inst).info
    #     log.i(a)

    @teststep
    def click_music_btn(self):
        '''点击音乐按钮
        :return:按钮的名称
        '''
        log.i('点击选择音乐按钮')
        text = self.d(resourceId="com.quvideo.xiaoying:id/music_title").get_text()
        self.d(resourceId="com.quvideo.xiaoying:id/layout_music_info").click()
        log.i('选择音乐按钮的文字为 %s' % text)

    @teststep
    def music_rerecord_select(self, change=False):
        '''重录弹窗选择，change=False 更换音乐重录'''
        log.i('重录弹窗选择')
        # if self.d(resourceId="com.quvideo.xiaoying:id/contentListView").wait():
        if self.d(resourceId="com.quvideo.xiaoying:id/md_contentRecyclerView").wait():
            if change:
                self.d(text="更换音乐重录").click()
                log.i('点击更换音乐重录')
            else:
                self.d(text="直接重录").click()
                log.i('点击直接重录')
        else:
            raise Exception('rerecord selection does not appear')

    @teststep
    def click_record_btn(self, duration=0.01):
        '''
        录制按钮的操作，默认点击  设置duration后为长按
        :param duration: 按住录制按键的时间，单位/秒
        '''
        log.i('点击、长按录制按钮，时长为%s秒' % duration)
        self.d(resourceId="com.quvideo.xiaoying:id/btn_rec").long_click(duration=duration)

    @teststep
    def click_next_btn(self):
        log.i('下一步按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/cam_btn_next").click()

    @teststep
    def click_delete_btn(self):
        log.i('撤销按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_cam_btn_text_delete").click()
        time.sleep(0.2)

    def get_record_info(self):
        '''
        获取录制的时长和录制片段数字
        :return: tuple（total_time, count） exp：(2.8, 2)
        '''
        log.i('获取录制的时长和录制片段数字')
        if self.d(resourceId="com.quvideo.xiaoying:id/cam_recording_total_time").exists:
            total_time = self.d(resourceId="com.quvideo.xiaoying:id/cam_recording_total_time").get_text()
            count = self.d(resourceId="com.quvideo.xiaoying:id/cam_clip_count").get_text()
            total_time = float(total_time)
            count = int(count)
            log.i('时长%s秒,录制片段数%s个' % (total_time, count))
            return total_time, count
        else:
            log.i('There has no record yet')



class camerasetting_page(BasePage):
    @teststep
    def switch_flashlight(self):
        log.i('相机设置 闪光灯开关按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/icon_tool_flashlight").click()
        time.sleep(1)

    @teststep
    def switch_grid(self):
        log.i('相机设置 九宫格按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/icon_tool_grid").click()
        time.sleep(1)

    @teststep
    def select_countdown_time(self):
        log.i('相机设置 倒计时按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/icon_tool_time").click()
        time.sleep(1)

    @teststep
    def switch_aelock(self):
        log.i('相机设置 曝光锁定 按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/icon_tool_aelock").click()
        time.sleep(1)

    @teststep
    def select_record_speed(self, inst=1):
        '''
        设置拍摄速度
        :param inst: inst  0~4之间任意间隔0.2的数字  exp 0.2、0.4、...1.8、2.0
        '''
        log.i('设置拍摄速度为 %s' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/speed_bar").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 24
        x = 2 * unit + bar['left'] + inst * unit * 5
        self.d.long_click(x, y)
        time.sleep(1)


class camerapreview_page(BasePage):

    @teststep
    def is_camerapreview(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/edit_video_layout").wait()
        return status

    @teststep
    def click_back_btn(self):
        log.i('点击 返回 按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_back_btn").click()

    @teststep
    def click_save_btn(self):
        log.i('点击 存草稿 按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_draft").click()

    @teststep
    def click_share_btn(self):
        log.i('点击 保存/上传 按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_publish").click()

    @teststep
    def click_edit_video_btn(self):
        log.i('点击 编辑该视频 按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/edit_video_layout").click()

    @teststep
    def click_play_btn(self):
        log.i('点击 播放 按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/seekbar_play").click()

    @teststep
    def get_seekbar_time(self):
        '''
        获取seekbar上的播放时间和视频时长
        :return:tuple（cur_time, duration_time） exp：(0.00, 0.01)
        '''
        log.i('获取seekbar上的播放时间和视频时长')
        cur_time = self.d(resourceId="com.quvideo.xiaoying:id/txtview_cur_time").get_text()
        duration_time = self.d(resourceId="com.quvideo.xiaoying:id/txtview_duration").get_text()
        log.i('视频时长 %s 当前播放到%s' % (duration_time, cur_time))
        return cur_time, duration_time


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # Camera_Page().leave_select(False)
    # Camera_Page().effect_downloaded(2)
    # Camera_Page().click_delete_btn()
    # Camera_Page().click_delete_btn()
    # log.i(Camera_Page().get_record_info())
    # Camera_Page().click_delete_btn()
    # Camera_Page().click_delete_btn()
    # log.i(Camera_Page().get_record_info())
    # log.i(camerapreview_page().get_seekbar_time())
    camera_page().select_filter('生色')