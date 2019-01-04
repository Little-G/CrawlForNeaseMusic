# import re
# import urllib.parse
# import urllib.request
# from collections import deque
# import http.cookiejar
# import ssl
#
# url = "https://music.163.com/"
# ssl._create_default_https_context = ssl._create_unverified_context
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print(data)

# url = 'http://www.baidu.com/'
# word = dict()
# word['word'] = 'python'
#
# suffix = urllib.parse.urlencode(word)
# f_url = url + suffix
# data = urllib.request.urlopen(url).read().decode('UTF-8')
# print(data)
# d = deque(['1','2',3])
# d.append('1')






# head: dict of header
# def makeMyOpener(head = {'Connection': 'Keep-Alive',
#                          'Accept': 'text/html, application/xhtml+xml, */*',
#                          'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
#                          }):
#     cj = http.cookiejar.CookieJar()
#
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#
#     header = []
#     for key, value in head.items():
#         elem = (key, value)
#         header.append(elem)
#     opener.addheaders = header
#
#     return opener
#
#
# oper = makeMyOpener()
# uop = oper.open('http://www.zhihu.com/', timeout=1000)
# data = uop.read()
# fout = open('otput.html', 'w',encoding='utf-8')
# fout.write(data.decode('utf-8'))
# fout.close()
# print(oper)
# print(data.decode('utf-8'))

# import gzip
# import re
# import http.cookiejar
# import urllib.request
# import urllib.parse
# import ssl
#
# def ungzip(data):
#     try:  # 尝试解压
#         print('正在解压.....')
#         data = gzip.decompress(data)
#         print('解压完毕!')
#     except:
#         print('未经压缩, 无需解压')
#     return data
#
#
# def getXSRF(data):
#     cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
#     strlist = cer.findall(data)
#     return strlist[0]
#
#
# def getOpener(head):
#     # deal with the Cookies
#     cj = http.cookiejar.CookieJar()
#     pro = urllib.request.HTTPCookieProcessor(cj)
#     opener = urllib.request.build_opener(pro)
#     header = []
#     for key, value in head.items():
#         elem = (key, value)
#         header.append(elem)
#     opener.addheaders = header
#     return opener
#
#
# header = {
#     'Connection': 'Keep-Alive',
#     'Accept': 'text/html, application/xhtml+xml, */*',
#     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
#     'Accept-Encoding': 'gzip, deflate',
#     'Host': 'www.zhihu.com',
#     'DNT': '1'
# }
# ssl._create_default_https_context = ssl._create_unverified_context
# url = 'http://www.zhihu.com/'
# opener = getOpener(header)
# op = opener.open(url)
# data = op.read()
# data = ungzip(data)  # 解压
# print(data.decode('utf-8'))
#_xsrf = getXSRF(data.decode('utf-8'))

# url += 'login'
# id = '这里填你的知乎帐号'
# password = '这里填你的知乎密码'
# postDict = {
#     '_xsrf': _xsrf,
#     'email': id,
#     'password': password,
#     'rememberme': 'y'
# }
# postData = urllib.parse.urlencode(postDict).encode()
# op = opener.open(url, postData)
# data = op.read()
# data = ungzip(data)

#print(data.decode())

#learn dict in python
# list1 = [1,2,3]
# list2 = ['1','2','3']
# list3 =[[1,2],[2,3]]
# test = dict(map(lambda x,y:[x,y],list1,list2))
# a = map(lambda x,y:[x,y],list1,list2)
# test2 = dict(i for i in list3)
# print(test)
# print(list(a))
# print(test2)
# line = "Cats are smarter than dogs aer are Pigs are ab"
# matchObj = re.match( r'(.*?) are (.*?) .* (ab*?)', line, re.M|re.I)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
#     print("matchObj.group(3) : ", matchObj.group(3))
# else:
#     print("No match!!")

""""""""""""
import requests
import math
import random
# pycrypto
from Crypto.Cipher import AES
import codecs
import base64
from bs4 import BeautifulSoup
import re

# 生成16个随机字符
def generate_random_strs(length):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # 控制次数参数i
    i = 0
    # 初始化随机字符串
    random_strs  = ""
    while i < length:
        e = random.random() * len(string)
        # 向下取整
        e = math.floor(e)
        random_strs = random_strs + list(string)[e]
        i = i + 1
    return random_strs


# AES加密
def AESencrypt(msg, key):
    # 如果不是16的倍数则进行填充(paddiing)

    # 用来加密或者解密的初始向量(必须是16位)
    iv = '0102030405060708'

    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 加密后得到的是bytes类型的数据
    encryptedbytes = cipher.encrypt(msg)
    # 使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf-8')

    return enctext


# RSA加密
def RSAencrypt(randomstrs, key, f):
    # 随机字符串逆序排列
    string = randomstrs[::-1]
    # 将随机字符串转换成byte类型数据
    text = bytes(string, 'utf-8')
    seckey = int(codecs.encode(text, encoding='hex'), 16)**int(key, 16) % int(f, 16)
    return format(seckey, 'x').zfill(256)


