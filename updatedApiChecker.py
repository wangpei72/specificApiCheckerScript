#!/usr/bin/python
# -*- coding: utf-8 -*-
import fileListParser as flp
import re
import os

# 该类用于查找单个java文件中是否包含以下api，并且在查找出的情况下给出所在包名、文件名、行号

# 一些api的定义
apiESD = "Environment.getExternalStorageDirectory"
apiESPD = "Environment.getExternalStoragePublicDirectory"
apiDCD = "Environment.getDownloadCacheDirectory"
apiSD = "Environment.getStorageDirectory"
apiDD = "Environment.getDataDirectory"
apiRD = "Environment.getRootDirectory"

# 硬编码目录
pathSDCard = "/sdcard/"
pathMNT = "/mnt/"

# 测试用目录
fileDir = "/Users/wangpei/workspace/AliSourcingProject/AliSourcingBuyerPoseidons/src-hook/com/alibaba/intl/android/apps" \
          "/poseidon/utils/EnvironmentInspector.java "


# 传入当前匹配的正则表达式，如果查找到给出的提示信息，被搜索的文件名
def check_for_upated_api(file_dir, m_re=None):
    line_num = 0
    hit_num = 0
    hit_line_num = []
    hit_kind = m_re

    git_name = flp.get_git_repo_name_print(file_dir)
    file_name = flp.get_java_file_name_print(file_dir)
    package_name = flp.get_package_name_print(file_dir)
    str_file = git_name + "/" + package_name + "." + file_name + ".java"
    curDiry = os.path.dirname(os.path.realpath(__file__))
    if m_re is None:
        print("m_re is Node! plz specific the api you are searching for.")
        return -1
    with open(file_dir[0:-1], "r+") as f:
        lines = f.readlines()
        for line in lines:
            line_num += 1
            if m_re in line:
                hit_num += 1
                hit_line_num.append(line_num)
                print("------>>> found api %s in file %s at line %d  hit_num for it in this file in total %d<<<------" % (hit_kind,
                                                                                                             str_file,
                                                                                                             line_num,
                                                                                                             hit_num))
    if hit_num == 0:
        pass
        # print("specific api: %s not found in file %s" % (hit_kind, str_file))
    return hit_num, hit_line_num


def check_for_path_hard_coded(file_dir, m_re=None):
    line_num = 0
    hit_num = 0
    hit_kind = m_re
    hit_line_num = []

    git_name = flp.get_git_repo_name_print(file_dir)
    file_name = flp.get_java_file_name_print(file_dir)
    package_name = flp.get_package_name_print(file_dir)
    str_file = git_name +"/" + package_name + "." + file_name + ".java"
    if m_re is None:
        print("plz provide your regex for hard code search.")
        return -1
    with open(file_dir[0:-1], "r+") as f:
        lines = f.readlines()
        for line in lines:
            line_num += 1
            if m_re in line:
                hit_num += 1
                hit_line_num.append(line_num)
                print("-----!!! found hard coded path %s not supported in tar30 at line %d. hit_num in this file now "
                      "is %d "
                      "!!!----- "
                      % (hit_kind, line_num, hit_num))
    if hit_num == 0:
        pass
        # print("specific path %s not found in this file %s."% (m_re, str_file))
    return hit_num, hit_line_num


# 各个api检查函数
def check_for_ESD(file_dir):
    # print("searching for ESD...")
    return check_for_upated_api(file_dir, apiESD)


def check_for_ESPD(file_dir):
    # print("searching for ESPD...")
    return check_for_upated_api(file_dir, apiESPD)


def check_for_DCD(file_dir):
    # print("searching for DCD...")
    return check_for_upated_api(file_dir, apiDCD)


def check_for_SD(file_dir):
    # print("searching for SD...")
    return check_for_upated_api(file_dir, apiSD)


def check_for_DD(file_dir):
    # print("searching for DD...")
    return check_for_upated_api(file_dir, apiDD)


def check_for_RD(file_dir):
    # print("searching for RD...")
    return check_for_upated_api(file_dir, apiRD)


def check_for_hard_code(file_dir, m_re):
    # print("searching for hard coded path %s ..."% m_re)
    return check_for_path_hard_coded(file_dir, m_re)


def check_file_for_api_allinone(file_dir):  # check单个java文件中的结果并且返回dic
    dic = {}
    # 以下是
    hit_ESD = check_for_ESD(file_dir)
    hit_ESPD = check_for_ESPD(file_dir)
    hit_DCD = check_for_DCD(file_dir)
    hit_SD = check_for_SD(file_dir)
    hit_DD = check_for_DD(file_dir)
    hit_RD = check_for_RD(file_dir)
    hit_mnt = check_for_hard_code(file_dir, pathMNT)
    hit_sdCard = check_for_hard_code(file_dir, pathSDCard)

    # 以下是文件信息 git仓库 tag：包名/java文件名
    git_name = flp.get_git_repo_name_print(file_dir)
    file_name = flp.get_java_file_name_print(file_dir)
    package_name = flp.get_package_name_print(file_dir)
    str_file = package_name + "." + file_name + ".java"
    # --------打印提示当前搜索的单个文件---------
    # print("searching in %s ..." % str_file)
    dic['git_name'] = git_name  # 可能有多行希望合并单元格
    dic['tag'] = package_name + ":" + file_name + ".java"
    # dic['pkg_name'] = package_name
    # dic['file_name'] = file_name
    dic['ESD'] = hit_ESD[0]
    dic['lines_ESD'] = hit_ESD[1]

    dic['ESPD'] = hit_ESPD[0]
    dic['lines_ESPD'] = hit_ESPD[1]

    dic['DCD'] = hit_DCD[0]
    dic['lines_DCD'] = hit_DCD[1]

    dic['SD'] = hit_SD[0]
    dic['lines_SD'] = hit_SD[1]

    dic['DD'] = hit_DD[0]
    dic['lines_DD'] = hit_DD[1]

    dic['RD'] = hit_RD[0]
    dic['lines_RD'] = hit_RD[1]

    dic['mnt'] = hit_mnt[0]
    dic['lines_mnt'] = hit_mnt[1]

    dic['sdCard'] = hit_sdCard[0]
    dic['lines_sdCard'] = hit_sdCard[1]

    total = hit_ESD[0] + hit_ESPD[0] + hit_DCD[0] + hit_SD[0] + hit_DD[0] + hit_RD[0] + hit_mnt[0] + hit_sdCard[0]
    dic['total'] = total

    if total != 0:
        # ----发现调用结果提示-----
        # print("specific api: not found in file %s" % str_file)
        # print('\033[1;33;44mThis is a test !\033[0m')
        print("\033[7;31;40m------>>> FOUND target api in file %s , plz give attention!<<<-------\033[0m" % str_file)
    # print("dic:",  dic)
    return dic


if __name__ == "__main__":
    check_file_for_api_allinone(fileDir)
