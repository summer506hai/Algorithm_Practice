# -*— coding:utf-8 --*
'''
给定一个字符串S，s包含以空格分割的若干个单词，请对S进行如下处理后输出
1、单词内部调整：对每个单词字母重新按字典序排序
2、单词间顺序调整
1）统计每个单词出现的次数，并按次数降序排列
2）次数相同时，按单词长度升序排序
3）次数和单词长度均相同时，按字典序升序排序
'''
from collections import Counter

def sorted_word_by_lexico(words):
    word_list = words.split(" ")
    new_word_list = []
    for w in word_list:
        new_word_list.append(''.join(sorted(w)))
    return new_word_list

def sorted_str_in_word(words_list):
    # word_count = Counter(words_list) #单词出现次数 Counter统计了列表中每个单词出现的次数 得到的是字典，会导致最后结果是去重的
    # sorted_words = sorted(word_count.items(),key=lambda x: x[1], reverse=True)
    # sorted_words_list_by_count = [word for word, count in sorted_words] #转成单词的list
    # sorted_words_by_len = sorted(sorted_words_list_by_count,key=lambda x: len(x)) #按单词长度排序
    # resorted = sorted(sorted_words_by_len)#按字典序排序
    # return " ".join(resorted)
    # sorted_words = sorted(word_count.items(), key=lambda x: (-x[1],len(x[0]),x[0]))
    sorted_words = sorted(words_list, key=lambda x: (-words_list.count(x), len(x), x))
    return " ".join(sorted_words)


def resort_words(words):
    return sorted_str_in_word(sorted_word_by_lexico(words))

def test():
    assert resort_words("This is an apple") == "an is This aelpp"
    assert resort_words("My sister is in the house not in the yard") == "in in eht eht My is not adry ehosu eirsst"


if __name__ == "__main__":
    # test()
    user_input = input("请输入内容：")  # 获取用户输入
    print(resort_words(user_input))
