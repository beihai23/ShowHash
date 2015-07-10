#!/usr/bin/python
# vim: set fileencoding=utf8

import hashlib

def MaxValue():
    '''返回整数表示的hash算法的最大取值'''
    return 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

def Sum(key):
    '''计算 hash 并返回大整数表示的 hash 值'''
    m = hashlib.md5()
    m.update(key)
    hashvalue = m.hexdigest()

    return eval("0x"+hashvalue), hashvalue
