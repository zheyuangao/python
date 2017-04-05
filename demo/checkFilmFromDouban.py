# -*- coding: cp936 -*-

import os
import os.path
from urllib import request
import  re
import io
import sys
from bs4 import BeautifulSoup
def getDirDict(path):
    paths = {}
    for dirpath, dirnames, filenames in os.walk(rootdir):
        # for dirname in dirnames:  # 输出文件夹信息
        #     print("parent is:" + dirpath)
        #     print("dirname is" + dirname)

        for filename in filenames:  # 输出文件信息
            print("=============================================================")
            # print("parent is" + dirpath)
            # print("filename is:" + filename)
            if ']' in filename:
                path1 = filename.split(']')
                real_file_name = path1[1].split('.')[1]
                print('has [] ：' + real_file_name)
                paths[os.path.join(dirpath, filename)] = real_file_name
            else:
                print('not has []')
            # print("the full name of the file is:" + os.path.join(dirpath, filename))
    return paths


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
rootdir = input('in:')
# rootdir = 'E:\迅雷下载'
pathDict = getDirDict(rootdir)
for value in pathDict.values():
    value=request.quote(value)
    path = 'https://movie.douban.com/subject_search?search_text='+value
    print(path)
    with request.urlopen(path) as f:
        data = f.read()

        # print('Status:', f.status, f.reason)
        # for k, v in f.getheaders():
        #     print('%s: %s' % (k, v))
        # print('Data:', data.decode('utf-8'))
        soup = BeautifulSoup(data,'html.parser')
        title = soup.find("div","pl2").a.get_text()
        if '/' in title:
            print('/ in title')
            title = title.split('/')[0]
        else:
            print('/ not in title')
        title = title.strip()
        score= soup.find('span','rating_nums').get_text()
        print(title+score)
