# -*— coding:utf-8 --*
'''
输入描述：
第一行输入 newspaper内容 ，包括 1-N个字符串，用空格分开
第二行输入 anonymousLetter内容，包括 1-N个字符串，用空格分开
1、newspaper内容和anonymousLetter内容的字符串由小写英文字母组成且每个字母只能使用一次
2、newspaper内容中的每个字符串字母顺序可以任意调整，但必须保证字符串的完整性（每个字符串不能由多余字母）
3、1<N<100,1<newspaper.length< anonymousLetter.length<=104
输出描述：如果报纸可以拼成匿名信返回true，否则返回false
示例
输入 
ab cd
ab
输出 true
输入 
ab ef
aef
输出 false
输入 
ab bcd ef
cbd fe
输出 true
输入 
ab bcd ef
cd fe
输出 false
'''

def splicing(newspaper,anonymous_letter):
    n = sorted(list(newspaper))
    a = sorted(list(anonymous_letter))
    n_after = "".join(n)
    a_after = "".join(a)
    if a_after == n_after:
       return True
    return False

if __name__ == "__main__":
    newspaper = input().split(" ")
    anonymous_letter = input().split(" ")
    for item in anonymous_letter:
        flag = False
        for item2 in newspaper:
            if splicing(item2, item):
                flag = True
                break
        if not flag:
            print(False)
            exit(0)
    print(True)
