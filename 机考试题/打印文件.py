# -*— coding:utf-8 --*
'''
题目描述：有5台打印机打印文件，每台打印机有自己的打印队列，队列中的文件有 1-10 不同的优先级，数字越大优先级越高。打印机会从自己的待打印队列中选择优
先级最高的文件打印。如果存在优先级一样的文件，则选择最早进入队列的文件
输入描述：每个输入包含1个测试用例，每个测试用例第一行给出发生事件的数量 N
接下来又N行，分别表示发生的事件
共又如下两种事件
1 IN P NUM 表示有一个优先级为 NUM的文件放到了打印机P的待打印队列中
2 OUT P 表示打印机P 进行了一次文件打印，同时该文件从待打印队列中取出
输出 对于每个测试用例，每次 OUT P事件，请在一行中输出文件的编号，如果此时没有文件可以打印，输出null
文件的编号为，IN P NUM发生的第几次，编号就是几

解题思路：operate_dict为dict，key为打印机P，value也为一个dict，该dict的key是文件编号，value是优先级
IN存放，OUT排序后去数据
'''
# 定义排序函数
def custom_sort(item):
    return (-item[1], item[0])

def print_file(operates):
    flag = 0
    operate_dict = {}
    result_list = []
    for each_operate in operates:
        eo = each_operate.split(" ")
        if "IN" in eo[0]:
            flag = flag + 1
            if eo[1] in operate_dict.keys():
                operate_dict[eo[1]][str(flag)] = int(eo[2])
            else:
                operate_dict[eo[1]] = {}
                operate_dict[eo[1]][str(flag)] = int(eo[2])   #{'1': {'1': 1, '2': 3, '3': 1, '4': 3}}
        elif "OUT" in eo[0]:
            if eo[1] in operate_dict.keys() and len(operate_dict[eo[1]]) > 0:
                out_content = operate_dict[eo[1]]
                out_content_sort = sorted(out_content.items(), key=custom_sort) #排序
                result_list.append(out_content_sort[0][0])
                # 将排序后的项重新构建成字典
                sorted_dict = {k: v for k, v in out_content_sort[1:]} #排序后去掉第一个
                operate_dict[eo[1]] = sorted_dict
            else:
                result_list.append("NULL")
    return result_list

def test():
    assert print_file(["IN 1 1","IN 1 3","IN 1 1","IN 1 3","OUT 1"]) == ['2']
    assert print_file(["IN 1 1", "IN 1 2", "IN 1 3", "IN 2 1", "OUT 1", "OUT 2", "OUT 2"]) == ['3', '4', 'NULL']


if __name__ == "__main__":
    # test()
    n = int(input()) #操作的个数
    operates_list = []
    for k in range(n):
        operates_list.append(input())

    result = print_file(operates_list)
    for r in result:
        print(r)


