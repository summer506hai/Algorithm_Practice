# -*- coding: utf-8 -*-
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

if __name__ == '__main__':
    print(bubble_sort([5,2,3,1]))
    print(bubble_sort([5,1,1,2,0,0]))