# -*- coding: utf-8 -*-
'''
一个图像有n个像素点，存储在一个长度为n的数组img里，每个像素点的取值范围[0,255]的正整数
请你给图像每个像素点值加上一个整数K（可以是负数），得到新图 newimg，使得newimg的所有像素平均值最接近中位值128，请输出这个整数K
'''
def calculate_k(img_list):
    ans = 0
    t = float('inf')
    for i in range(-127,255):
        total_sum = 0
        for num in img_list:
            tmp = i + num
            if tmp < 0:
                tmp = 0
            elif tmp > 255:
                tmp = 255
            total_sum = total_sum + tmp

        if t > abs(128*len(img_list) - total_sum):
            ans = i
            t = abs(128*len(img_list) - total_sum)

    return ans

def test():
    assert calculate_k([0,0,255,255]) == 1
    assert calculate_k([0, 0, 0, 0]) == 128
    assert calculate_k([129, 130, 129, 130]) == -2

if __name__ == "__main__":
    test()
