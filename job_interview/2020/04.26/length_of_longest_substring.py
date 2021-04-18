#-*- coding: utf-8 -*-
#最长无重复字符的子串
def lengthOfLongestSubstring(s):
    dic_letter={}
    i = -1 #若i==0，s为''的时候，结果是0
    longest_length = 0
    for j,letter in enumerate(s):
        if letter in dic_letter:
            i = max(dic_letter[letter],i)
        dic_letter[letter] = j
        longest_length = max(longest_length, j - i)
    #print(dic_letter)
    return longest_length

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('bbbb'))
    print(lengthOfLongestSubstring('pwwkew'))
    print(lengthOfLongestSubstring('dvdf'))
    print(lengthOfLongestSubstring(''))