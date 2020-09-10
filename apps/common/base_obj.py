#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BaseHandler(object):
    """责任链模式基类"""
    def set_successor(self, successor):
        self.successor = successor