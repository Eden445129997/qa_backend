#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apps.common.cache import LRUCacheDict
from functools import wraps, lru_cache


def cache_it(max_size=1024, expiration=60):
    """缓存装饰器"""
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)
    def outter_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result
        return inner_wrapper
    return outter_wrapper

def print_clazz(clazz):
    """打印类装饰器"""
    def outter_wrapper(*args, **kwargs):
        print("进入clazz：",clazz)
        return clazz(*args, **kwargs)
    return outter_wrapper

def print_func(func):
    """打印方法装饰器"""
    def outter_wrapper(*args, **kwargs):
        print("进入func：",func)
        return func(*args, **kwargs)
    return outter_wrapper

def print_model_and_data(func):
    """打印入参列表数据 装饰器"""

    def outter_wrapper(*args, **kwargs):
        print("*" * 200)
        suit: list or tuple = args[1]
        for case_group in suit:
            print("* 场景分组  ：", case_group)
            print("* 数据类型  ：", type(case_group))
            for i in range(len(case_group)):
                print("* 数据内容 %s:" % i, case_group[i])
            print("*" * 200)
        return func(*args, **kwargs)

    return outter_wrapper