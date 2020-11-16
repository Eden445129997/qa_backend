#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# http每一个请求的类
# from django.http.request import HttpRequest

# 笛卡尔积:Cartesian
cartesian = itertools.product('房管普', '房管庄')

for i in cartesian:
    print(i)


first = True
second = '1    2    d '

first = ('%s'%first).strip()

print(len(first))
print(len(second))

print(27059+4606)

weilidai = 32000
meituan = 2168.43+1849.41+4008+500.25
zhifubao = 3186.17 + 5757.83
jingdong = 3616.17 + 3100 + 4600

print("美团：%s"%(meituan))
print("支付宝：%s"%zhifubao)
print("京东：%s"%jingdong)

print(2000+4606+2000)

print(meituan+zhifubao+jingdong)
