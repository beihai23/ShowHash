#!/usr/bin/python
# vim: set fileencoding=utf8

import Hash
import struct

# 哈希值在分布轴上显示的粒度，既多少个值显示成一个点
GRANULARITY            = 100
# 保存已经计算的hash值在值空间范围的分布情况
Distribution_container = [0 for i in range(0,101)]

def PrepareKey():
    '''产生并返回待测试的 key list'''
    return range(0, 1450000)

def CalculateHash():
    keylist  = PrepareKey()
    maxValue = Hash.MaxValue()

    processed = 0.0
    processing = 0.0
    total = len(keylist)
    for key in keylist:
        cur = processed * 100.0 / total
        if cur > processing:
            processing_str = '[%2d %%]' % processing
            print '\r',
            print processing_str,
        processing = cur
        if isinstance(key, int) or isinstance(key, long) :
            key = struct.pack('Q', key)
        value, valuestring = Hash.Sum(key)
        value_index = int(value * 100.0 / maxValue)
        try:
            Distribution_container[value_index] += 1
        except IndexError as e:
            print value_index, len(Distribution_container), e
        processed += 1

    print '\b'*100,
    print '[100 %] CalculateHash finished.'

def ShowHashDistribution():
    # 按粒度合并空间范围内的hash 值计数
    merge = lambda count : count / GRANULARITY + (1 if count % GRANULARITY > 0 else 0)
    merged_container = []
    x_level = 0
    for count in Distribution_container:
        dot_num = merge(count)
        merged_container.append(dot_num)
        if dot_num > x_level:
            x_level = dot_num

    # 输出数值空间的分布情况
    for i in range(x_level):
        for count in merged_container:
            if count - i > 0:
                print '\b*',
            else:
                print '\b ',
        print # break line

    #  打印代表值空间的横轴 print y axe
    for j in range(len(Distribution_container)):
        print '\b-',
    print '\b>'

if __name__=='__main__':
    CalculateHash()
    ShowHashDistribution()
