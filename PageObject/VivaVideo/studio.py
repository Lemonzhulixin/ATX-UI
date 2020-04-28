#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.Decorator import *
from Public.Log import Log
from PageObject.VivaVideo import home, gallery, publish
log = Log()


class studio_page(BasePage):
    '''工作室页面'''

    @teststeps
    def create_draft(self):
        log.i('创建一个草稿工程')
        home.home_Page().click_edit_btn()
        gallery.gallery_page.gallery_clip_add(2)
        publish.publish_page().click_draft_btn()

    @teststep
    def select_draft(self):
        log.i('打开一个草稿工程')
        try:
            self.d(resourceId="com.quvideo.xiaoying:id/rl_studio_draft_item").click(3)
        except:
            log.i('当前没有草稿工程，新建一个草稿')
            home.home_Page().click_home_btn()
            self.create_draft()
            self.d(resourceId="com.quvideo.xiaoying:id/rl_studio_draft_item").click()




    @teststep
    def click_back_btn(self):
        log.i('工作室点击返回按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_left").click()

    @teststep
    def cancel_share(self):
        '''导出分享dialog取消操作'''
        if self.d(resourceId="com.quvideo.xiaoying:id/share_title").wait(timeout=1):
            self.back()
        else:
            pass

    @teststep
    def select_view(self,status=0):
        '''
        切换工作室的显示模式  status=0:列表模式  其他:grid模式
        :param status:
        :return:
        '''

        if status==0:
            log.i('工作室显示切换 list模式')
            while self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_bottom").wait(timeout=1):
                self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_right").click()
            else:
                pass
        else:
            log.i('工作室显示切换 grid模式')
            while self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_bottom").wait_gone(timeout=1):
                self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_com_btn_right").click()
            else:
                pass

    @teststep
    def get_stuido_time(self,inst=1):
        log.i('获取第%s个草稿时长'% inst)
        time = self.d(resourceId="com.quvideo.xiaoying:id/studio_item_time_duration",instance=inst -1).get_text()
        log.i(time)
        return time

    @teststep
    def click_publish_btn(self, inst=1):
        log.i('点击第%s个草稿发布按钮' % inst)
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_bottom").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_publish_btn",
                   instance=inst - 1).click()
        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_publish_btn_intel",
                   instance=inst - 1).click()

    @teststep
    def delete_studio(self, inst=1):
        log.i('删除第%s个草稿' % inst)
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_bottom").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_img_more",
                   instance=inst - 1).click()

        else:
            self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_img_delete",
                   instance=inst - 1).click()
        time.sleep(1)
        self.d(resourceId="com.quvideo.xiaoying:id/md_buttonDefaultNegative").click()

    @teststep
    def click_studio_img(self, inst=1):
        log.i('点击第%s个草稿' % inst)
        self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb",
               instance=inst - 1).click()
        time.sleep(2)

    @teststep
    def get_exported_status(self,inst=1):
        if self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_bottom").exists:
            status = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_top",instance=inst - 1).\
                child(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_textview_exported").exists
        else:
            status =self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_layout_right",instance=inst - 1).\
                child(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_textview_exported").exists

        return status


if __name__ == '__main__':
    from Public.Log import Log
    from PageObject import gallery

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)

    log.i(studio_page().get_exported_status(4))