# -- coding: utf-8 --
import os
from redmine.Data.var import *
# 存放报告的位置


def latest_report(report_url):
    # os.listdir()方法用于返回指定文件夹包含文件或文件名字列表
    lists = os.listdir(report_url)
    # 按照时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_url+'\\'+fn))
    file = os.path.join(report_url, lists[-1])
    return file

