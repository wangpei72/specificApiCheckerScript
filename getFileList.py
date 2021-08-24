#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re


def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    reg = re.compile(r"\..*")
    regForJava = re.compile(r"\.java")
    regForGradle = re.compile(r"\.gradle|\.sh|\.pro|\.xml|\.bat|\.jar|\.MD|\.md|\.png|\.txt|\.json|\.flat|\.class")
    curDiry = os.path.dirname(os.path.realpath(__file__))
    for fi in files:
        if reg.match(fi) is not None or regForGradle.search(fi) is not None:
            continue
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            if regForJava.search(fi_d) is None:
                continue
            print(os.path.join(filepath, fi_d))
            data = os.path.join(filepath, fi_d) + "\n"
            fw = open(os.path.join(curDiry, "fileList.txt"), 'a+')
            fw.write(data)
            fw.close()


def trunc_all_context(filePath):
    fw = open(filePath, 'a+')
    fw.truncate(0)
    fw.close()


# 递归遍历目录下所有文件
curDir = os.path.dirname(os.path.realpath(__file__))
fileDir = os.path.join(curDir, "fileList.txt")
trunc_all_context(fileDir)
gci('/Users/wangpei/workspace/AliSourcingProject')

