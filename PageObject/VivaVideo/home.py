#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.Decorator import *
from Public.Test_data import *

log = Log()

class home_Page(BasePage):
    '''创作页首页'''
    # @teststep
    # def wait_page(self):
    #     try:
    #         if self.d(resourceId="com.quvideo.xiaoying:id/iv_vip_home8_cut").wait(timeout=10):
    #             pass
    #         else:
    #             raise Exception('Not in Creation_Page')
    #     except Exception:
    #         raise Exception('Not in Creation_Page')

    # @teststep
    # def close_float_imag(self):
    #     if self.d(resourceId="com.quvideo.xiaoying:id/float_imageview").wait(timeout=5):
    #         log.i('关闭创作页浮窗图片')
    #         self.d(resourceId="com.quvideo.xiaoying:id/float_imageview").child(className="android.widget.ImageView",
    #                                                                        instance=1).click_exists(timeout=3)
    #     else:
    #         log.i('没有创作页浮窗图片,跳过')
    #         pass


    @teststep
    def close_popup(self):
        log.i('关闭首页家庭政策弹窗')
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/iv_close").click(3)
        except:
            log.i('弹窗未弹出或者已消除')
            pass

    @teststep
    def close_ad_popup(self,timeout = 3):
        log.i('关闭广告弹窗 ')
        self.d(resourceId="com.quvideo.xiaoying:id/tt_insert_dislike_icon_img").click_exists(timeout=timeout)

    @teststep
    def click_template_btn(self):
        log.i('点击底部拍同款按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/tv_home_tab", text="拍同款").click()

    @teststep
    def click_home_btn(self):
        log.i('点击底部剪辑按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/tv_home_tab", text="剪辑").click()

    @teststep
    def click_me_btn(self):
        log.i('点击底部我按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/tv_home_tab", text="我").click()

    @teststep
    def click_vip_btn(self):
        log.i('点击VIP按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_vip_home8_cut").click()

    @teststep
    def click_edit_btn(self):
        log.i('点击视频剪辑')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_edit_home8_cut").click()
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/imgbtn_help_exit").implicitly_wait(3).click()
        except:
            log.i("立刻升级页面已消除")
            pass

    @teststep
    def click_mv_btn(self):
        log.i('点击相册MV')
        self.d(resourceId="com.quvideo.xiaoying:id/iv_mv_home8_cut").click()

    @teststep
    def click_draft_btn(self):
        log.i('点击草稿')
        self.d(resourceId="com.quvideo.xiaoying:id/tv_draft_icon_home8_cut",text= '草稿').click()


    @teststep
    def click_home_more(self):
        log.i('点击素材中心查看更多按钮')
        self.d(text="查看更多").click()

    @teststep
    def click_camera_btn(self):
        log.i('点击拍摄按钮')
        self.watch_device('取消|允许|始终允许')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight4_home8_cut").click()
        time.sleep(5)  # 等待相机加载完成
        self.d.click(0.5, 0.5)  # 点击对焦,取消弹出的滤镜


    @teststep
    def click_sec_addText(self):
        log.i('点击次要功能位加字幕')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight0_home8_cut").click()

    @teststep
    def click_sec_Mixer(self):
        log.i('点击次要功能位画中画')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight1_home8_cut").click()

    @teststep
    def click_sec_Mosaic(self):
        log.i('点击次要功能位马赛克')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight2_home8_cut").click()\

    @teststep
    def click_sec_FAQ(self):
        log.i('点击次要功能位新手教程')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight3_home8_cut").click()

    @teststep
    def click_sec_Capture(self):
        log.i('点击次要功能位拍摄')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight4_home8_cut").click()

    @teststep
    def click_sec_musicExtraction(self):
        log.i('点击次要功能位音频提取')
        self.d(resourceId="com.quvideo.xiaoying:id/ll_eight5_home8_cut").click()


    # @teststep
    # def click_view_pager_btn(self, text):
    #     '''
    #     次要功能位置，各个按钮的点击操作
    #     :param text: 次要功能位置的text名称
    #     :return:
    #     '''
    #     log.i('查找次要功能位 %s 并进行点击操作'% text)
    #     if self.d(text=text).wait(timeout=1):
    #         self.d(text=text).click()
    #         return True
    #     else:
    #         try:
    #             self.d(resourceId="com.quvideo.xiaoying:id/view_pager", scrollable=True).scroll.horiz.to(text=text)
    #             self.d(text=text).click()
    #             return True
    #         except UiObjectNotFoundError:
    #             log.i("找不到控件-->%s" % text)
    #             return False

    # @teststep
    # def select_studio_view(self, inst=1):
    #     '''
    #     点击我的工作室的view 默认第一个
    #     :param inst: 0为第一个view 以此类推 1、2、3--> 一二三
    #     '''
    #     log.i('点击我的工作室第%s个草稿' % inst)
    #     self.d(resourceId="com.quvideo.xiaoying:id/layout_draft_item").child(className='android.widget.ImageView')[inst-1].click()


if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    home_Page().close_ad_popup()


