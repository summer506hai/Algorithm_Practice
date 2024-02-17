# -*- coding: utf-8 -*-
'''
1、每成功上报一条日志，奖励1分
2、每条日志每延迟上报1秒，扣一分
3、积累日志达到100条，必须立刻上报
给出日志序列，根据该规则，计算首次上报能获得最多的积分数
输入描述 按时序产生的日志条数 T1 T2..Tn
输出描述 首次上报最多能获得的积分数
示例 输入  1 98 1 输出 98 输入 50 60 1 输出 50
1 2 97
1
1+2-1
1+2+97-2*1-1*2 = 96
'''

log_list = input().split()
pre,total,now,max_value = 0,0,0,0   #total是总和
for l in log_list:
    log_num = int(l)
    pre = total
    total = total + log_num
    if total >= 100:
        total = 100
        now = now + pre
        break
    now = now + pre
    max_value = max(max_value,total-now)
max_value = max(max_value,total-now)
print(max_value)
