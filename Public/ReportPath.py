#  -*- coding: utf-8 -*-
#  /usr/local/bin/python
#  @Time: 2020/4/16 5:29 PM
#  @Author: lemon_zhulixin
#  @Email: zhulixin@live.com
#  @Project: UI
#  @File: __init__.py.py


class ReportPath:
    @classmethod
    def set_path(cls, ps):
        cls.path = ps

    def get_path(self):
        return self.path
