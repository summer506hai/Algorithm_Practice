#-*- coding: utf-8 -*-
#返回字符串str2在str1中第一次出现的位置，若找不到则返回-1

def findstr(str1,str2):
    l1 = str1.find(str2)
    return l1

def find_str(str1,str2):
    if len(str2) > len(str1):
        return -1
    for i in range(len(str1)):
        j = 0
        if str1[i] != str2[j]:
            continue
        while (i + j )< len(str1) and (j) < len(str2) :
            #print(i,j)
            if str1[i+j] != str2[j]:
                break
            j += 1
        if j == len(str2):
            return i
    return -1

if __name__ == '__main__':
    print(findstr("fgdabcefg","abc"))
    print(find_str("fgdabcefg","abc"))
    print(findstr("fgdacefg", "abc"))
    print(find_str("fgdacefg", "abc"))
    print(find_str("a", "abc"))
    print(findstr("a", "abc"))
    print(find_str("abc", "abc"))
    print(findstr("abc", "abc"))