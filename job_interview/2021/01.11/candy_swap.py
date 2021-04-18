# -*- coding: utf-8 -*-

def fairCandySwap(x,y):
    total_a = sum(x)
    total_b = sum(y)
    diff_candy = (total_a - total_b) / 2
    sorted(x)
    sorted(y)
    i = 0
    j = 0
    while x[i] - y[j] != diff_candy:
        if x[i] - y[j] > diff_candy:
            j += 1
        else:
            i += 1
    return [x[i] , y[j]]

def fairCandySwap_use_dic(x,y):
    total_a = sum(x)
    total_b = sum(y)
    diff_candy = (total_a - total_b) / 2
    dict_candy_a = {}
    for i in x:
        dict_candy_a[i] = 0
    for j in y:
        if (j + diff_candy) in dict_candy_a.keys():
            return [int(j + diff_candy),j]

if __name__ == '__main__':
    print(fairCandySwap([1,2,5],[2,4]))
    print(fairCandySwap([1,1],[2,2]))
    print(fairCandySwap([1,2],[2,3]))
    print(fairCandySwap([2],[1,3]))
    print(fairCandySwap([1,3,5,8],[3,5,2,9]))
    print(fairCandySwap_use_dic([1,2,5],[2,4]))
    print(fairCandySwap_use_dic([1,1],[2,2]))
    print(fairCandySwap_use_dic([1,2],[2,3]))
    print(fairCandySwap_use_dic([2],[1,3]))
    print(fairCandySwap_use_dic([1,3,5,8],[3,5,2,9]))
