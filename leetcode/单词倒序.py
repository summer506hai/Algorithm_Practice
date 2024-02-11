# -*— coding:utf-8 --*
'''
输入单行英文句子，里面包含英文字母 空格 以及 ,.?三种标点符号，请将句子内每个单词进行倒序，并输出倒序后的语句
'''

def reverse_words(sentence):
    current_word = ""
    result = ""
    for char in sentence:
        if char in [",",".","?"," "]:
            if current_word:
                result = result + current_word[::-1] + char
                current_word = ""
            else:
                current_word = current_word + char
        else:
            current_word = current_word + char

    if current_word: #处理最后一个单词
        result = result + current_word[::-1]

    return result

def test():
    sentence = input("请输入句子：")
    reversed_sentence = reverse_words(sentence)
    print("逆序后的句子：", reversed_sentence)

if __name__ == "__main__":
    test()
