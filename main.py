import urllib.request
import http.cookiejar
import ssl
from Crypto.Cipher import AES
import base64
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.header import Header

"""
url = "https://music.163.com/"  # homepage
ssl._create_default_https_context = ssl._create_unverified_context
data = urllib.request.urlopen(url).read().decode('utf-8')


def makeMyOpener(head):

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header

    return opener

headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Connection': 'keep-alive',
             'Cookie': '_ntes_nuid=aaf4f6ab4c0f1a0625e3375535676656; vjuids=-136ff0311.15bc23a4ff0.0.2763f1a1bb1bf; _ga=GA1.2.1693856492.1494482682; _ngd_tid=ohzQjVMtXobqCgKX53dOOJPCoZND9ZKA; _iuqxldmzr_=32; _ntes_nnid=aaf4f6ab4c0f1a0625e3375535676656,1524972414127; mail_psc_fingerprint=c131d8c1d1e0b41e212c049d0e8cd2b2; usertrack=O2+gyls1w6QhUWcPA3mmAg==; WM_TID=8S%2BxW61mqmApRo9bfcdMgaH6AkhoiTQ8; __oc_uuid=2ccc02f0-9157-11e8-8bb1-6191b8199f1f; __utma=187553192.1693856492.1494482682.1532666424.1532666424.1; __utmz=187553192.1532666424.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; NTES_CMT_USER_INFO=85651346%7Cidle7echo%7Chttp%3A%2F%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif%7Cfalse%7CaWRsZTAwMUAxMjYuY29t; mp_MA-9ADA-91BF1A6C9E06_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fcampus.163.com%2Fapp%2Fhy%2Flh%22%2C%22updatedTime%22%3A%201538198006028%2C%22sessionStartTime%22%3A%201538198006023%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%2286f24670-017a-416d-999a-bef4a1674aa2%22%2C%22persistedTime%22%3A%201534218935561%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201538198006029%7D%2C%22sessionUuid%22%3A%20%22eaf6d550-d14e-4583-b78c-ef4df97c7399%22%7D; vinfo_n_f_l_n3=b7cb0f867b47f948.1.4.1493612253192.1520003130603.1540371640919; __f_=1540888102421; ANTICSRF=25b800198f557f5b68e12637e693d205; playliststatus=visible; __utmc=94650624; vjlast=1493612253.1545226642.22; NTES_SESS=0_Xx1UXvE0VZUUvUg9Uf6sWBgMF9sW4v8UuSBL30iDzNO1zGOBYERD2trLl3Dg7L.LHaizdA4h9PD.nweEP.C2X70oEvauD9cTgsE3N.hp.bI9Y_sKXh3BXyYQQgfrxMhuD1f7qsi0ALYWirdhs8VGxSwe09S7TQnPOwv1bG2Ck5plvP5wyfXrNAIUCMsDvs8zMt.FsT.BKtw6fyJ2tShRe6V1nJTF_Uv6QsCGUFNdgsk; P_INFO=idle001@126.com|1545620271|0|mail126|11&12|bej&1545391677&mail126#bej&null#10#0#0|130165&0|mail126|idle001@126.com; S_INFO=1545620271|0|#3&100#|idle001@126.com; MUSIC_EMAIL_U=9e3c31275f4de54bc16fb664e7e6ecca77451908902688db7a926360334e19e93c12fb440e0ea128cc218dc06fc10632b0d15bef322b74f7c3061cd18d77b7a0; playerid=33147134; WM_NI=1TiHOB4ozHkt3k%2B3st9ad0qd3fCvu5tm3XB2kvhz8zMZ7IbjD9PTyY4T07rCn4f4bWS8cf9yAlwvrSLKS7nL3vhIjzpP3NAMc5uuW2tNXP4kd0B8nwUU%2FENtx0jtu9SDc2w%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacaa52bab2feb9f9688eb08ba2c14f869a9eabbc6bedabffa8dc21ba9dac85d62af0fea7c3b92af38ca7a9ce4af8b1b6a9ea80f1b5e5d4f280fbbfacd1f470f1ba8d97f83fb8b3fdb9c13aa9aaa89bbb728f86f9aae16288e7a0b5fc53f88c00d8f149aeecaad5e15d91e8ad87bc7383b4b997f15990959dd8ed48f1aaa8aae972b490fdafc447a1ebbb96d63ab89298b1b761a8f08ed9ed7d978be1a6cd80bcf0a695f833919cadd3f637e2a3; __utma=94650624.1693856492.1494482682.1546075856.1546178987.37; __utmz=94650624.1546178987.37.17.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=o92%2Foy1tNdtIGF81l%2FJfJkiKIBl19SFBdwEv%2FDfqJf%2Fhepp13kEsTfqD%2B5mS%2F8QsVDFcuwOqURaYlSsPDe1%2Fo97OT2jUmNh5%5C%2B5elgzlC4aJHdSnt3qWWCkzqfpQAvKJa5EBNF0YMq%2BMgHsNt%5CuHG0B1eJPy6hXCZcB1UxZA8pehFgx2%3A1546186693712',
             'Host': 'music.163.com',
             'Referer': 'http://music.163.com/',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/66.0.3359.181 Safari/537.36'}
comments_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_"
ssl._create_default_https_context = ssl._create_unverified_context
op = makeMyOpener(headers)
data = op.open(comments_url).read().decode('utf-8')
#data = urllib.request.urlopen(comments_url).read().decode('utf-8')
"""

