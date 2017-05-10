#!/usr/bin/python
# -*- coding: UTF-8 -*-
import io
import sys
from datetime import datetime
from demo.fileUtil import getDirDict, change_file_name
from demo.netutil import get_movie_name
import time


need_check_net = True
need_change_name = False
# rootdir = input('in:')
rootdir = 'G:\电影\电影'
# rootdir = 'G:\电影\亚洲'
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def check_from_net(pathDict):
    for key in pathDict.keys():
        name_new = get_movie_name(key, pathDict.get(key))
        if name_new is None:
            continue
        else:
            print('file name change from :' + key + "\n  to :" + name_new)
            if need_change_name:
                change_file_name(key, name_new)
        time.sleep(1)
        break

def main():
    pathDict = getDirDict(rootdir)
    print("=============================================================")
    if need_check_net:
        check_from_net(pathDict)


if __name__ == '__main__':
    main()
