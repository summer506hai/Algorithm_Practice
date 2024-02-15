# -*— coding:utf-8 --*
'''
小明有n块木板，第i块目标的长度为 ai
小明买了一块长度为m的木料，这块木料可以切割成任意块，拼接到已有的木板上，用来加长木板。
小明想让最短的木板尽量长。
请问小明加长木板后，最短木板的长度最大可以为多少
'''

def dunamic_cal(arr,mlength):
    '''

    :param arr:  n块木板长度list
    :param length:长度为m的木料的长度
    对排序后的木材进行遍历，当遍历到第二根的时候，如果，第二比第一长，第一根加一截，木材m的长队length减一
    :return:
    '''
    for _ in range(mlength):
        for i in range(len(arr)):
            if (i + 1) < len(arr) and arr[i] + 1 > arr[i+1]:
                continue
            arr[i] = arr[i] + 1
            break
    return arr


def test():
    arr_result = dunamic_cal(sorted([4,5,3,5,5]),3)
    assert arr_result[0] == 5
    arr_result = dunamic_cal(sorted([4,5,3,5,5]),2)
    assert arr_result[0] == 4


if __name__ == "__main__":
    # test()
    arr_length = int(input())
    m_length = int(input())
    arr_list = list(map(int,input().split()))
    arr = dunamic_cal(sorted(arr_list),m_length)
    print(arr[0])