def AESencrypt(msg, key, iv):
    padding = 16 - len(msg) % 16
    msg = msg + str(padding * '0')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encryptedbytes = cipher.encrypt(msg)
    # 使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    return encodestrs

# RSA加密
def RSAencrypt(randomstrs, key, f):
    # 随机字符串逆序排列
    string = randomstrs[::-1]
    # 将随机字符串转换成byte类型数据
    text = bytes(string, 'utf-8')
    seckey = int(text.hex(), 16)**int(key, 16) % int(f, 16)
    return format(seckey, 'x').zfill(256)


# 获取参数
def get_params(page):
    # msg也可以写成msg = {"offset":"页面偏移量=(页数-1) *　20", "limit":"20"},offset和limit这两个参数必须有(js)
    # limit最大值为100,当设为100时,获取第二页时,默认前一页是20个评论,也就是说第二页最新评论有80个,有20个是第一页显示的
    # msg = '{"rid":"R_SO_4_1302938992","offset":"0","total":"True","limit":"100","csrf_token":""}'
    # 偏移量
    offset = (page-1) * 20
    # offset和limit是必选参数,其他参数是可选的,其他参数不影响data数据的生成
    msg = '{"offset":' + str(offset) + ',"total":"True","limit":"20","csrf_token":""}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    iv = '0102030405060708'
    i = '0' * 16
    enctext = AESencrypt(msg, key,iv)
    encText = AESencrypt(enctext.decode('utf-8'),i,iv)
    # RSA加密之后得到encSecKey的值
    encSecKey = RSAencrypt(i, e, f)
    data = dict()
    data['params','encSecKey'] = encText, encSecKey
    return data

