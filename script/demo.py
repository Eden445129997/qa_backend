#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# 笛卡尔积:Cartesian
cartesian = itertools.product('房管普', '房管庄')

for i in cartesian:
    print(i)


first = True
second = '1    2    d '

first = ('%s'%first).strip()

print(len(first))
print(len(second))
