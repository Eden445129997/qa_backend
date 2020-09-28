#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from collections import OrderedDict

class LRUCacheDict(object):
    """
    LRU（最近最少使用）算法实现的缓存字典
    """

    def __init__(self, max_size=1024, expiration=60):
        """
        最大容量为1024个key，每个key的有效期是60s
        """
        self.max_size = max_size
        self.expiration = expiration

        self._cache = {}
        # 记录访问时间
        self._access_records = OrderedDict()
        # 记录失效时间
        self._expire_records = OrderedDict()

    def __setitem__(self, key, value):
        now = int(time.time())
        self.__delete__(key=key)

        self._cache[key] = value
        self._expire_records[key] = now + self.expiration
        self._access_records[key] = now

        self.cleanup()

    def __getitem__(self, key):
        now = int(time.time())
        del self._access_records[key]
        self._access_records[key] = now
        self.cleanup()

        return self._cache[key]

    def __contains__(self, key):
        self.cleanup()
        return key in self._cache

    def __delete__(self, key):
        if key in self._cache:
            del self._cache[key]
            del self._expire_records[key]
            del self._access_records[key]

    def cleanup(self):
        """
        去掉无效（过期或者超出存储大小）的缓存
        :return:
        """
        if self.expiration is None:
            return None

        pending_delete_keys = []
        now = int(time.time())
        # 删除已过期的缓存
        for k, v in self._expire_records.items():
            if v < now:
                pending_delete_keys.append(k)

        for del_k in pending_delete_keys:
            self.__delete__(del_k)

        # 如果数据量大于max_size，则删掉最旧的缓存
        while (len(self._cache) > self.max_size):
            for k in self._access_records:
                self.__delete__(k)
                break


