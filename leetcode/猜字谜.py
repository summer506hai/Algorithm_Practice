# -*— coding:utf-8 --*
'''
输入谜面和谜底
谜面单词列表，以 , 分割
谜底单词列表，以 , 分割
输出： 匹配到 正确单词列表，以 , 分割，匹配不到 返回  not found
1、变换顺序后 一样 2、字母去重后一样 —— 算匹配上
示例：
输入 
conection
connection,today
输出：
connection
输入：
bdni,wood
bind,wrong,wood
输出：
bind,wood

'''

def remove_duplicates(question, answer):
    q = list(set(question))
    a = list(set(answer))
    if q == a:
        return True
    return False

def change(question,answer):
    q = sorted(list(set(question)))
    a = sorted(list(set(answer)))
    if q == a:
        return True
    return False

def guess_game():
    result_list = []
    questions = input().split(",")
    answers = input().split(",")
    for q in questions:
        flag = False
        for a in answers:
            if remove_duplicates(q,a) or change(q,a):
                result_list.append(a)
                flag = True
                break
        if not flag:
            result_list.append("not found")

    return ",".join(result_list)

if __name__ == "__main__":
    print(guess_game())