def judge_adding(song_id):

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': '_ntes_nuid=aaf4f6ab4c0f1a0625e3375535676656; vjuids=-136ff0311.15bc23a4ff0.0.2763f1a1bb1bf; _ga=GA1.2.1693856492.1494482682; _ngd_tid=ohzQjVMtXobqCgKX53dOOJPCoZND9ZKA; _iuqxldmzr_=32; _ntes_nnid=aaf4f6ab4c0f1a0625e3375535676656,1524972414127; mail_psc_fingerprint=c131d8c1d1e0b41e212c049d0e8cd2b2; usertrack=O2+gyls1w6QhUWcPA3mmAg==; WM_TID=8S%2BxW61mqmApRo9bfcdMgaH6AkhoiTQ8; __oc_uuid=2ccc02f0-9157-11e8-8bb1-6191b8199f1f; __utma=187553192.1693856492.1494482682.1532666424.1532666424.1; __utmz=187553192.1532666424.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; NTES_CMT_USER_INFO=85651346%7Cidle7echo%7Chttp%3A%2F%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif%7Cfalse%7CaWRsZTAwMUAxMjYuY29t; mp_MA-9ADA-91BF1A6C9E06_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fcampus.163.com%2Fapp%2Fhy%2Flh%22%2C%22updatedTime%22%3A%201538198006028%2C%22sessionStartTime%22%3A%201538198006023%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%2286f24670-017a-416d-999a-bef4a1674aa2%22%2C%22persistedTime%22%3A%201534218935561%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201538198006029%7D%2C%22sessionUuid%22%3A%20%22eaf6d550-d14e-4583-b78c-ef4df97c7399%22%7D; vinfo_n_f_l_n3=b7cb0f867b47f948.1.4.1493612253192.1520003130603.1540371640919; __f_=1540888102421; ANTICSRF=25b800198f557f5b68e12637e693d205; playliststatus=visible; __utmc=94650624; vjlast=1493612253.1545226642.22; NTES_SESS=0_Xx1UXvE0VZUUvUg9Uf6sWBgMF9sW4v8UuSBL30iDzNO1zGOBYERD2trLl3Dg7L.LHaizdA4h9PD.nweEP.C2X70oEvauD9cTgsE3N.hp.bI9Y_sKXh3BXyYQQgfrxMhuD1f7qsi0ALYWirdhs8VGxSwe09S7TQnPOwv1bG2Ck5plvP5wyfXrNAIUCMsDvs8zMt.FsT.BKtw6fyJ2tShRe6V1nJTF_Uv6QsCGUFNdgsk; P_INFO=idle001@126.com|1545620271|0|mail126|11&12|bej&1545391677&mail126#bej&null#10#0#0|130165&0|mail126|idle001@126.com; S_INFO=1545620271|0|#3&100#|idle001@126.com; MUSIC_EMAIL_U=9e3c31275f4de54bc16fb664e7e6ecca77451908902688db7a926360334e19e93c12fb440e0ea128cc218dc06fc10632b0d15bef322b74f7c3061cd18d77b7a0; playerid=33147134; WM_NI=1TiHOB4ozHkt3k%2B3st9ad0qd3fCvu5tm3XB2kvhz8zMZ7IbjD9PTyY4T07rCn4f4bWS8cf9yAlwvrSLKS7nL3vhIjzpP3NAMc5uuW2tNXP4kd0B8nwUU%2FENtx0jtu9SDc2w%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacaa52bab2feb9f9688eb08ba2c14f869a9eabbc6bedabffa8dc21ba9dac85d62af0fea7c3b92af38ca7a9ce4af8b1b6a9ea80f1b5e5d4f280fbbfacd1f470f1ba8d97f83fb8b3fdb9c13aa9aaa89bbb728f86f9aae16288e7a0b5fc53f88c00d8f149aeecaad5e15d91e8ad87bc7383b4b997f15990959dd8ed48f1aaa8aae972b490fdafc447a1ebbb96d63ab89298b1b761a8f08ed9ed7d978be1a6cd80bcf0a695f833919cadd3f637e2a3; __utma=94650624.1693856492.1494482682.1546075856.1546178987.37; __utmz=94650624.1546178987.37.17.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=o92%2Foy1tNdtIGF81l%2FJfJkiKIBl19SFBdwEv%2FDfqJf%2Fhepp13kEsTfqD%2B5mS%2F8QsVDFcuwOqURaYlSsPDe1%2Fo97OT2jUmNh5%5C%2B5elgzlC4aJHdSnt3qWWCkzqfpQAvKJa5EBNF0YMq%2BMgHsNt%5CuHG0B1eJPy6hXCZcB1UxZA8pehFgx2%3A1546186693712',
               'Host': 'music.163.com',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    comments_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + str(song_id) + "?crsf_token="
    # ssl._create_default_https_context = ssl._create_unverified_context
    # data_para = get_params(1)
    data_para ={
        'params':'AP76nG2pMQ2FzFklvBgh0gJrRT+4vYTNs8Z6W2jKw8zyDqron1mehTRfmF/Ngh9dOIRqkB9sO2G+6HHuDpB4c82rrYI542EFC94YqI7dKhp7afIq8wKhITpRxDDxqJR7',
        'encSecKey':'babc57ca9e9ffb0a879ae290ac6cba6f60620aa9ae3b36a84585e23bbc73d73b13a2ebab4aa2ee80544d255727adc5a04db613d77d02a62a52b3a03134d16f191d54675f560f797c7f03e3a30c43df8b1b49878fd225b62f5f78041427debc3e95b93582f130618630702621da4eda9c71af91836cc39ab3b760b033643a1889'
    }
    data = requests.post(comments_url, headers =headers, data=data_para)

    if data.json['total'] > 100000:
        return True
    else:
        return False

