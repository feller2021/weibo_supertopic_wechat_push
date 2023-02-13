import json
import time
from pprint import pprint
from pypushdeer import PushDeer
import os
import requests
import re
from lxml import etree

# https://m.weibo.cn/status/4669812238457985
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Accept': 'application/json, text/plain, */*','Connection':'close',
    'Referer': 'https://m.weibo.cn/u/'  # 这个需要改成所要爬取用户主页的手机版本下的url
}
# /html/body/script[1]
# /html/body/script[1]

# context = ssl._create_unverified_context()

# yuanchuang  4669870622900757
# zhuanfa 4669870106477736
# kuanzhuan  4669812238457985
# pic_num=''global
# imgpost = 'https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154'
headers = {'Content-Type': 'application/json','Connection':'close'}


def getpiclast(idd):
    id = idd
    realurl = 'https://m.weibo.cn/status/%s' % id
    res = requests.get(realurl, headers=header,stream=True, verify=False)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)

    gameList = root.xpath("/html/body/script[2]/text()")

    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
        jpg = ''
        jpg2 = ''
        for j in list1:
            pprint(type(j))
            print(j)
            objson = json.loads(j)
            k = objson['status']
            t = 'retweeted_status'
            # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
            tupian = ""
            if t not in k:
                print("原创")
                pic = k['pic_ids']
                for lis in pic:
                    jpg = 'https://image.baidu.com/search/down?url=https://wx4.sinaimg.cn/large/' + lis + '.jpg'
                    print("TUPISN"+jpg)
                    zuhe = "<img src=\"" + jpg + "\" >"
                    tupian += zuhe
                    postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg}})
                    # repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    time.sleep(4)

                pic_num = k['pic_num']
                picww = pic_num
                # pprint(pic_num)


            else:
                print("转发")
                pic2 = k['retweeted_status']['pic_ids']
                for lis2 in pic2:
                    jpg2 = 'https://image.baidu.com/search/down?url=https://wx4.sinaimg.cn/large/' + lis2 + '.jpg'
                    print(jpg2)
                    zuhe = "<img src=\"" + jpg2 + "\" >"
                    tupian += zuhe
                    postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg2}})
                    # repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    time.sleep(4)

                pic_num2 = k['retweeted_status']['pic_num']
                picww = pic_num2
                # print(pic_num2)
            return tupian

        
        
        
def getpiclast2(idd):
    id = idd
    realurl = 'https://m.weibo.cn/status/%s' % id
    res = requests.get(realurl, headers=header,stream=True, verify=False)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)

    gameList = root.xpath("/html/body/script[2]/text()")

    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
        jpg = ''
        jpg2 = ''
        for j in list1:
            pprint(type(j))
            print(j)
            objson = json.loads(j)
            k = objson['status']
            t = 'retweeted_status'
            # 2022年3月份替换模板消息发送渠道，为了拼接图片。故作出如下更改
            tupian = ""
            tupian88 = []
            if t not in k:
                print("原创")
                pic = k['pic_ids']
                for lis in pic:
                    jpg = 'https://image.baidu.com/search/down?url=https://wx4.sinaimg.cn/large/' + lis + '.jpg'
                    print(jpg)
                    tupian88.append(jpg)
                    zuhe = "<img src=\"" + jpg + "\" >"
                    tupian += zuhe
                    postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg}})
                    # repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    time.sleep(4)

                pic_num = k['pic_num']
                picww = pic_num
                # pprint(pic_num)


            else:
                print("转发")
                pic2 = k['retweeted_status']['pic_ids']
                for lis2 in pic2:
                    jpg2 = 'https://image.baidu.com/search/down?url=https://wx4.sinaimg.cn/large/' + lis2 + '.jpg'
                    print(jpg2)
                    tupian88.append(jpg2)
                    zuhe = "<img src=\"" + jpg2 + "\" >"
                    tupian += zuhe
                    postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg2}})
                    # repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    time.sleep(4)

                pic_num2 = k['retweeted_status']['pic_num']
                picww = pic_num2
                # print(pic_num2)
            return tupian88        
        
        
def mun(idd):
    id = idd
    realurl = 'https://m.weibo.cn/status/%s' % id
    res = requests.get(realurl, headers=header,stream=True, verify=False)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)

    gameList = root.xpath("/html/body/script[2]/text()")

    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
        for j in list1:
            # pprint(type(j))
            # print(j)
            objson = json.loads(j)
            k = objson['status']
            t = 'retweeted_status'
            if t not in k:
                # print("原创")
                pic = k['pic_ids']
                for lis in pic:
                    jpg = 'https://image.baidu.com/search/down?url=https://wx4.sinaimg.cn/large/' + lis + '.jpg'
                    # print(jpg)

                pic_num = k['pic_num']
                # print(pic_num)
                return pic_num
                # return pic_num
                # picww=pic_num
                # pprint(pic_num)


            else:
                # print("转发")
                pic2 = k['retweeted_status']['pic_ids']
                for lis2 in pic2:
                    jpg2 = 'https://image.baidu.com/search/down?url=https://wx4.sinaimg.cn/large/' + lis2 + '.jpg'
                    # print(jpg2)

                pic_num2 = k['retweeted_status']['pic_num']
                return pic_num2

                # print(pic_num2)

                # print(pic_num2)



def isyuanchuang(idd):
    id = idd
    realurl = 'https://m.weibo.cn/status/%s' % id
    res = requests.get(realurl, headers=header,stream=True, verify=False)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)

    gameList = root.xpath("/html/body/script[2]/text()")

    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
        for j in list1:
            # pprint(type(j))
            # print(j)
            objson = json.loads(j)
            k = objson['status']
            t = 'retweeted_status'
            if t not in k:
                # print("原创")
                s='原创'
                return s



            else:
                # print("转发")
                b='转发'
                return b

            
            
            
            
            
            
    
    
    
    
def iphonepushdeer(fasname,idd):
    # https://m.weibo.cn/status/4806281305784430
    # ![](https://wx4.sinaimg.cn/large/006d5LOagy1h5ejyra00lj31o02801kx.jpg)
    # print(getpiclast(4806281305784430))
    fasname=fasname
    idd=idd
    ttt = getpiclast2(idd)
    tpp4 = ''
    for pt in ttt:
        tpp1 = '![]('
        tpp2 = ')'
        tpp3 = tpp1 + pt + tpp2
        tpp4 += tpp3


    
    pushkey = os.environ["pushkey"]
    pushdeer = PushDeer(pushkey=pushkey)
    
    print(tpp4)
    if tpp4=='':
        print("无图片")
        return
    else:
        pushdeer.send_markdown(fasname, desp=tpp4)
        print("推送到iPhonepushdeer成功！")
   
