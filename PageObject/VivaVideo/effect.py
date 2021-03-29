#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *


class effect_page(BasePage):
    '''素材效果页面 '''

    @teststep
    def select_effect_edit_tool(self, text="字幕"):
        log.i('素材效果功能位 点击 %s' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/effect_tool_rcview", scrollable=True).scroll.horiz.to(
            text=text)
        time.sleep(0.5)
        if self.d(text=text).exists:
            self.d(text=text).click()
            time.sleep(2)
            return True
        else:
            log.i("找不到效果控件-->%s" % text)
            return False

    @teststep
    def click_effect_play_btn(self):
        log.i('效果页面的播放/暂停按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_play").click()

    @teststep
    def get_effect_seek_time(self):
        '''获取效果页面的播放时长和视频总时长'''
        cur = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_current_time").get_text().split(":")
        cur_time = float(cur[0]) * 60 + float(cur[1])
        total = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_duration").get_text().split(":")
        total_time = float(total[0]) * 60 + float(total[1])
        log.i('获取效果页面 播放时长:%s 视频总时长:%s' % (cur_time, total_time))
        return cur_time, total_time

    @teststep
    def effect_view_swipe_left(self):
        log.i('素材效果页seekbar左滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_gallery")
        BasePage().swipe_left(ele, steps=0.2)
        time.sleep(1)

    @teststep
    def effect_view_swipe_rigth(self):
        log.i('素材效果页seekbar右滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/video_editor_seek_gallery")
        BasePage().swipe_right(ele, steps=0.2)
        time.sleep(1)

    @teststep
    def click_download_btn(self):
        log.i('点击下载按钮')
        if self.d(resourceId="com.quvideo.xiaoying:id/btn_roll_bubble_download_state").wait(timeout=1):
            text = self.d(resourceId="com.quvideo.xiaoying:id/btn_roll_bubble_download_state").get_text()
            if text == '下载':
                self.d(resourceId="com.quvideo.xiaoying:id/btn_roll_bubble_download_state").click()
                time.sleep(10)  # 等待字幕下载完成
                return True
            else:
                print('按键为%s 不执行点击操作' % text)
                return False
        else:
            log.i('没有下载按钮')
            return True

    @teststep
    def select_top_tab(self, inst=1):
        '''字幕\贴纸\FX 顶部TAB点击 '''
        log.i('选择item_layout顶部的第%s个tab' % inst)
        if self.d(resourceId="com.quvideo.xiaoying:id/item_layout").exists:  # 字幕\贴纸
            self.d(resourceId="com.quvideo.xiaoying:id/item_icon", instance=inst - 1).click()
            # self.d(resourceId="com.quvideo.xiaoying:id/item_layout", instance=inst - 1).click()
            time.sleep(1)
        else:  # FX
            self.d(resourceId="com.quvideo.xiaoying:id/iv_thumb", instance=inst - 1).click()
            time.sleep(1)

    @teststep
    def select_subtitle_icon(self, inst=1):
        log.i('点击第列表第 %s字幕/贴纸' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/div_roll_thumb", instance=inst - 1).click()
        time.sleep(1)

    @teststep
    def click_download_more_btn(self):
        log.i('点击更多按钮')
        if self.d(resourceId="com.quvideo.xiaoying:id/ib_download").exists:  # 字幕\贴纸
            self.d(resourceId="com.quvideo.xiaoying:id/ib_download").click()
            time.sleep(1)
        else:  # FX 特效
            self.d(resourceId="com.quvideo.xiaoying:id/iv_download_more").click()
            time.sleep(1)


class audio_page(BasePage):
    '''多段配乐'''

    @teststep
    def click_audio_operation_btn(self):
        '''添加\删除\完成  按钮点击'''
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_editor_audio_operation").exists(timeout=2):
            text = self.d(resourceId="com.quvideo.xiaoying:id/tv_editor_audio_operation").get_text()
            log.i('点击按钮 %s' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/tv_editor_audio_operation").click()
            time.sleep(1)
            return text
        else:
            raise Exception('找不到配乐操作按钮')

    @teststep
    def select_voice_bar(self, inst=30):
        '''设定配乐的音量bar inst 不是很精准'''
        log.i('设置配乐的音量为 %s ' % inst)
        if self.d(resourceId="com.quvideo.xiaoying:id/seekbar_editor_effect_audio_volume").wait(timeout=5):
            ele = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_editor_effect_audio_volume").info['bounds']
            y = (ele['bottom'] + ele['top']) / 2
            unit = (ele['right'] - ele['left']) / 100
            x = 2 * unit + ele['left'] + inst * unit
            self.d.click(x, y)
            time.sleep(1)
        else:
            raise Exception('没有找到音乐音量bar')

    @teststep
    def click_music_fade_btn(self, status=0):
        if status == 0:
            log.i('点击音乐渐入开关按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/iv_editor_music_fade_in").click()
        else:
            log.i('点击音乐渐出开关按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/iv_editor_music_fade_out").click()
        toast = self.get_toast_message()
        log.i('toast is: %s' % toast)
        time.sleep(2)
        return toast


class subtitle_page(BasePage):
    '''字幕\贴纸'''

    @teststep
    def click_subtitle_operation_btn(self):
        '''添加\删除\完成  按钮点击'''
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_subtitle_op_btn").wait(timeout=3):
            text = self.d(resourceId="com.quvideo.xiaoying:id/tv_subtitle_op_btn").get_text()
            log.i('点击按钮 %s' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/tv_subtitle_op_btn").click()
            time.sleep(1)
            return text
        else:
            raise Exception('找不到字幕操作按钮')

    @teststep
    def select_subtitle_tab(self, inst=1):
        '''点击字幕底部的tab'''
        if inst == 1:
            log.i('点击动态字幕tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_animtitle").click()
        elif inst == 2:
            log.i('点击其他字幕tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_subtitle").click()
        elif inst == 3:
            log.i('点击字体tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_font").click()
        elif inst == 4:
            log.i('点击对齐tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_align").click()
            # self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_stroke").click()
        # elif inst == 5:
        #     log.i('点击字幕格式按(阴影\对齐方式')
        #     self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_more").click()
        else:
            raise Exception('字幕tab inst超出范围')
        time.sleep(1)

    @teststep
    def select_anim_text(self, inst=1):
        log.i('点击第%s个动态字幕' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/item_layout", instance=inst + 2).click()
        time.sleep(5)  # 等待字幕预览加载完

    @teststep
    def subtitle_swipe_left(self):
        log.i('字幕列表左滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/recycler_view_subtitle")
        self.swipe_left(element=ele, steps=0.2)
        time.sleep(1)

    @teststep
    def subtitle_swipe_rigth(self):
        log.i('字幕列表右边滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/recycler_view_subtitle")
        self.swipe_right(element=ele, steps=0.2)
        time.sleep(1)

    @teststeps
    def text_subtitle(self, text='这是字幕这是字幕这是字幕'):
        '''点击字幕输入文字'''
        self.set_fastinput_ime()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/editor_fake_layout").info['bounds']
        x = (ele['left'] + ele['right']) / 2
        unit = (ele['bottom'] - ele['top']) / 10
        y = ele['bottom'] - unit
        self.d.click(x, y)
        self.d(resourceId="com.quvideo.xiaoying:id/edit_text").click()
        time.sleep(1)
        self.d.clear_text()
        self.d(resourceId="com.quvideo.xiaoying:id/edit_text").set_text(text)
        time.sleep(1)
        self.d(resourceId="com.quvideo.xiaoying:id/buttonDefaultPositive").click()
        time.sleep(1)

    @teststep
    def _select_font_setting_tab(self, inst=1):
        '''字幕设置顶部tab点击'''
        if inst == 1:
            log.i('点击字体按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/tab_font_style_tv").click()
        elif inst == 2:
            log.i('点击颜色按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/tab_font_color_tv").click()
        elif inst == 3:
            log.i('点击描边按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/tab_font_stroke_tv").click()
        elif inst == 4:
            log.i('点击阴影按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/tab_font_shadow_tv").click()
        else:
            raise Exception('顶部tab inst超出范围 isnt=%s' % inst)

    @teststep
    def select_subtitle_font(self, inst=1):
        '''选择字体'''
        self._select_font_setting_tab(1)
        if inst == 0:
            log.i('点击添加本地字体按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_subtitle_font_add_local_layout").click()
        else:
            log.i('点击第%s个字体' % inst)
            self.d(resourceId="com.quvideo.xiaoying:id/rl_subtitle_font_item_layout", instance=inst - 1).click()
            time.sleep(6)  # 等待字体下载完成

    @teststep
    def select_text_color(self, inst=10):
        '''
        设置字幕颜色背景颜色
        :param inst:[1:28]任意整数
        :return:
        '''
        self._select_font_setting_tab(2)
        log.i('设置字幕颜色背景颜色,inst=%s' % inst)
        ele = self.d(resourceId="com.quvideo.xiaoying:id/multicolor_bar_subtitle").info['bounds']
        y = (ele['bottom'] + ele['top']) / 2
        unit = (ele['right'] - ele['left']) / 30
        x = 1 * unit + ele['left'] + unit * inst
        self.d.click(x, y)

    @teststep
    def select_stroke_color(self, inst=10):
        '''
        设置描边颜色背景颜色
        :param inst:[1:28]任意整数
        :return:
        '''
        self._select_font_setting_tab(3)
        log.i('设置描边颜色背景颜色 inst=%s' % inst)
        ele = self.d(resourceId="com.quvideo.xiaoying:id/multicolor_bar_stroke").info['bounds']
        y = (ele['bottom'] + ele['top']) / 2
        unit = (ele['right'] - ele['left']) / 30
        x = 1 * unit + ele['left'] + unit * inst
        self.d.click(x, y)

    @teststep
    def select_stroke_alpha(self, inst=50):
        '''
        设置描边程度
        :param inst:[0:99]任意整数
        :return:
        '''
        self._select_font_setting_tab(3)
        log.i('设置描边程度 inst= %s' % inst)
        ele = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_stroke").info['bounds']
        y = (ele['bottom'] + ele['top']) / 2
        unit = (ele['right'] - ele['left']) / 100
        x = ele['left'] + unit * inst
        self.d.click(x, y)

    @teststep
    def click_shadow_switch(self):
        self._select_font_setting_tab(4)
        log.i('点击字幕阴影开关')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_import_finish").click()

    @teststep
    def click_align_mode(self, inst=1):
        '''
        点击字幕对齐方式
        :param inst: 1:左对齐 2:居中 3:右对齐
        :return:
        '''
        mod = ['1:左对齐', '2:居中', '3:右对齐']
        log.i('点击字幕对齐方式:%s' % mod[inst - 1])
        self.d(className="android.widget.RadioButton", instance=inst - 1).click()

    @teststep
    def click_move_btn(self, direction='up', duration=1):
        '''
        点击字幕移动方向按钮
        :param direction: 点按钮选择 up、down、left、right
        :param duration: 点击时长,默认1秒
        :return:
        '''
        log.i('点击 %s 按钮 ，时长%s秒' % (direction, duration))
        if direction == 'up':
            self.d(resourceId="com.quvideo.xiaoying:id/top_move").long_click(duration)
        elif direction == 'down':
            self.d(resourceId="com.quvideo.xiaoying:id/bottom_move").long_click(duration)
        elif direction == 'left':
            self.d(resourceId="com.quvideo.xiaoying:id/left_move").long_click(duration)
        elif direction == 'right':
            self.d(resourceId="com.quvideo.xiaoying:id/right_move").long_click(duration)
        else:
            raise Exception('点击方向 str设定错误  direction=%s' % direction)

    @teststep
    def select_subtitle_location(self, inst=5):
        '''设定字幕在预览窗口的位置'''
        if inst == 1:
            log.i('点击top_left按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/top_left").click()
        elif inst == 2:
            log.i('点击top按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/center_top").click()
        elif inst == 3:
            log.i('点击top_right按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/top_right").click()
        elif inst == 4:
            log.i('点击center_left按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/center_left").click()
        elif inst == 5:
            log.i('点击center按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/center").click()
        elif inst == 6:
            log.i('点击center_right按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/center_right").click()
        elif inst == 7:
            log.i('点击bottom_left按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/bottom_left").click()
        elif inst == 8:
            log.i('点击center_bottom按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/center_bottom").click()
        elif inst == 9:
            log.i('点击bottom_right按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/bottom_right").click()
        else:
            raise Exception('点击方位inst 超出范围  inst=%s' % inst)

    @teststep
    def select_nav_effect(self, inst=1):
        log.i('选择已添加的字幕 inst=%s' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/nav_effect_item_layout", instance=inst - 1).click()


class sticker_page(BasePage):
    '''贴纸'''

    @teststep
    def click_sticker_add_btn(self):
        '''贴纸添加 按钮点击'''
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_sticker_op_btn").wait(timeout=3):
            text = self.d(resourceId="com.quvideo.xiaoying:id/tv_sticker_op_btn").get_text()
            log.i('点击按钮 %s' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/tv_sticker_op_btn").click()
            time.sleep(1)
            return text
        else:
            raise Exception('找不到贴纸添加按钮')

    @teststep
    def click_gif_download_btn(self):
        log.i('点击giph下载按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/ib_giphy_download").click()

    @teststeps
    def search_gif(self, text='cat'):
        self.set_fastinput_ime()
        self.d(resourceId="com.quvideo.xiaoying:id/edittext_search").click()
        time.sleep(1)
        self.d.clear_text()
        self.d(resourceId="com.quvideo.xiaoying:id/edittext_search").set_text(text)
        self.d.send_action("search")
        time.sleep(5)  # 等待搜索结果出来

    @teststeps
    def download_use_gif(self, inst=1):
        log.i('下载贴纸搜索页面第%s个贴纸并使用' % inst)
        btn = self.d(resourceId="com.quvideo.xiaoying:id/template_caption_grid_btn_update", instance=inst - 1)
        print(btn.get_text())
        if btn.get_text() == "使用":
            btn.click()
        elif btn.get_text() == "下载":
            btn.click()
            time.sleep(4)
            btn.click()

    @teststep
    def sticker_swipe_left(self):
        log.i('贴纸列表左滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/recycler_view_package")
        self.swipe_left(element=ele, steps=0.2)
        time.sleep(1)

    @teststep
    def sticker_swipe_rigth(self):
        log.i('贴纸列表右边滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/recycler_view_package")
        self.swipe_right(element=ele, steps=0.2)
        time.sleep(1)


class pic_in_pic_page(BasePage):
    '''画中画页面'''

    @teststep
    def click_up_down_btn(self):
        log.i('点击展开收起按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_expand").click()

    @teststep
    def select_tab(self, inst=1):
        if inst == 2:
            log.i('点击GIF tab')
            # self.d(className="android.support.v7.app.ActionBar$b", instance=1).click()
            self.d(description=u"GIF").click()
        else:
            log.i('点击图片 tab')
            # self.d(className="android.support.v7.app.ActionBar$b", instance=0).click()
            self.d(description=u"图片").click()

    @teststep
    def click_other_album(self):
        log.i('点击其他相册')
        self.d(resourceId="com.quvideo.xiaoying:id/collage_pic_item_other_album").click()

    @teststeps
    def select_folder(self, name='AutoTest'):
        '''
        相册文件夹选择
        :param name: folder name textContains exp: '系统' will click folder'系统相册'
        '''
        log.i('自定义背景，其他相册点击文件夹 %s ' % name)
        if self.d(resourceId="com.quvideo.xiaoying:id/rc_folder", scrollable=True).exists:
            self.d(resourceId="com.quvideo.xiaoying:id/rc_folder", scrollable=True).fling.toBeginning()
        ele = self.d(resourceId="com.quvideo.xiaoying:id/rc_folder")
        rect = self.find_element_by_swipe_up(value=self.d(textContains=name), element=ele, steps=0.2).info['bounds']
        time.sleep(0.5)
        x = (rect['right'] + rect['left']) / 2
        y = rect['top'] - self.d.window_size()[0] / 3
        if name == '扫描试试':
            for i in range(4):
                if not self.d(resourceId="com.quvideo.xiaoying:id/btn_edit_photo").wait(timeout=0.5):
                    y = rect['top'] - self.d.window_size()[0] / 3
                    self.d.click(x, y)
                    time.sleep(0.5)
                else:
                    pass
        else:
            for i in range(4):
                if self.d(resourceId="com.quvideo.xiaoying:id/rc_folder").wait(timeout=0.5):
                    self.d.click(x, y)
                    time.sleep(0.5)
                else:
                    pass

    @teststep
    def select_pic(self, inst=1):
        log.i('点击图片board 第%s张图片' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/collage_pic_item_cover", instance=inst - 1).click()

    @teststep
    def select_gif(self, inst=1):
        log.i('点击GIF board 第%s张图片' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/collage_gif_item_cover", instance=inst - 1).click()
        time.sleep(5)  # 等待gif下载\加载完成

    @teststep
    def search_gif(self, text='pig'):
        self.set_fastinput_ime()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_search_gif").click()
        time.sleep(1)
        self.d.clear_text()
        self.d(resourceId="com.quvideo.xiaoying:id/btn_search_gif").set_text(text)
        self.d.send_action("search")
        time.sleep(5)  # 等待搜索结果出来

    @teststep
    def click_operation_btn(self):
        '''添加\完成  按钮点击'''
        if self.d(resourceId="com.quvideo.xiaoying:id/ve_collage_op_btn").wait(timeout=3):
            text = self.d(resourceId="com.quvideo.xiaoying:id/ve_collage_op_btn").get_text()
            log.i('点击按钮 %s' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/ve_collage_op_btn").click()
            time.sleep(1)
            return text
        else:
            raise Exception('找不到画中画操作按钮')


class fx_page(BasePage):
    '''FX 特效页面操作'''

    @teststep
    def select_fx_icon(self, inst=1):
        log.i('点击第列表第 %s字幕/贴纸' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/recycler_category_group_detail").\
            child(className="android.widget.RelativeLayout", instance=inst - 1).click()
        time.sleep(5)

    @teststep
    def click_operation_btn(self):
        '''添加\删除  按钮点击'''
        if self.d(resourceId="com.quvideo.xiaoying:id/ve_music_op_btn").wait(timeout=3):
            text = self.d(resourceId="com.quvideo.xiaoying:id/ve_music_op_btn").get_text()
            log.i('点击按钮 %s' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/ve_music_op_btn").click()
            time.sleep(1)
            return text
        else:
            raise Exception('找不到FX操作按钮')

    @teststep
    def fx_swipe_left(self):
        log.i('贴纸列表左滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/recycler_category_group_detail")
        self.swipe_left(element=ele, steps=0.2)
        time.sleep(1)

    @teststep
    def fx_swipe_rigth(self):
        log.i('贴纸列表右边滑')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/recycler_category_group_detail")
        self.swipe_right(element=ele, steps=0.2)
        time.sleep(1)


class sound_effect_page(BasePage):
    '''音效页面操作'''

    @teststep
    def select_tab(self, inst=1):
        if inst == 2:
            log.i('点击音效 tab')
            # self.d(className="android.support.v7.app.ActionBar$b", instance=1).click()
            self.d(description=u"音效").click()
        else:
            log.i('点击录音 tab')
            # self.d(className="android.support.v7.app.ActionBar$b", instance=0).click()
            self.d(description=u"录音").click()

    @teststep
    def click_record_btn(self, time=None):

        if time:
            log.i('长按录音按钮%s 秒' % time)
            self.d(resourceId="com.quvideo.xiaoying:id/view_editor_audio_record").long_click(duration=time)
        else:
            log.i('点击录音按钮')
            self.d(resourceId="com.quvideo.xiaoying:id/view_editor_audio_record").click()

    @teststep
    def click_operation_btn(self):
        '''添加\删除  按钮点击'''
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_editor_audio_operation").wait(timeout=3):
            text = self.d(resourceId="com.quvideo.xiaoying:id/tv_editor_audio_operation").get_text()
            log.i('点击按钮 %s' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/tv_editor_audio_operation").click()
            time.sleep(2)
            return text
        else:
            raise Exception('找不到音效操作按钮')

    @teststep
    def select_voice_bar(self, inst=80):
        '''设定配音的音量bar inst 不是很精准'''
        log.i('设置配乐的音量为 %s ' % inst)
        if self.d(resourceId="com.quvideo.xiaoying:id/seekbar_editor_effect_audio_volume").wait(timeout=5):
            ele = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_editor_effect_audio_volume").info['bounds']
            y = (ele['bottom'] + ele['top']) / 2
            unit = (ele['right'] - ele['left']) / 100
            x = 2 * unit + ele['left'] + inst * unit
            self.d.click(x, y)
        else:
            raise Exception('没有找到音乐音量bar')


if __name__ == '__main__':
    from Public.Log import Log
    from PageObject import gallery

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)

    # subtitle_page().select_text_color()
    # subtitle_page().select_stroke_alpha()
    # subtitle_page().select_stroke_color()
    # subtitle_page().click_shadow_switch()
    # subtitle_page().select_subtitle_tab(4)
    # subtitle_page().click_move_btn('down')
    # subtitle_page().click_move_btn('left')
    # subtitle_page().click_move_btn('right')
    # subtitle_page().click_move_btn('up')
    # subtitle_page().text_subtitle('hhhhhhhla')
    # for i in range(9):
    #     subtitle_page().select_subtitle_location(i + 1)
    # subtitle_page().select_subtitle_location()
    effect_page().select_top_tab(2)