def send_mail():
    mail_host = "smtp.XXX.com"  # 设置服务器
    mail_user = "XXXX"  # 用户名
    mail_pass = "XXXXXX"  # 口令

    receivers = ['idle001@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText('Finished', 'plain', 'utf-8')
    message['From'] = Header("Cloud", 'utf-8')
    message['To'] = Header("Master", 'utf-8')
    subject = 'Running consequence'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':

    from script import check_configue
    import logging
    import time

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    handler = logging.FileHandler('main.log')
    logger.addHandler(handler)

    check_configue()
    # config webdriver
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

    singerlist_url = 'https://music.163.com/discover/artist/cat?' # id=(1-5)00(1-5), initial ord(A-Z),0,-1
    id = [1001, 1002, 1003, 2001, 2002, 2003, 3001, 3002, 3003, 4001, 4002, 4003]
    init = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
           90]
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
    music_list_url = 'https://music.163.com/#/artist?id='
    se = re.compile('\d+')
    csf = np.empty((0,2))
    x = []
    try:
        for i in id:
            for j in init:
                url = singerlist_url + 'id=' + str(i) + '&initial=' + str(j)
                print(url)
                data = requests.get(url, headers=headers)
                soup = BeautifulSoup(data.text, "html5lib")
                results = soup.find_all('a', attrs={'class':'nm nm-icn f-thide s-fc0'})
                for child in results:
                    id_artist = se.search(child['href']).group()
                    csf = np.append(csf, [[id_artist, child.get_text()]], axis=0)
                    albulm_url = music_list_url + str(id_artist)
                    print(child.get_text())
                    # browser.get(albulm_url)
                    # res = browser.switch_to.frame("g_iframe")
                    session = HTMLSession()
                    r = session.get(albulm_url)
                    r.html.render()
                    music_soup = BeautifulSoup(r.text, 'html5lib')
                    ul = soup.find('ul', attrs={'class': 'f-hide'}).find_all('a')
                    music_dic = dict()
                    for link in ul:
                        music_id = se.findall(link['href'])[0]
                        music_name = link.get_text()
                        if judge_adding(music_id):
                            #add song in to list
                            #TODO: Star music through api in Netease music further
                            music_dic['编号'] = music_id
                            music_dic['歌名'] = music_name
                            music_dic['歌手'] = child.get_text()
                            x.append(music_dic)
                    time.sleep(1)
        pf = pd.DataFrame(csf,columns=['id','歌手'])
        py = pd.DataFrame(x,columns=['id','music','singer'])
        pf.to_csv('singerlist.csv')
        py.to_csv('music.csv')
    except:
        logger.exception('Something is not formal')
    send_mail()


