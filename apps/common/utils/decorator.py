#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_clazz(clazz):
    def outter_wrapper(*args, **kwargs):
        print("进入clazz：",clazz)
        return clazz(*args, **kwargs)
    return outter_wrapper

def print_func(func):
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