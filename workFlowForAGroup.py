#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import fileListGetter as getter
import wrtXlsForOneFileList as writer


def get_file_lists(group_dir_, file_lists_dir_):  # 会在指定目录下生成所有txt文件
    getter.get_file_lists_allinone(group_dir_, file_lists_dir_)


def wrt_all_lists_res(file_lists_dir_, xls_output_path='output.xls'):
    # cur_dir_ = os.path.dirname(os.path.realpath(__file__))
    txt_files = os.listdir(file_lists_dir_)
    for txt_file in txt_files:
        # 这里源txt文件可能存在相对路径和绝对路径相冲突的问题
        writer.wrt_res_xls_content(file_lists_dir_ + "/" + txt_file, xls_output_path)


def workflow_start(group_dir_, file_lists_dir_, xls_output_path='output.xls'):
    get_file_lists(group_dir_, file_lists_dir_)
    writer.wrt_xls_file_header(xls_output_path)
    wrt_all_lists_res(file_lists_dir_, xls_output_path)
    writer.set_width_via_context(xls_output_path)


if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    xls_out_path = "output_sourcing2.xls"
    file_lists_dir = os.path.join(cur_dir, "fileListsFromSourcing")
    group_dir = "/Users/wangpei/git-group-sourcing-project/"
    workflow_start(group_dir, file_lists_dir, xls_out_path)

