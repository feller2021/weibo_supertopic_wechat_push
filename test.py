#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 微博
# Desc      : 微博主模块
import time
import traceback
import requests, json, sys
import getpic
import content
import htmljiexi
from urllib.parse import quote
import urlencode
import tosuperid
requests.packages.urllib3.disable_warnings()

class weiboMonitor():
    def __init__(self, ):
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://passport.weibo.cn/signin/login',
            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        # akb48teamsh等成员1
        aa=tosuperid.findsupid('吴安琪')
        bb = tosuperid.findsupid('张倩霏')
        cc = tosuperid.findsupid('朱苓')
        # gnz48等成员1
        dd = tosuperid.findsupid('黄楚茵')
        ee = tosuperid.findsupid('吴羽霏')
        ff = tosuperid.findsupid('梁婉琳')
        # bej48等成员1
        gg = tosuperid.findsupid('唐晨葳')
        hh = tosuperid.findsupid('王若诗蓝')
        ii = tosuperid.findsupid('张梦慧')
        # gnz48等成员2
        jj = tosuperid.findsupid('杨若惜')
        kk = tosuperid.findsupid('刘力菲')
        ll = tosuperid.findsupid('龙亦瑞')
        mm = tosuperid.findsupid('罗可嘉')
        nn = tosuperid.findsupid('方琪')
        # snh48等成员
        oo = tosuperid.findsupid('苏杉杉')
        pp = tosuperid.findsupid('费沁源')
        qq = tosuperid.findsupid('姜杉')

        self.uid = [aa, bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn]
        print("---总共要循环的人---")
        print(self.uid)
        print("---总共要循环的人---")

    # 获取访问连接

    def getweiboInfo(self):
        print("# 获取访问连接")
        self.itemIds = []

        self.weiboInfo = []

        for i in self.uid:
            time.sleep(6)

            # userInfo = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % (i)
            # userInfo = 'https://m.weibo.cn/api/container/getIndex?containerid=231522type%s&page_type=searchall' % (i)
            userInfo = 'https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&containerid=%s_-_sort_time' % (
                i)
            print("i的值是："+i)
            print("第 "+i+"---uid开始获取数据")
            res = requests.get(userInfo, headers=self.reqHeaders,stream=True, verify=False)
            d = res.json()['data']['cards']
            # print(d)
            for j in d:

                df = j['card_type']
                # print(df)
                if int(df) == 11:
                    try:
                        print(j)
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

                        print(traceback.format_exc())
                        pass
                        # print('error')

                        # sys.exit()
                else:
                    try:
                        print(j)

                        with open('wbIds.txt', 'a') as f:
                            for x in j['card_type']:

                                kl = x

                                print(kl)
                                if int(kl) == 9:
                                    mblog = j['mblog']['id']
                                    print(mblog)

                                    f.write(j['mblog']['id'] + '\n')
                                    self.itemIds.append(j['mblog']['id'])
                            print('Info', 'card_type不等于11时，微博数目获取成功')
                            print('Info', 'card_type不等于11时，目前有 %s 条微博' % len(self.itemIds))

                    except:

                        print(traceback.format_exc())
                        pass

                    # if j['card_type'] == 11:
                    #     try:
                    #         df = j['card_group'][1]
                    #         print(df)
                    #     except:
                    #         print("45454")

                    # if j['card_type'] == 11:

    # 开始监控

    def startmonitor(self, ):
        print("# 开始监控")
        returnDict = {}  # 获取微博相关内容
        itemIds = []
        with open('wbIds.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                itemIds.append(line)
        for i in self.uid:
            time.sleep(6)

            # userInfo = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % (i)
            userInfo = 'https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&containerid=%s_-_sort_time' % (
                i)
            res = requests.get(userInfo, headers=self.reqHeaders,stream=True, verify=False)
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
                                        print("最新的是id："+str(x['mblog']['id']))
                                        dayin="https://m.weibo.cn/status/"
                                        print("最新的微博链接是："+dayin+str(x['mblog']['id']))
                                        txt = x

                                        createtime = x['mblog']['created_at']

                                        sourcel = x['mblog']['source']

                                        fasname = x['mblog']['user']['screen_name']
                                        # 推送到iPhonepushdeer
                                        htmljiexi.iphonepushdeer(fasname,idd)

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

                        print(traceback.format_exc())
                        pass
                        print("没有更新")
                        # print('Error')


if __name__ == '__main__':
    w = weiboMonitor()
    # w.getweiboInfo()
    with open('wbIds.txt', 'r') as f:
        text = f.read()
        if text == '':
            w.getweiboInfo()
    newWB = w.startmonitor()
