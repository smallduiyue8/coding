"""
# Author: wangyue 
# Date: 2020/8/8 
# Description: 

"""
def bubbleSort(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums