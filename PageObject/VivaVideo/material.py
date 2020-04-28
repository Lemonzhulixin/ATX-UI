#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.Decorator import *
from Public.Log import Log
from PageObject.VivaVideo import edit

log = Log()


class material_page(BasePage):
    '''素材中心页面'''

    @teststep
    def is_material_page(self):
        '''判断是否在素材中心页面,查看banner控件是否存在'''
        status = self.d(resourceId="com.quvideo.xiaoying:id/tv",text = '素材中心').wait(timeout=3)
        log.i('判断是否在素材中心页面 status=%s' % status)
        return status

    @teststep
    def material_back(self):
        self.d(resourceId="com.quvideo.xiaoying:id/iv_back").click()

    @teststep
    def click_material_banner(self):
        log.i('点击banner')
        self.d(resourceId="com.quvideo.xiaoying:id/cv").click()

    @teststep
    def swipe_material_banner(self):
        log.i('滑动banner')
        banner = self.d(resourceId="com.quvideo.xiaoying:id/cv")
        self.swipe_left(element=banner,steps=0.05)

    @teststep
    def material_banner_back(self):
        log.i('从banner跳转后的页面返回')
        self.d.press("back")
        if self.d(resourceId="com.quvideo.xiaoying:id/cv").exists:
            print("已经返回到素材中心了")
        else:
            log.i('需要再次back返回素材中心')
            self.d.press("back")

    @teststep
    def select_material_type(self, text=None):
        log.i('点击%s' % text)
        if self.d(resourceId="com.quvideo.xiaoying:id/sub_btn_text", text=text).wait(timeout=1):
            el = self.d(resourceId="com.quvideo.xiaoying:id/sub_btn_text", text=text)
        else:
            el = self.find_element_by_swipe_up(self.d(resourceId="com.quvideo.xiaoying:id/tv_title", text=text))
        el.click()
        time.sleep(1)

    @teststep
    def click_material_cover(self):
        log.i("选择一个素材封面点击")
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/imgCover").click(3)
        except:
            log.i("当前是字体选择页面")
            self.d(className = "android.view.ViewGroup").click()

    @teststep
    def select_material_use(self, text=None):
        log.i('使用%s' % text)
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/btnAdd", text='立即添加').click(3)
            self.d(resourceId="com.quvideo.xiaoying:id/btnToEditor", text='去使用').click()
        except:
            log.i('当前%s已添加，直接去使用' % text)
            self.d(resourceId="com.quvideo.xiaoying:id/btnToEditor", text='去使用').click()

    @teststep
    def use_all_clips(self, all = True):
        log.i('是否应用全部镜头')
        if all:
            log.i('应用全部镜头')
            try:
                self.d(resourceId="com.quvideo.xiaoying:id/tv_all_clip",text = '全部镜头').click(3)
                self.d(resourceId="com.quvideo.xiaoying:id/iv_bar_done").click()
            except:
                log.i('当前是应用转场/背景素材')
                self.d(resourceId="com.quvideo.xiaoying:id/btnRight", text = '全部镜头').click()
                self.d(resourceId="com.quvideo.xiaoying:id/btnDone").click()
        else:
            log.i('不应用全部镜头')
            try:
                self.d(resourceId="com.quvideo.xiaoying:id/iv_bar_done").click(3)
            except:
                self.d(resourceId="com.quvideo.xiaoying:id/btnDone").click()

    @teststep
    def material_theme_change(self, themelist ='热门',theme= '落日飞车',text =True):
        """
       :param themeList: 主题分类
       :param theme: 主题名称
       :param text: 是否带有字幕
       :return:
        """
        log.i('从素材中心切换到%s主题分类' % themelist)
        self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text=themelist).click()

        log.i('点击%s主题' % theme)
        if self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text=theme).wait(timeout=1):
            el = self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text=theme)
        else:
            el = self.find_element_by_swipe_up(self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text=theme))
        el.click()
        time.sleep(0.5)
        self.select_material_use('主题')
        time.sleep(3)
        self.screenshot()
        if text:
            edit.edit_page().stop_video_play()
            self.d(resourceId="com.quvideo.xiaoying:id/item_title", text=theme).click()
            self.screenshot()
        else:
            pass

    @teststep
    def preview_theme_change(self, themelist='日常'):
       self.d(text = themelist).click()
       self.d(resourceId="com.quvideo.xiaoying:id/item_cover").click()
       time.sleep(5)
       self.screenshot()


    @teststep
    def text_change(self, text='动态'):
        log.i('切换到%s分类' % text)
        self.d(resourceId="com.quvideo.xiaoying:id/tvTitle", text=text).click()
        self.select_material_use('字幕')

    @teststep
    def FX_change(self, text='玩法'):
        log.i('切换到%s分类' % text)
        self.d(text=text).click()
        self.d(resourceId = "com.quvideo.xiaoying:id/layout_main").click()
        time.sleep(2)
        self.screenshot()
        self.d(resourceId="com.quvideo.xiaoying:id/iv_choose_finish").click()

    @teststep
    def common_change(self, text='分屏'):
        """适应特效滤镜、调色滤镜、转场、背景"""
        log.i('切换到%s分类' % text)
        self.d(text=text).click()
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/item_cover").click(3)
        except:
            self.d(resourceId = "com.quvideo.xiaoying:id/content_layout").click()

    @teststep
    def sticker_change(self, text='可爱'):
        log.i('切换到%s分类' % text)
        self.d(text=text).click()
        self.d(resourceId="com.quvideo.xiaoying:id/item_layout").click()
        time.sleep(2)
        self.screenshot()
        self.d(resourceId="com.quvideo.xiaoying:id/iv_choose_finish").click()









    # @teststep
    # def get_title(self):
    #     log.i('获取当前页面title')
    #     title = self.d(resourceId="com.quvideo.xiaoying:id/tvTitle").get_text()
    #     return title
    #
    #
    # @teststep
    # def enter_material_page(self):
    #     log.i('进入素材中心')
    #     self.d.app_start(package_name='com.quvideo.xiaoying',
    #                 activity='com.quvideo.xiaoying.templatex.ui.TemplateCenterActivity')

    @teststep
    def click_management_btn(self):
        log.i('点击素材管理按钮')
        if self.d(resourceId="com.quvideo.xiaoying:id/text_right").exists:  # 主题、字幕、动画贴纸、转场
            self.d(resourceId="com.quvideo.xiaoying:id/text_right").click()
        elif self.d(resourceId="com.quvideo.xiaoying:id/right_mgr").exists:  # 滤镜、字体
            self.d(resourceId="com.quvideo.xiaoying:id/right_mgr").click()
        elif self.d(resourceId="com.quvideo.xiaoying:id/btn_manager").exists:  # 改版后的特效页面
            self.d(resourceId="com.quvideo.xiaoying:id/btn_manager").click()
        time.sleep(2)


class theme_fx_transition(BasePage):
    '''素材中心,主题 特效 转场页面'''
    def item_count(self):
        count = self.d(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_title").count
        return count

    def get_item_info(self,inst=1):
        # tag=self.d(resourceId="com.quvideo.xiaoying:id/template_caption_grid_layout_icon",instance=inst - 1).\
        #     child(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_scene").get_text()
        # name = self.d(resourceId="com.quvideo.xiaoying:id/info_list_item_layout_title",instance=inst - 1).\
        #     child(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_title").get_text()
        self.d(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_title").wait(timeout=2)
        name = self.d(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_title",instance=inst - 1).get_text()
        log.i('item name:%s ' % name)
        return name

    def get_item_list(self):
        item_list = [self.get_item_info(i+1) for i in range(self.item_count())]
        log.i('item_list:%s ' % item_list)
        return item_list

    @teststep
    def click_icon(self,inst=1):
        log.i('点击:%s,' % self.get_item_info(inst))
        if self.d(resourceId="com.quvideo.xiaoying:id/template_caption_grid_layout_icon").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/template_caption_grid_layout_icon", instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/item_cover",instance=inst - 1).click()  # 特效页面点击图片
        time.sleep(1)

    @teststeps
    def click_download_btn(self,inst=1):
        log.i('下载:%s ' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/rl_download_status", instance=inst - 1).\
            child(resourceId="com.quvideo.xiaoying:id/imgbtn_download").click()
        time.sleep(5)

    @teststeps
    def click_fx_dwonload_all_btn(self):
        if self.d(resourceId="com.quvideo.xiaoying:id/btn_download").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/btn_download").click()
            log.i('开始下载全部 【%s】 特效'% self.d(resourceId="com.quvideo.xiaoying:id/title").get_text())
            time.sleep(5)
        else:
            raise Exception('没有发现特效【下载全部】按钮')

    @teststeps
    def click_action_btn(self,inst=1):
        log.i('点击使用/删除 :%s ' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/rl_download_status", instance=inst - 1). \
            child(resourceId="com.quvideo.xiaoying:id/template_caption_grid_btn_update").click()
        time.sleep(2)

    @teststeps
    def img_close(self):
        log.i('关闭预览弹窗')
        self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_close").click()

    @teststeps
    def img_use(self):
        log.i('预览弹窗下载并点击使用')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_download").wait()
        btn = self.d(resourceId="com.quvideo.xiaoying:id/btn_download")
        if btn.get_text() == '下载':
            btn.click()
            time.sleep(5)
            btn.click()
        else:
            btn.click()

    @teststeps
    def delete_theme(self,inst=1):
        log.i('删除第%s个主题/特效/转场' % inst)
        self.click_action_btn(inst)
        self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click()
        time.sleep(1)

class subtitle_sticker_giphy(BasePage):
    '''素材中心 字幕页面'''
    def item_count(self):
        count = self.d(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_title").count
        return count

    def get_item_info(self,inst=1):
        text = self.d(resourceId="com.quvideo.xiaoying:id/info_list_item_txt_title",instance=inst - 1).get_text()
        log.i('item name:%s ' % text)
        return text

    def get_item_list(self):
        item_list = [self.get_item_info(i+1) for i in range(self.item_count())]
        log.i('item_list:%s ' % item_list)
        return item_list

    @teststep
    def click_icon(self, inst=1):
        log.i('点击:%s' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/item_layout", instance=inst - 1).click()

    @teststeps
    def click_download_btn(self,inst=1):
        log.i('下载%s'% self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/rl_download_status",instance=inst - 1).\
            child(resourceId="com.quvideo.xiaoying:id/imgbtn_download").click()
        time.sleep(5)

    @teststeps
    def click_use_btn(self,inst=1):
        log.i('点击使用%s' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/rl_download_status", instance=inst - 1).\
            child(dresourceId="com.quvideo.xiaoying:id/info_list_item_btn_update").click()
        time.sleep(2)

    @teststeps
    def delete_subtitle(self,inst=1):
        log.i('删除第%s个字幕/贴纸'% inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_delete",instance=inst - 1).click()
        self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click()
        time.sleep(1)

    @teststeps
    def img_use(self):
        log.i('详情页面下载并点击使用')
        if self.d(resourceId="com.quvideo.xiaoying:id/template_pack_download_btn").wait(timeout=5):
            self.d(resourceId="com.quvideo.xiaoying:id/template_pack_download_btn").click()
            time.sleep(7)
            self.d(resourceId="com.quvideo.xiaoying:id/template_pack_apply_btn").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/template_pack_apply_btn").click()

    @teststeps
    def select_tab(self,inst =1):
        if inst==1:
            log.i('点击tab [动画贴纸]')
            self.d(resourceId="com.quvideo.xiaoying:id/left_button").click()
        elif inst==2:
            log.i('点击tab [GIPHY]')
            self.d(resourceId="com.quvideo.xiaoying:id/right_button").click()
            time.sleep(2)

    ##############GIPHY#################
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
    def clear_search(self):
        log.i('搜索输入框 x 点击')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_clear_edit").click()

    @teststep
    def click_download_gif_btn(self,inst=1):
        log.i('下载giphy搜索页面第%s个gif' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/template_caption_grid_btn_update", instance=inst - 1).click()
        time.sleep(3)

    @teststeps
    def download_use_gif(self, inst=1):
        log.i('下载giphy搜索页面第%s个gif并使用' % inst)
        btn = self.d(resourceId="com.quvideo.xiaoying:id/template_caption_grid_btn_update", instance=inst - 1)
        if btn.get_text() == "使用":
            btn.click()
        elif btn.get_text() == "下载":
            btn.click()
            time.sleep(4)
            btn.click()

    @teststeps
    def delete_gif(self,inst=1):
        log.i('删除第%s个 gif' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/text_delete",instance=inst-1).click()
        self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultPositive").click()
        time.sleep(1)

class fitler(BasePage):
    '''滤镜'''
    def item_count(self):
        count = self.d(resourceId="com.quvideo.xiaoying:id/tv_filter_item_title").count
        return count

    def get_item_info(self,inst=1):
        text = self.d(resourceId="com.quvideo.xiaoying:id/tv_filter_item_title", instance=inst - 1).get_text()
        log.i('item name:%s ' % text)
        return text

    def get_item_list(self):
        item_list = [self.get_item_info(i + 1) for i in range(self.item_count())]
        return item_list

    @teststep
    def click_icon(self, inst=1):
        log.i('点击:%s' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/img_filter_itme_src", instance=inst - 1).click()

    @teststeps
    def click_download_btn(self, inst=1):
        log.i('下载%s' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/template_filter_download", instance=inst - 1).click()
        time.sleep(5)

    @teststeps
    def click_use_btn(self, inst=1):
        log.i('点击使用 %s' % self.get_item_info(inst))
        self.d(resourceId="com.quvideo.xiaoying:id/template_filter_apply", instance=inst - 1).click()
        time.sleep(2)

    @teststeps
    def delete_fitler(self, inst=1):
        log.i('删除第%s个字幕/贴纸' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_delete", instance=inst - 1).click()
        time.sleep(1)


    @teststeps
    def img_use(self):
        log.i('滤镜详情页面下载并点击使用')
        if self.d(resourceId="com.quvideo.xiaoying:id/btn_filter_download").wait(timeout=5):
            self.d(resourceId="com.quvideo.xiaoying:id/btn_filter_download").click()
            time.sleep(5)
            self.d(resourceId="com.quvideo.xiaoying:id/btn_filter_apply").click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/btn_filter_apply").click()


class fonts(BasePage):
    '''字体'''
    @teststeps
    def click_download_btn(self, inst=1):
        log.i('下载第%s个字体'%  inst)
        self.d(resourceId="com.quvideo.xiaoying:id/btn_download", instance=inst - 1).click()
        time.sleep(5)

    def click_use_bun(self,inst=1):
        log.i('点击第 %s个已下载字体使用按钮'% inst)
        self.d(resourceId="com.quvideo.xiaoying:id/btn_apply", instance=inst - 1).click()

    def click_delete_btn(self,inst=1):
        log.i('删除第 %s个已下载字体'% inst)
        self.d(resourceId="com.quvideo.xiaoying:id/img_delete", instance=inst - 1).click()
        time.sleep(1)






if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # material_page().select_material_type("主题")
    material_page().click_material_cover()
    material_page().select_material_use("主题")




