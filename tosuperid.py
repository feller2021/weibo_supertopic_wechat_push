import time

import requests
from urllib.parse import urlencode
from urllib import parse


import urlencode
import re
import traceback

def findsupid(name):
    HEADERS = {'Content-Type': 'application/json','Connection':'close'}
    name=name
    # bm='=98&q='+name+'&t=0'
    bm=urlencode.urlencode(name)

    # url='https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D98%26q%3D%E5%BC%A0%E5%80%A9%E9%9C%8F%26t%3D0&page_type=searchall'
    url='https://m.weibo.cn/api/container/getIndex?containerid=100103type'+bm+'&page_type=searchall'
    res=requests.get(url, headers=HEADERS,stream=True, verify=False)
    try:
        res=res.json()['data']['cards'][0]['card_group'][0]['scheme']
    except:
        print(traceback.format_exc())
        time.sleep(3)
        pass
        print("空列表,再试一下begin")
        res=res.json()['data']['cards'][0]['card_group'][0]['scheme']
        print("空列表,再试一下end")
        time.sleep(3)



    t='https://m.weibo.cn/p/index?extparam=SNH48&containerid=1008086bd7cfe0bc1b396eede72d35bf433f4f&luicode=10000011&lfid=100103type%3D98%26q%3Dsnh48%26t%3D0'

    lsat=re.findall(r"containerid=(.+?)&luicode=", res)
    lsat = lsat[0]

    # print(type(lsat))
    return lsat

#循环60次
# for _ in range(60):
#     print(findsupid('苏杉杉'))
