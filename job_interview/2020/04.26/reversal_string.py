#-*- coding: utf-8 -*-
#给定一个字符串，逐个翻转字符串中的每个单词
def reversal_string(s):
    return " ".join(reversed(s.split(' ')))

if __name__ == '__main__':
    print(reversal_string('the sky is blue'))