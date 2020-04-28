#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py

import os
import re
import time
import zipfile
from jinja2 import Environment, FileSystemLoader
import requests

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, )),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html(path_list, title):
    '''以Pubilc/index.html 生成 自动化测试报告.html'''
    name = "./TestReport/Statistics_report.html"
    urls = path_list
    context = {
        'urls': urls,
        'title': title
    }
    with open(name, 'w', encoding="utf-8") as f:
        html = render_template('index.html', context)
        f.write(html)
        f.close()

def _get_report_info(run):
    '''获取每个设备报告的参数'''
    report = run.test_report_path + '/TestReport.html'
    result = {}
    with open(report, 'r', encoding='utf-8') as f:
        res_str = re.findall("测试结果(.+%)", f.read())
        if res_str:
            res = re.findall(r"\d+", res_str[0])
            result["sum"] = res[0]
            result["pass"] = res[1]
            result['fail'] = res[2]
            result['error'] = res[3]
            result['passrate'] = re.findall('通过率 = (.+%)', res_str[0])[0]
        else:
            raise Exception("The TestReport.html in %s has no string'测试结果',please check out!!!" % run.get_path())
        f.close()
    with open(report, 'r', encoding='utf-8') as f:
        result['duration'] = re.findall("合计耗时 : </strong> (.+)</p>", f.read())[0].split('.')[0]
        f.close()
    return result



def create_statistics_report(runs,title=None):
    '''根据运行设备的数量生成统计报告，路径为
    ./TestReport/自动化测试报告.html'''
    report_path_list = []
    for run in runs:
        tmp_dic = {}
        # tmp_dic['path'] = re.findall("./TestReport/(.+$)", run.get_path())[0] + "/TestReport.html"
        tmp_dic['path'] = os.path.split(run.get_path())[1] + "/TestReport.html"
        tmp_dic['name'] = run.get_device()['model'].replace(':', '_').replace(' ', '')+'_'+run.get_device()['serial']
        tmp_dic.update(_get_report_info(run))
        report_path_list.append(tmp_dic)
    create_index_html(report_path_list,title=title)
    print('Generate statistics report completed........ ')
    return report_path_list


def backup_report(time):
    '''备份旧报告 TestReport文件夹'''
    if not os.path.exists("./TestReport_History"):
        os.mkdir("./TestReport_History")
    if not os.path.exists("./TestReport"):
        pass
    else:
        try:
            os.rename('./TestReport', './TestReport_History/Report_' + time)
        except PermissionError as e:
            raise e
        print('Backup TestReport dir success')
    # return './TestReport_History/Report_' + time



def zip_report(time):
    '''压缩TestReport文件夹'''
    if not os.path.exists("./TestReport_ZIP"):
        os.mkdir("./TestReport_ZIP")
    name = 'Android_' + time
    startdir = "./TestReport"  # 要压缩的文件夹路径
    file_news = './TestReport_ZIP/' + name + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            # z.write(os.path.join(dirpath, filename))
    z.close()
    print('Generate zip_report file %s completed........ ' % file_news)
    return file_news

def upload_report_zip(zip_file):
    '''上传压缩文件'''
    url = 'http://10.0.32.194:5100/api/v1/report'
    files = {'file': open(zip_file, 'rb')}
    response = requests.post(url, files=files)
    print(response)
    if response.status_code == 200:
        print('Upload zip_report file success to %s ' % response.json())
    else:
        print('Upload zip_report file Fail ')
        pass



