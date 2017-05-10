#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
def change_file_name(old , new):
    os.rename(old,new)

def getDirDict(path):
    paths = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:  # 输出文件信息
            print("=============================================================")
            print(filename)
            if ']' in filename:
                path1 = re.findall('(?<=]\.)[\u4e00-\u9fa5]+', filename)
                if len(path1)==0:
                    path1 = re.findall('(?<=])[\u4e00-\u9fa5]+', filename)
                for path in path1:
                    if path == '':
                        pass
                    else:
                        file_name=path;
                real_file_name=file_name.replace('.','')
            else:
                path1=re.findall('[\u4e00-\u9fa5]*\d*',filename)
                real_file_name = path1[0].replace('.', '')
            print(real_file_name)
            paths[os.path.join(dirpath, filename)] = real_file_name
            # print("the full name of the file is:" + os.path.join(dirpath, filename))
    return paths