#-*- coding : utf-8 -*-
'''
字符的最短距离
遍历字符串，找到目标字母，用cIndices数组记下位置. 遍历字符串，将当前位置与cIndices数组的位置进行相减，取最小值
'''
def shortestToChar(S, C):
    cIndices = []
    res = []
    for i,x in enumerate(S):
        if x == C:
            cIndices.append(i)
    for i,x in enumerate(S):
        r = float('inf')
        for j,y in enumerate(cIndices):
            r = min(r,abs(i - y))
        res.append(r)
    return res

print(shortestToChar("loveleetcode","e"))