# -*- coding: utf-8 -*-
#sentence 包含英语字母表中每个字母至少一次。

def checkIfPangram_01(sentence):
    # 先去重
    dict_letter={}
    ss=""
    for i in sentence:
        if i in dict_letter.keys():
            continue
        else:
            dict_letter[i] = 1
            ss = ss + i
    if len(ss) == 26:
        return True
    else:
        return False

def checkIfPangram_02(sentence):
    ss=[]
    for i in sentence:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            if i not in ss:
                ss.append(i)
    if len(ss) == 26:
        return True
    else:
        return False

if __name__ == '__main__':
    print(checkIfPangram_01("thequickbrownfoxjumpsoverthelazydog"))
    print(checkIfPangram_01("leetcode"))
    print(checkIfPangram_02("thequickbrownfoxjumpsoverthelazydog"))
    print(checkIfPangram_02("leetcode"))