# 获取参数
def get_params(songid):
    # id为歌曲的id号,后面的lv和tv都是固定值
    msg = '{id: ' + str(songid) + ', lv: -1, tv: -1}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    enctext = AESencrypt(msg, key)
    # 生成长度为16的随机字符串
    i = generate_random_strs(16)

    # 两次AES加密之后得到params的值
    encText = AESencrypt(enctext, i)
    # RSA加密之后得到encSecKey的值
    encSecKey = RSAencrypt(i, e, f)
    return encText, encSecKey


def main():

    # Dream it possible
    # 歌曲id号
    songid = 38592976
    # params的长度为108,不要拿浏览器控制面板中的数据进行测试,那里的params长度为128,不符合
    params, encSecKey = get_params(songid)
    data = {'params': params, 'encSecKey': encSecKey}
    url = 'https://music.163.com/weapi/song/lyric?csrf_token='
    r = requests.post(url, data=data)
    # 状态码
    print(r.status_code)
    print(r.json())


if __name__ == "__main__":
    def get_artists(url):
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'keep-alive',
                   'Cookie': '_iuqxldmzr_=32; _ntes_nnid=0e6e1606eb78758c48c3fc823c6c57dd,1527314455632; '
                             '_ntes_nuid=0e6e1606eb78758c48c3fc823c6c57dd; __utmc=94650624; __utmz=94650624.1527314456.1.1.'
                             'utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=blBrSVohtue8%2B6VgDkxOkJ2G0VyAgyOY;'
                             ' JSESSIONID-WYYY=Du06y%5Csx0ddxxx8n6G6Dwk97Dhy2vuMzYDhQY8D%2BmW3vlbshKsMRxS%2BJYEnvCCh%5CKY'
                             'x2hJ5xhmAy8W%5CT%2BKqwjWnTDaOzhlQj19AuJwMttOIh5T%5C05uByqO%2FWM%2F1ZS9sqjslE2AC8YD7h7Tt0Shufi'
                             '2d077U9tlBepCx048eEImRkXDkr%3A1527321477141; __utma=94650624.1687343966.1527314456.1527314456'
                             '.1527319890.2; __utmb=94650624.3.10.1527319890',
                   'Host': 'music.163.com',
                   'Referer': 'http://music.163.com/',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/66.0.3359.181 Safari/537.36'}
        r = requests.get(url, headers=headers)

        return r


    ls1 = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]  # id的值
    ls2 = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
           90]  # initial的值


    url = 'https://music.163.com/artist?id=5781'
    # r = get_artists(url)

    # a = soup.p.a
    se = re.compile('\d+')
    # print(a['href'])
    # print(se.findall(a['href']))
    # from selenium import webdriver
    #
    # virbr = webdriver.Chrome()
    # page = virbr.get('https://music.163.com/artist?id=5781')
    # virbr.switch_to.frame("g_iframe")
    # print(virbr.page_source)

    # from requests_html import HTMLSession
    #
    # session = HTMLSession()
    # #r = session.get('https://www.jobbnorge.no/en/available-jobs/job/148574/project-manager-researcher-translational-nk-cell-biology')
    # r = session.get(url)
    # r.html.render()
    # soup = BeautifulSoup(r.text, "html5lib")
    # ul = soup.find('ul',attrs={'class':'f-hide'}).find_all('a')
    # for i in ul:
    #     print(se.findall(i['href'])[0],i.get_text())
    # soup = BeautifulSoup('''
    #     <span class="count">
    #     <i class="icon-user">1</i>
    #     30.5K<a>1</a> </span>
    # ''','html5lib')
    # usercount = soup.find('span', class_='count').strings
    # for i in usercount:
    #     print(i)
    # import pandas as pd
    # x = [{'a':'b','b':'c'},{'a':'d','d':'e'}]
    # pf = pd.DataFrame(x)
    # print(pf)

    #nohup
    # 自己打印自己的代码
    # import sys
    # import time
    # # 读取并输出的就是该程序文件out_put_self.py
    # f_name = sys.argv[0]
    # with open(f_name, 'r', encoding='utf-8') as f:
    #     line_int = 0
    #     while True:
    #         line_int += 1
    #         line_str = f.readline()
    #         # 如果读到的行为空，就结束
    #         if line_str:
    #             time.sleep(0.5)
    #             for word in line_str:
    #                 print('{}'.format(word),end='')
    #
    #
    #         else:
    #             break

    import os
    import logging
    try:
        openFile = open('notExistsFile.txt', 'r')
        fileContent = openFile.readlines()
    except ZeroDivisionError:
        print('File not Exists')
        if not os.path.exists('notExistsFile.txt'):
            raise
            pass





