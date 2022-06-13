#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2021/7/28 11:43
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: ATX-UI
#  @File: 1.py.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.Decorator import *
from PageObject.VivaVideo import home


class edit_page(BasePage):
    # ————————————————————————
    # 主题、镜头编辑、素材效果公共方法
    # ————————————————————————
    @teststep
    def is_edit_page(self):

        status = self.d(resourceId="com.quvideo.xiaoying:id/editor_draft").wait()
        log.i('是否在编辑页面，status=%s' % status)
        return status

    @teststep
    def is_addText_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text="热门样式").wait()
        log.i('是否在添加字幕页面，status=%s' % status)
        return status

    @teststep
    def is_mixer_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/tv_main_panel_mode_title", text="画中画").wait()
        log.i('是否在添加画中画页面，status=%s' % status)
        return status

    @teststep
    def is_maosaic_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/tv_title", text="马赛克").wait()
        log.i('是否在添加马赛克页面，status=%s' % status)
        return status

    @teststep
    def is_musicExitraction_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/btn_confirm", text="提取").wait()
        log.i('是否在音频提取页面，status=%s' % status)
        return status

    @teststep
    def is_preview_page(self):
        status = self.d(resourceId="com.quvideo.xiaoying:id/editor_publish", text="保存").wait()
        log.i('是否在预览页面，status=%s' % status)
        return status

    @teststep
    def edit_back(self,value):
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/editor_back_btn").click(3)
        except:
            log.i("当前在添加文本&特效页面，需要再次返回")
            self.d(resourceId="com.quvideo.xiaoying:id/ib_second_back").click()
            self.d(resourceId="com.quvideo.xiaoying:id/editor_back_btn").click()

        if value=='保存并退出':
            self.d(resourceId="com.quvideo.xiaoying:id/ll_save_exit").click()
            self.d.wait_activity(activity="com.quvideo.xiaoying.MainActivity",timeout=5)
        elif value == '直接退出':
            self.d(resourceId="com.quvideo.xiaoying:id/ll_just_exit").click()
            self.d.wait_activity(activity="com.quvideo.xiaoying.MainActivity",timeout=5)
        home.home_Page().close_ad_popup()

    @teststep
    def close_pop_dialog(self):
        log.i("关闭新手引导")
        if self.d(resourceId="com.quvideo.xiaoying:id/iv_close").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/iv_close").click()
        else:
            log.i("新手引导已关闭")

    @teststep
    def click_store_icon(self):
        log.i('进入素材商店')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_store").click()

    @teststeps
    def text_input(self, text = "aaaa"):
        log.i('字幕文本输入')
        self.set_fastinput_ime()
        self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text="键盘").click()
        self.d(resourceId="com.quvideo.xiaoying:id/et_edit").clear_text()
        self.d(resourceId="com.quvideo.xiaoying:id/et_edit").set_text(text)

    @teststep
    def edit_finish(self):
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/ivFinish").click(3)
        except:
            self.d(resourceId="com.quvideo.xiaoying:id/btnDone").click()

    @teststep
    def stop_video_play(self):
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/iv_play").click(3)
        except:
            self.d(resourceId="com.quvideo.xiaoying:id/seekbar_play").click()

    @teststep
    def edit_child_tab(self, parent='镜头剪辑', child='修剪'):
        """
        :param par: 主tab，如镜头剪辑
        :param child: 二级页面，如修剪，分割
        :return:
        """
        log.i('点击%s' % parent)
        self.d(text = parent).click()
        log.i('点击%s' % child)
        self.d(resourceId="com.quvideo.xiaoying:id/bottom_text_view", text=child).click(3)
        time.sleep(1)

    @teststep
    def edit_font_enter(self):
        self.edit_child_tab(parent="文字&特效",child="字幕")
        self.text_input(text="修改字体测试")
        self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text="自定义样式").click()

    @teststep
    def edit_font_download(self):
        try:
            self.d(resourceId='com.quvideo.xiaoying:id/iv_font_download_flag').click(3)
            time.sleep(5)
        except:
            log.i('当前页面字体已全部下载')
            pass

    @teststep
    def edit_font_use(self):
        self.d(resourceId="com.quvideo.xiaoying:id/iv_font_item").click()
        time.sleep(5)
        self.d(resourceId="com.quvideo.xiaoying:id/ivFinish").click()


    @teststep
    def select_editor_tab(self, inst=1):
        '''
        切换编辑模块，主题、编辑、效果
        # :param inst:1主题；2编辑；3效果
        :param inst:1主题;2配乐;3镜头编辑;4素材效果
        '''
        # log.i('切换编辑模块，1主题;2配乐;3镜头编辑;4素材效果,select->%s' % inst)
        tab = self.d(resourceId="com.quvideo.xiaoying:id/tab_iv", instance=inst - 1)
        text = tab.get_text()
        log.i('点击tab %s' % text)
        tab.click()

    @teststep
    def click_draft_btn(self):
        log.i('点击存草稿')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_draft").click()
        time.sleep(2)

    @teststep
    def click_publish_btn(self):
        log.i('点击发布按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_publish").click()
        time.sleep(2)

    @teststep
    def click_back_btn(self):
        log.i('点击返回按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/editor_back_btn").click()

    @teststep
    def click_seekbar_play_btn(self):
        log.i('编辑页点击播放按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/seekbar_play").click()

    @teststep
    def get_seekabr_time(self):
        log.i('获取seekbar的播放时长和视频总时长')
        cur = self.d(resourceId="com.quvideo.xiaoying:id/txtview_cur_time").get_text().split(":")
        cur_time = float(cur[0]) * 60 + float(cur[1])
        total = self.d(resourceId="com.quvideo.xiaoying:id/txtview_duration").get_text().split(":")
        total_time = float(total[0]) * 60 + float(total[1])
        log.i('cur_time:%s, total_time:%s' % (cur_time, total_time))
        return cur_time, total_time

    @teststep
    def select_seekbar_position(self, inst=5):
        '''
        点击seekbar的播放位置
        :param inst: inst  [0~10)之间任意数字  exp 0.2、0.4、...1.8、9.8.0
        '''
        log.i('播放进度点击到 %s/10的播放' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_simple_edit").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 10
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def click_add_clip_bt(self):
        log.i('点击添加clip按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/clipedit_add_btn").click()

    @teststep
    def effect_setting(self):
        log.i('设定生效按钮点击')
        time.sleep(1)
        self.d(resourceId="com.quvideo.xiaoying:id/terminator_right").click(timeout=5)
        time.sleep(3)  # 生效后等待3秒

    @teststeps
    def cancel_setting(self):
        log.i('设定取消按钮点击')
        time.sleep(2)
        self.d(resourceId="com.quvideo.xiaoying:id/terminator_left").click(timeout=5)
        time.sleep(2)
        self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click_exists(timeout=2)
        time.sleep(3)

    @teststep
    def preview_swipe_left(self):
        log.i('预览页右滑动')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/preview_layout")
        BasePage().swipe_left(ele)
        time.sleep(1.5)

    @teststep
    def preview_swipe_right(self):
        log.i('预览页左滑动')
        ele = self.d(resourceId="com.quvideo.xiaoying:id/preview_layout")
        BasePage().swipe_right(ele)
        time.sleep(1.5)

    # ————————————————————————
    # 镜头编辑页面方法
    # ————————————————————————
    @teststep
    def click_apply_all_btn(self):
        log.i('点击应用全部镜头')
        self.d(resourceId="com.quvideo.xiaoying:id/apply_all_layout").click()

    @teststep
    def get_clip_time(self, inst=1):
        '''
        获取缩略图内的时间
        :param inst: 存在时间显示的clip缩略图，不包含 focus状态的clip
        :return:
        '''

        str_time = self.d(resourceId="com.quvideo.xiaoying:id/item_duration", instance=inst - 1).get_text().split(
            ":")
        clip_time = float(str_time[0]) * 60 + float(str_time[1])
        log.i('第%s个 clip的时长显示为 %s' % (inst, clip_time))
        return clip_time

    # def is_focused(self,inst=1):
    #     focused = self.d(resourceId="com.quvideo.xiaoying:id/item_comtent", instance=inst-1).\
    #         child(resourceId="com.quvideo.xiaoying:id/item_focus_layout").exists
    #     return focused

    @teststep
    def select_clip_edit_tool(self, text="滤镜"):
        log.i('镜头编辑功能位,点击[%s]' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/clipedit_tool_rcview", scrollable=True).scroll.horiz.to(
            text=text)
        time.sleep(0.5)
        if self.d(text=text).exists:
            self.d(text=text).click()
            time.sleep(1)
            return True
        else:
            log.i("找不到编辑控件-->%s" % text)
            log.i("找不到编辑控件-->%s" % text)
            return False

    @teststeps
    def delete_clip(self, inst=1):
        log.i('删除clipboard 第%s个clip' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/item_delete_btn", instance=inst - 1).click()
        time.sleep(2)
        self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click_exists()
        time.sleep(2)

    @teststep
    def click_transition_btn(self, inst=1):
        log.i('点击clipboard中 第%s个clip后的的转场按钮' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/transition_entrance_btn", instance=inst - 1).click()
        # 点击无效重试一次
        if self.d(resourceId="com.quvideo.xiaoying:id/terminator_left").wait(timeout=2):
            pass
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/transition_entrance_btn", instance=inst - 1).click()
        time.sleep(1)

    @teststep
    def click_clip(self, inst=1):
        log.i('点击clipboard中 第%s个clip' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/item_comtent", instance=inst - 1).click()

    @teststep
    def drag_clip(self, start=1, end=2):
        '''
        拖动clipboard上clip的顺序
        :param start: 被移动clips的顺序
        :param end:  移动到clips的位置顺序
        :return:
        '''
        log.i('拖动clipboard上第%s个clip到第%s个的位置' % (start, end))
        start_clip = self.d(resourceId="com.quvideo.xiaoying:id/item_cover", instance=start - 1)
        # start.click()
        end_clip = self.d(resourceId="com.quvideo.xiaoying:id/item_cover", instance=end - 1).info["bounds"]
        if start > end:
            start_clip.drag_to(end_clip["left"], end_clip["top"])
        else:
            start_clip.drag_to(end_clip["right"], end_clip["bottom"])
        log.i('拖动第%s个clip到第%s个的位置' % (start, end))

    @teststep
    def click_confirm_btn(self):
        log.i('镜头顺序，确认按钮点击')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_confirm").click()
        time.sleep(1)

    @teststep
    def wait_progress_done(self, timeout=60):
        log.i('等待倒放结束')
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_ve_basic_tool_dialog_candel_button").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_ve_basic_tool_dialog_candel_button").wait_gone(
                timeout=timeout)
        else:
            pass
        toast = self.get_toast_message()
        return toast


    # ————————————————————————
    # 主题配乐页面方法
    # ————————————————————————
    @teststep
    def select_theme(self, text="无主题", click_tag=False):
        '''

        :param text: 主题名字
        :param click_tag: 是否点击主题下方的文字跳转到tag
        :return:
        '''

        # self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor", scrollable=True).scroll.horiz.to(text=text)
        self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor", scrollable=True).fling.horiz.toBeginning()
        self.find_element_by_swipe_left(self.d(text=text), self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor"))
        self.swipe_left(self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor"))
        time.sleep(1)
        if self.d(text=text).exists:
            if click_tag:
                log.i('主题配乐，点击主题 %s下方的文字' % text)
                self.d(text=text).click()
                tag = self.d(resourceId="com.quvideo.xiaoying:id/theme_scene_name")
                return tag.get_text()
            else:
                log.i('主题配乐，点击主题 %s使用' % text)
                rect = self.d(text=text).info['bounds']
                print(rect)
                x = (rect['left']+rect['right'])/2
                y = rect['top'] - self.d.window_size()[0] / 8
                self.d.click(x, y)
                time.sleep(10)  # 等待主题下载完成
                return True
        else:
            log.i("找不到主题-->%s" % text)
            return False

    @teststep
    def click_hide_btn(self):
        log.i('点击主题分类页面下方的√按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_2lev_hide").click()

    @teststep
    def click_change_music_btn(self):
        log.i('点击主题下 更换配乐按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/rv_theme_editor", scrollable=True).scroll.horiz. \
            to(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music")
        time.sleep(0.5)
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/tv_theme_change_music").click()
            time.sleep(1)
            return True
        else:
            log.i("找不到修改配乐按钮")
            log.i("找不到修改配乐按钮")
            return False

    @teststep
    def change_photo_time_btn(self):
        log.i('点击调整图片时长按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/tvDurateionSetBtn").click()
        # self.d(text='调整照片显示时长').click()

    @teststep
    def select_phtot_time(self,inst=5.5):
        log.i('设定图片时长')
        if self.d(resourceId="com.quvideo.xiaoying:id/seekbar_theme_duration").wait(timeout=5):
            ele = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_theme_duration").info['bounds']
            y = (ele['bottom'] + ele['top']) / 2
            unit = (ele['right'] - ele['left']) / 100
            x = ele['left'] + inst * unit*10
            self.d.click(x, y)
            time.sleep(1)
            set_time = self.d(resourceId="com.quvideo.xiaoying:id/tvThemeDurationTime").get_text()
            log.i('设定时长为%s秒' % set_time)
            return float(set_time.strip('秒'))
        else:
            raise Exception('没有找到图片时长设定bar')


class fitler_page(BasePage):
    '''滤镜操作页面'''

    @teststep
    def select_filter(self, text="原图"):
        log.i('选择滤镜卷 %s 并点击' % text)

        self.d(resourceId="com.quvideo.xiaoying:id/rc_editor_filter", scrollable=True).scroll.horiz.to(
            resourceId="com.quvideo.xiaoying:id/item_fitler_parent_name", text=text)
        time.sleep(0.5)
        if self.d(text=text).exists:
            self.d(text=text).click()
            time.sleep(3)  # 等待下载完成
            return True
        else:
            log.i("找不到滤镜卷-->%s" % text)
            log.i("找不到滤镜卷-->%s" % text)
            return False

    @teststeps
    def click_filter_btn(self, text):
        log.i('点击选择滤镜 %s ' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/rc_editor_filter", scrollable=True).scroll.horiz.to(
            resourceId="com.quvideo.xiaoying:id/item_fitler_child_name", text=text)
        time.sleep(0.5)
        if self.d(text=text).exists:
            self.d(text=text).click()
            return True
        else:
            log.i("找不到滤镜卷-->%s" % text)
            log.i("找不到滤镜卷-->%s" % text)
            return False

    @teststeps
    def select_filter_alpha(self, inst=50):
        '''
        设置滤镜程度 除了（0~10） 之间的的任意数字,5左右的数字存在一定的偏差
        :param inst: inst  0—~100之间任意间隔0.2的数字  exp 10、21、46、...67、98
        '''
        log.i('设置滤镜程度为 %s' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/indicatorSeekBar").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left'] + inst * unit
        self.d.long_click(x, y)


class scale_page(BasePage):
    '''比例和背景操作页面'''

    @teststep
    def click_backgrand_tab(self, inst=1):
        if inst == 1:
            log.i('点击比例调节tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_blur").click()
            # self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_main").click()  # 新方案
        elif inst == 2:
            log.i('点击背景颜色tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_color").click()
            # self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_blurcolor").click()  # 新方案
        elif inst == 3:
            log.i('点击自定义背景tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_background").click()
            # self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_background").click()  # 新方案
        else:
            log.i('点击比例调节tab')
            self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_blur").click()
            # self.d(resourceId="com.quvideo.xiaoying:id/rl_tab_main").click()

    @teststep
    def click_fit_btn(self):
        log.i('点击缩放按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_btn_fit").click()

    @teststep
    def click_play_btn(self):
        log.i('点击播放按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/ib_play").click()

    @teststeps
    def select_scale(self, text="1:1"):
        '''
        选择画面比例
        :param text: 比例对应的文字 例如 4:3  注意冒号
        '''
        log.i('选择画面比例,点击%s' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/hs_clip_ratios", scrollable=True).scroll.horiz.to(text=text)
        time.sleep(0.5)
        self.d(resourceId="com.quvideo.xiaoying:id/ratio_title", text=text).click()

    @teststep
    def pinch_view(self, mode="in"):
        log.i('缩放预览窗口 pinch %s 操作' % mode)
        self.d(resourceId="com.quvideo.xiaoying:id/video_editor_preview").wait()
        if mode == "in":
            self.d(resourceId="com.quvideo.xiaoying:id/video_editor_preview").pinch_in(percent=13, steps=10)
        elif mode == "out":
            self.d(resourceId="com.quvideo.xiaoying:id/video_editor_preview").pinch_out(percent=66, steps=10)

    @teststep
    def select_blur_alpha(self, inst=50):
        '''
        设置背景模糊程度
        :param inst: [0:99) 任意数字
        :return:
        '''
        log.i('设置背景模糊程度为%s' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_blur").info['bounds']
        y = (bar['bottom'] + bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 100
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def select_colour(self, inst=14):
        '''
        设置背景颜色
        :param inst:[1:28]任意整数
        :return:
        '''
        log.i('设置背景颜色 inst=%s' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/multicolor_bar").info['bounds']
        y = (bar['bottom'] + bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 28
        x = bar['left'] + inst * unit - 4
        self.d.long_click(x, y)

    @teststep
    def select_backpic_blur_alpha(self, inst=50):
        '''
        设置背景模糊程度
        :param inst: [0:99) 任意数字
        :return:
        '''
        log.i('设置背景模糊程度 为 %s ' % inst)
        bar = self.d(resourceId="com.quvideo.xiaoying:id/pic_seekbar_blur").info['bounds']
        y = (bar['bottom'] + bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 100
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def select_backpic(self, inst=1):
        log.i('自定义背景 选择第%s张照片，并点击' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/btn_expand").click()  # 点击向上箭头按钮
        self.d(resourceId="com.quvideo.xiaoying:id/collage_pic_item_cover", instance=inst - 1).click()

    @teststep
    def click_none_pic_btn(self):
        log.i('自定义背景，点击设定为默认背景')
        self.d(resourceId="com.quvideo.xiaoying:id/pic_item_none").click()

    @teststep
    def click_other_pic_btn(self):
        log.i('自定义背景 ，点击其他相册')
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
    def select_photo_clip(self, inst=1, preview=False):
        '''
        选择图片
        :param inst: inst=n 点击第n个clips
        :param preview: if True click gallery_preview_button
        :return:
        '''
        log.i('自定义背景，其他相册 点击第%s张 图片，preview=%s' % (inst, preview))
        if not preview:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/img_click_mask", instance=inst - 1).sibling(
                className="android.widget.RelativeLayout").click()


class trim_cut_page(BasePage):
    '''修剪操作页面'''

    def click_trim_btn(self):
        log.i('点击修剪按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/trim_button").click()

    def click_cut_btn(self):
        log.i('点击剪中间按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/cut_button").click()

    def get_trim_time(self):
        log.i('获取trim时长')
        trim_time = self.d(resourceId="com.quvideo.xiaoying:id/ve_split_right_time").get_text()
        log.i(trim_time)
        return trim_time

    def trim_swipe(self):
        log.i('左右滑动trim及微调trim，只有初次进入才能操作成功（trimbar无法定位）')
        log.i('original clip time is：%s 秒' % self.get_trim_time())
        trim = self.d(resourceId="com.quvideo.xiaoying:id/ve_gallery").info['bounds']
        unit = int(trim["right"] - trim["left"]) / 7
        y = int(trim["top"] + (trim["bottom"] - trim["top"]) / 2)
        self.d.swipe(int(trim["left"]) + unit / 4, y, int(trim["left"]) + 3 * unit, y, duration=0.1)
        log.i('after left_trim swipe clip time is：%s 秒' % self.get_trim_time())
        edit_page().preview_swipe_left()
        log.i(self.get_trim_time())
        self.d.swipe(int(trim["right"]) - unit / 4, y, int(trim["right"]) - 3 * unit, y, duration=0.1)
        log.i('after right_trim swipe time is：%s 秒' % self.get_trim_time())
        edit_page().preview_swipe_right()
        log.i(self.get_trim_time())


class split_page(BasePage):
    '''分割操作页面'''

    @teststeps
    def split_select(self, inst=30):
        '''
        设定分割的百分比位置
        :param inst:[0:100]
        :return: 截取点的时间 单位/s
        '''
        log.i('设定分割的百分比位置 %s' % inst)
        ele = self.d(resourceId="com.quvideo.xiaoying:id/ve_gallery").info['bounds']
        y = (ele['bottom'] + ele['top']) / 2
        unit = (ele['right'] - ele['left']) / 16
        x = unit + ele['left'] + inst * unit * 14 / 100
        self.d.click(x, y)
        time.sleep(2)
        total_time = split_page().get_total_time()
        split_time = total_time * inst / 100
        log.i('分割时长为：%s' % split_time)
        return split_time

    @teststep
    def get_total_time(self):
        log.i('获取clip时长')
        total = self.d(resourceId="com.quvideo.xiaoying:id/ve_split_right_time").get_text().split(":")
        trim_time = float(total[0]) * 60 + float(total[1])
        log.i(trim_time)
        time.sleep(0.5)
        return trim_time


class speed_page(BasePage):
    '''变速操作页面'''

    def speed_select(self, inst=5):
        '''
        设置镜头变速
        :param inst:[0:10]
        :return: 截取点的时间 单位/s
        '''
        ele = self.d(resourceId="com.quvideo.xiaoying:id/txtseekbar_clip_speed").info['bounds']
        y = (ele['bottom'] + ele['top']) / 2
        unit = (ele['right'] - ele['left']) / 25
        x = 2 * unit + ele['left'] + inst * unit * 22 / 10
        self.d.click(x, y)
        time.sleep(0.5)
        text = self.d(resourceId="com.quvideo.xiaoying:id/tv_speed_value").get_text()
        log.i('设定镜头变速为 %s' % text)

    def click_keep_tone_btn(self):
        log.i('点击保持影调不变按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/keep_tone_layout").click()


class transition_page(BasePage):
    '''转场选择页面'''

    @teststep
    def select_transition(self, text="推出"):
        log.i('选择转场 %s 并点击' % text)

        self.d(resourceId="com.quvideo.xiaoying:id/gallery_common_content_filter",
               scrollable=True).scroll.horiz.to(
            resourceId="com.quvideo.xiaoying:id/item_name", text=text)
        time.sleep(0.5)
        x = self.d(resourceId="com.quvideo.xiaoying:id/item_name", text=text).center()[0]
        y = self.d(resourceId="com.quvideo.xiaoying:id/item_name", text=text).center()[1] - self.d.window_size()[0] / 9
        self.d.click(x, y)
        time.sleep(3)  # 等待下载完成


class magic_sound_page(BasePage):
    '''变声操作页面'''
    @teststeps
    def select_mode(self,text='原声'):
        log.i('点击音效模式 %s'% text)
        self.d(resourceId="com.quvideo.xiaoying:id/rv_magic_sound", scrollable=True).scroll.horiz.to(
            resourceId="com.quvideo.xiaoying:id/tv_title", text=text)
        if self.d(resourceId="com.quvideo.xiaoying:id/tv_title", text=text).exists:
            self.d(resourceId="com.quvideo.xiaoying:id/tv_title", text=text).\
                up(resourceId="com.quvideo.xiaoying:id/fl_icon").click()
        else:
            raise Exception('%s 模式 没有找到')

    @teststep
    def select_sound_alpha(self, inst=70):
        log.i(' 调节音高程度为 %s' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/sb_volume").wait()
        bar = self.d(resourceId="com.quvideo.xiaoying:id/sb_volume").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 120
        x = 10 * unit + bar['left'] + inst * unit
        self.d.click(x, y)

class mosaic_page(BasePage):
    '''马赛克页面操作'''
    @teststep
    def click_gaussian_mode(self):
        log.i('点击高斯模糊')
        self.d(resourceId="com.quvideo.xiaoying:id/gaussian_blur_layout").click()

    @teststep
    def click_pixel_mode(self):
        log.i('点击像素化')
        self.d(resourceId="com.quvideo.xiaoying:id/pixel_layout").click()

    @teststep
    def select_mosaic_alpha(self, inst=70):
        log.i(' 调节音高程度为 %s' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/mosaic_degree").wait()
        bar = self.d(resourceId="com.quvideo.xiaoying:id/mosaic_degree").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 110
        x = 5 * unit + bar['left'] + inst * unit
        self.d.click(x, y)

if __name__ == '__main__':
    from Public.Log import Log
    from PageObject import gallery

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # edit_page().select_editor_tab(1)
    # scale_page().click_backgrand_tab(1)
    # scale_page().select_blur_alpha()
    # edit_page().select_theme('复古频道')
    # print(edit_page().get_seekabr_time()[1])
    # magic_sound_page().select_mode('自定义')
    # magic_sound_page().select_sound_alpha(80)
    # edit_page().effect_setting()
    # edit_page().effect_setting()
    mosaic_page().select_mosaic_alpha()
