# -*-coding-*- : utf-8
'''
夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
'''
def maxIceCream(costs, coins) -> int:
    costs = sorted(costs)
    all_costs=0
    count = 0
    for c in costs:
        all_costs = all_costs + c
        if all_costs <= coins:
            count = count+1
            continue
        else:
            return count
    return count

if __name__ == '__main__':
    print(maxIceCream([1, 3, 2, 4, 1], 7))
    print(maxIceCream([10, 6, 8, 7, 7, 8], 5))
    print(maxIceCream([1, 6, 3, 1, 2, 5], 20))



