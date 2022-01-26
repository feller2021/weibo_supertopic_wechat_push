#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 微博
# Desc      : 微博主模块

import requests, json, sys
import getpic
import content
import htmljiexi
from urllib.parse import quote
import urlencode
import tosuperid


class weiboMonitor():
    def __init__(self, ):
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://passport.weibo.cn/signin/login',
            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        aa=tosuperid.findsupid('吴安琪')
        bb = tosuperid.findsupid('张倩霏')
        cc = tosuperid.findsupid('朱苓')
        dd = tosuperid.findsupid('黄楚茵')
        ee = tosuperid.findsupid('吴羽霏')
        ff = tosuperid.findsupid('梁婉琳')

        self.uid = [aa, bb,cc,dd,ee,ff]

    # 获取访问连接
    def getweiboInfo(self):
        self.itemIds = []

        self.weiboInfo = []

        for i in self.uid:

            # userInfo = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % (i)
            # userInfo = 'https://m.weibo.cn/api/container/getIndex?containerid=231522type%s&page_type=searchall' % (i)
            userInfo = 'https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&containerid=%s_-_sort_time' % (
                i)
            res = requests.get(userInfo, headers=self.reqHeaders)
            d = res.json()['data']['cards']
            # print(d)
            for j in d:
                df = j['card_type']
                # print(df)
                if int(df) == 11:
                    try:
                        dfd = j['card_group']
                        # print(type(dfd))
                        with open('wbIds.txt', 'a') as f:
                            for x in dfd:
                                kl = x['card_type']
                                print(kl)
                                if int(kl) == 9:
                                    mblog = x['mblog']['id']
                                    print(mblog)

                                    f.write(x['mblog']['id'] + '\n')
                                    self.itemIds.append(x['mblog']['id'])
                            print('Info', '微博数目获取成功')
                            print('Info', '目前有 %s 条微博' % len(self.itemIds))

                    except:
                        print('error')

                        # sys.exit()

                    # if j['card_type'] == 11:
                    #     try:
                    #         df = j['card_group'][1]
                    #         print(df)
                    #     except:
                    #         print("45454")

                    # if j['card_type'] == 11:

    # 开始监控
    def startmonitor(self, ):
        returnDict = {}  # 获取微博相关内容，编辑为邮件
        itemIds = []
        with open('wbIds.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                itemIds.append(line)
        for i in self.uid:

            # userInfo = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % (i)
            userInfo = 'https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&containerid=%s_-_sort_time' % (
                i)
            res = requests.get(userInfo, headers=self.reqHeaders)
            # testt=res.text
            d = res.json()['data']['cards']
            for j in d:
                df = j['card_type']
                # print(df)
                if int(df) == 11:
                    try:
                        dfd = j['card_group']
                        # print(type(dfd))
                        for x in dfd:
                            kl = x['card_type']
                            # print(kl)
                            if int(kl) == 9:
                                mblog = x['mblog']['id']
                                # print(mblog)
                                if str(x['mblog']['id']) not in itemIds:
                                    with open('wbIds.txt', 'a') as f:
                                        f.write(x['mblog']['id'] + '\n')
                                        idd = str(x['mblog']['id'])
                                        # print('idd is' + idd)
                                        txt = x

                                        createtime = x['mblog']['created_at']

                                        sourcel = x['mblog']['source']

                                        fasname = x['mblog']['user']['screen_name']

                                        try:
                                            deit = x['mblog']['edit_config']['edited']

                                        except:
                                            deit = False

                                        reposts = x['mblog']['reposts_count']

                                        attitudes = x['mblog']['attitudes_count']

                                        comments = x['mblog']['comments_count']

                                        picnum = x['mblog']['pic_num']

                                        content.wbcontent(txt, createtime, sourcel, fasname, deit, reposts, attitudes,
                                                          comments,
                                                          idd)
                                        # 以下输出微博图片
                                        htmljiexi.getpiclast(idd)





                    except:
                        print('Error')


if __name__ == '__main__':
    w = weiboMonitor()
    # w.getweiboInfo()
    with open('wbIds.txt', 'r') as f:
        text = f.read()
        if text == '':
            w.getweiboInfo()
    newWB = w.startmonitor()
