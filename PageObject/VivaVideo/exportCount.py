#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/5/6 2:40 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: ATX-UI
#  @File: exportCount.py

from Public.Decorator import *
from PageObject.VivaVideo import edit, home, publish
from Public.Log import Log
log = Log()
import xlwt

class im_ex_count(BasePage):

    @teststep
    def importTime(self, number):
        self.d.app_start("com.quvideo.xiaoying")
        home.home_Page().click_edit_btn()
        time.sleep(0.5)
        log.i('开始添加镜头')
        for i in range(number):
            el = self.d(resourceId='com.quvideo.xiaoying:id/iv_cover')
            el[i].click()
        log.i('点击下一步进入编辑页')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_next", text='下一步').click()
        import_start = time.time()
        if edit.edit_page().is_preview_page():
            import_end = time.time()
            time_im = str(round(import_end - import_start, 2))
        else:
            raise Exception('导入失败')
        return time_im

    @teststep
    def exportTime(self, inst = 2,timeout=600):
        publish.publish_page().click_export_btn()
        publish.publish_page().select_export(inst=inst)
        export_start = time.time()
        self.d(resourceId="com.quvideo.xiaoying:id/tvProgress").wait(timeout=2)
        if self.d(resourceId="com.quvideo.xiaoying:id/tvProgress").wait_gone(timeout=timeout):
            export_end = time.time()
            time_ex = str(round(export_end - export_start, 2))
        else:
            raise Exception('导出等待超时,导出时长超过%s秒' % timeout)
        self.d.app_stop("com.quvideo.xiaoying")
        return time_ex


    def getDevice(self):
        rt = os.popen('adb devices').readlines()
        n = len(rt)-2
        dev= []
        for i in range(n):
            nPos = rt[i + 1].index("\t")
            dev = rt[i + 1][:nPos]
        return dev

    def clearData(self):
        dev = self.getDevice()
        cmd_clear = 'adb -s ' + dev + ' shell rm -r /sdcard/DCIM/XiaoYing'
        os.popen(cmd_clear)

    def export_test(self, clips = 2, inst = 2, pix = '720P', times = 1):
        """
        :param clips: 添加的镜头个数
        :param inst: 1, 2, 3, 4, 其他，1对应480P
        :param pix: 480, 720, 1080, GIF, 4k
        :param times: 导出次数
        :return:
        """
        # 获取设备信息
        dev = im_ex_count().getDevice()
        t1_list = []
        t2_list = []
        #导出次数
        for i in range(times):
            t1 = im_ex_count().importTime(clips)
            # 导出尺寸: 1-480 2-720 3-1080  4-GIF 其他 4k
            t2 = im_ex_count().exportTime(inst=inst, timeout=600)
            t1_list.append(t1)
            t2_list.append(t2)
            # 清除导出视频
            im_ex_count().clearData()
        print(t1_list, t2_list)

        wb = xlwt.Workbook()  # 创建excel文件
        ws = wb.add_sheet(dev)  # 创建sheet

        # 表格列值
        ws.write(0, 0, "设备")
        ws.write(0, 1, "导入时长")
        ws.write(0, 2, "导出尺寸")
        ws.write(0, 3, "导出时长")

        for i in range(len(t1_list)):
            ws.write(i + 1, 0, dev)
            ws.write(i + 1, 1, t1_list[i])
            ws.write(i + 1, 2, pix)
            ws.write(i + 1, 3, t2_list[i])

        # 保存Excel文件
        # report_time = time.strftime("%H%M%S", time.localtime())
        wb.save('Result_' + pix + '.xls')


if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    im_ex_count().export_test(clips=2, inst=1, pix='480P', times=2)
    im_ex_count().export_test(clips=2, inst=2, pix='720P', times=2)
    # im_ex_count().export_test(clips=2, inst=3, pix='1080P', times=2)
    # im_ex_count().export_test(clips=2, inst=0, pix='4K', times=2)
