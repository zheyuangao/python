from urllib import request
from bs4 import BeautifulSoup
import re
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Connection": "keep-alive"
}
# return location_category_
def get_movie_detail(path):
    req = request.Request(path, None, header)
    r = request.urlopen(req)
    data = r.read().decode('utf-8')
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    info = soup.find(id='info').get_text()
    pattern = re.compile('类型:.*')
    s = pattern.findall(info)
    pattern = re.compile('[^类型](\S\S)')
    k = pattern.findall(s[0])
    back = ''
    for i in k:
        back += i
    back += '_'
    pattern = re.compile('制片国家/地区:.*')
    s = pattern.findall(info)
    pattern = re.compile('[^制片国家/地区](\S\S)')
    k = pattern.findall(s[0])
    for i in k:
        back += i
    return back

def get_movie_name_mobile(key ,value):
    print('=======================' + value)
    value = request.quote(value)
    path = 'https://m.douban.com/search/?query=' + value
    req = request.Request(path, None, header)
    r = request.urlopen(req)
    data = r.read().decode('utf-8')
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    try:
        title_full = soup.find('div','subject-info').find('span').get_text()
    except:
        print('!!!!!!!!!! can not request ' + request.unquote(value, 'utf-8', 'replace') + 'skip')
        return None
    url=''
    for aList in soup.find_all('a'):
        if '/movie/subject' in aList.get('href'):
            url=aList.get('href')
            break
    if url is None:
        print('get url faild')
        return None
    time.sleep(0.3)
    category_back = get_movie_detail('https://m.douban.com'+url)
    score = soup.find('div','subject-info').find('p','rating').get_text().strip()
    title_final = title_full + '_' + score + '_' + category_back
    if request.unquote(value, 'utf-8', 'replace') != title_full:
        print(
            'callback title not same input: ' + request.unquote(value, 'utf-8', 'replace') + ",callback:" + title_full)
        print('callback :' + title_final)
        return None
    else:
        head = re.compile('.*\\\\').findall(key)
        foot = re.compile('\.\w+').findall(key)
        file_name = head[0] + title_final + foot[foot.__len__() - 1]
        return file_name

def get_movie_name(key ,value):
    print('=======================' + value)
    value = request.quote(value)
    path = 'https://movie.douban.com/subject_search?search_text=' + value
    req = request.Request(path, None, header)
    r = request.urlopen(req)
    data = r.read().decode('utf-8')
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    try:
        title_full = soup.find("div", "pl2").a.get_text()
    except:
        print('!!!!!!!!!! can not request ' + request.unquote(value, 'utf-8', 'replace') + 'skip')
        return None
    url = soup.find("div", "pl2").a.get('href')
    category_back = get_movie_detail(url)
    if '/' in title_full:
        title_real = title_full.split('/')[0]
    else:
        title_real = title_full
    title_real = title_real.strip()
    score = soup.find('span', 'rating_nums').get_text()
    title_final = title_real + '_' + score + '_' + category_back
    if request.unquote(value, 'utf-8', 'replace') != title_real:
        print(
            'callback title not same input: ' + request.unquote(value, 'utf-8', 'replace') + ",callback:" + title_full)
        print('callback :' + title_final)
        return None
    else:
        head = re.compile('.*\\\\').findall(key)
        foot = re.compile('\.\w+').findall(key)
        file_name = head[0] + title_final + foot[foot.__len__() - 1]
        return file_name
