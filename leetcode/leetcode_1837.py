#-*- coding : utf-8 -*-
'''
给你一个整数 n（10 进制）和一个基数 k ，请你将 n 从 10 进制表示转换为 k 进制表示，计算并返回转换后各位数字的 总和 。
转换后，各位数字应当视作是 10 进制数字，且它们的总和也应当按 10 进制表示返回。
'''
def sumBase(n, k):
    y = 0
    while n/k != 0:
        print(n/k)
        n,x = int(n/k),int(n%k)
        y = y + x
    return y

if __name__ == '__main__':
    print(sumBase(34,6))
    #print(sumBase(10, 10))
