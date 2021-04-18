#-*- coding: utf-8 -*-
#判断给定的字符串是否是有效的括号对
def valid_brackets(str):
    dic_a = {'(':')','[':']','{':'}'}
    s=[]
    for i in str:
        if i in dic_a:
            s.append(i)
        elif i in dic_a.values():
            if len(s) == 0:
                return False
            if dic_a[s.pop()] != i:
                return False
    return len(s)== 0

if __name__ == '__main__':
    print(valid_brackets('()'))
    print(valid_brackets(')'))
    print(valid_brackets('){'))
    print(valid_brackets('()[[]]{}'))