## 解题思路
- 创建inc数组用来记录增量操作
## 代码
```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.cnt = 0
        self.maxSize = maxSize
        self.inc = []
        self.st = []


    def push(self, x: int) -> None:
        if self.cnt < self.maxSize:
            self.st.append(x)
            self.cnt = self.cnt + 1
            self.inc.append(0)


    def pop(self) -> int:
        if self.cnt == 0:
            return -1
        self.cnt -= 1
        if self.cnt >= 1:
            self.inc[-2] += self.inc[-1]
        return self.st.pop() + self.inc.pop()


    def increment(self, k: int, val: int) -> None:
        if self.cnt:
            self.inc[min(k,self.cnt)-1] += val
            #print(self.inc)


if __name__ == '__main__':
    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)
    obj.pop()
    obj.push(2)
    obj.push(3)
    obj.push(4)

    obj.increment(5, 100)
    obj.increment(2, 100)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
```
## 算法复杂度
时间负责度 O(1)