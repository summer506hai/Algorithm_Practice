# -*- coding: utf-8 -*-
'''
数组的中心位置 一个整数数组nums，计算数组的中心位置
数组的中心位置是数组的一个下标，其左侧的所有元素相乘的积等于右侧所有元素相乘的积
数组第一个元素的左侧积是1，最后一个元素的右侧积是1
如果数组有多个中心位置，应该返回最靠近左边的那一个，如果数组不存在中心位置，返回-1
'''
from functools import reduce

def calc_center_pos(nums):
    right = reduce(lambda x,y:x*y,nums,1) #数组的总乘积
    flag = False
    left = 1
    for i in range(len(nums)):
        if i != 0:
            left = left * nums[i-1]
        right = right/nums[i]
        if float(left) == float(right):
            flag = True
            return i
    if not flag:
        return -1

def test():
    assert calc_center_pos([2,5,3,6,5,6]) == 3
    print("测试通过！")

if __name__ == "__main__":
    # test()
    print(calc_center_pos(list(map(int,input().split()))))
