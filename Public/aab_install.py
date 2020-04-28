

import platform
import os
import base64
import sys
import whichcraft


# current_path = os.path.dirname(os.path.abspath(__file__))
current_path = os.path.dirname(sys.executable)

bundle_tool_path = os.path.join(current_path, 'static', 'bundletool-all.jar')
vc_ks_path = os.path.join(current_path, 'static', 'c2hlbmcuaGFuMTEwOjp2aXZhY3V0OjpzaGVuZy5oYW4xMTAK')
xy_ks_path = os.path.join(current_path, 'static', 'c2hlbmcuaGFuOjp4aWFveWluZzo6c2hlbmcuaGFuCg==')
tmp_apks_path = os.path.join(current_path, 'tmp.apks')
solidexplorer_apk_path = os.path.join(current_path,'static','SolidExplorerFileManager.apk')


def get_ks_info(ks_path):
    '''
    获取ks信息
    :param ks: ks file name
    :return: [ks_pass, key_alias, key_pass]
    '''
    ks2str = str(base64.b64decode(os.path.basename(ks_path)).decode('utf-8')).strip()
    return ks2str.split('::')


def get_java_path():
    if whichcraft.which('java'):
       jpath= whichcraft.which('java')
    elif platform.system() == "Darwin":
         jpath= os.path.join(current_path, 'static/JRE/jre1.8.0_251.jre/Contents/Home/bin/java')
    elif platform.system() == 'Windows':
          jpath= os.path.join(current_path, 'static\JRE\jre1.8.0_251\\bin\java')
    print('Java Path: %s' % jpath)
    return jpath


def build_apks_code(serial_number, bundle_apth, ks_path):
    ks_info = get_ks_info(ks_path)
    code = '%s -jar %s build-apks --connected-device --device-id=%s --bundle=%s --output=%s --overwrite --ks=%s --ks-pass=pass:%s --ks-key-alias=%s --key-pass=pass:%s' % \
           (get_java_path(), bundle_tool_path, serial_number, bundle_apth, tmp_apks_path, ks_path, ks_info[0],
            ks_info[1], ks_info[2])
    return code.split(' ')


def install_apks_code(serial_number, apks_path):
    code = '%s -jar %s install-apks --device-id=%s --apks=%s' % (
    get_java_path(), bundle_tool_path, serial_number, apks_path)
    return code.split(' ')


def get_apks_size_code(apks_path):
    code = '%s -jar %s get-size total --apks=%s' % (get_java_path(), bundle_tool_path, apks_path)
    return code.split(' ')

#
if __name__ == '__main__':
    ks1 = get_ks_info(xy_ks_path)
    ks2 = get_ks_info(vc_ks_path)
    print(ks1)
    print(ks2)