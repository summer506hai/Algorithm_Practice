## 题目描述
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
## 解题思路
- 用栈
- 非 ']' 入栈操作
- 若遇到数字，则将 reStr * 数字（次数）
- '[' 出栈
## 代码
```python
#-*- coding : utf-8 -*-
'''
字符串解码
输入：s = "3[a2[c]]"
输出："accaccacc"
'''
def decodeString(s):
    stack = []
    for i in s:
        if i == ']':
            reStr = ''
            reCount = ''
            while stack and stack[-1] != '[':
                reStr = stack.pop() + reStr

            stack.pop()

            while stack and stack[-1].isnumeric():
                reCount = stack.pop() + reCount

            stack.append(reStr*int(reCount))


        else:
            stack.append(i)

    return "".join(stack)

if __name__ == '__main__':
    print(decodeString("3[a2[c]]"))

```
## 算法复杂度
- 时间复杂度 O(N)
- 空间复杂度 O(N)
