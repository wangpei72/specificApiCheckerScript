#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

fileDir = "/Users/wangpei/workspace/AliSourcingProject/AliSourcingBuyerPoseidons/src-hook/com/alibaba/intl/android/apps" \
          "/poseidon/utils/EnvironmentInspector.java"


def spilt_by_path(str_):
    regForJava = re.compile(r"\.java")
    list = re.split(r'/', str_)
    # print(list)
    return list


def get_index_workspace(str_list):
    regForWs = re.compile(r"workspace");
    for i in range(len(str_list)):
        if regForWs.match(str_list[i]):
            return i
    return -1


def get_index_src(str_list):
    regForSrc = re.compile(r"src?-\W*")
    for i in range(len(str_list)):
        if regForSrc.match(str_list[i]):
            # print("src_idx: ", i)
            return i
    return -1


def get_index_java(str_list):
    regForJava = re.compile(r"\.java")
    for i in range(len(str_list)):
        if regForJava.search(str_list[i]):
            # print("java_idx: ", i)
            return i
    return -1


def get_git_repo_name(str_list, ws_idx=2):
    return str_list[ws_idx+1: ws_idx+2]


def get_java_file_name(str_list, java_idx):
    return re.split(r"\.", str_list[java_idx])[0]


def get_package_name(str_list, src_idx, java_idx):
    res = ""
    for item in str_list[src_idx + 1: java_idx]:
        res += item
        res += "."
    return res[0:-1]


def get_java_file_name_print(path, print_button=False):
    mlist = spilt_by_path(path)
    java_idx = get_index_java(mlist)
    file_name = get_java_file_name(mlist, java_idx)
    if print_button:
        # print("path %s \n" % path)
        print("file name : %s.java" % file_name)
    return file_name


def get_package_name_print(path, button=False):
    mlist = spilt_by_path(path)
    java_idx = get_index_java(mlist)
    src_idx = get_index_src(mlist)
    package_name = get_package_name(mlist, src_idx, java_idx)
    if button:
        # print("path %s \n" % path)
        print("package name : %s" % package_name)
    return package_name


def get_git_repo_name_print(path, button=False):
    mlist = spilt_by_path(path)
    ws_idx = get_index_workspace(mlist)
    git_name = get_git_repo_name(mlist, ws_idx)
    if(button):
        print("git name : %s" % git_name)
    return git_name


if __name__ == "__main__":
    get_git_repo_name_print(fileDir, True)