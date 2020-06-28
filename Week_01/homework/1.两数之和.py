#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            从hash表中查找index
        '''
        # 1.建立hash表，键是源数组的值，值是源数组的键
        hashmap = {}
        for key,value in enumerate(nums):
            hashmap[value] = key

        # 2.进行对比，然后返回index
        for i,v in enumerate(nums):
            j = hashmap.get(target-v)

            if i!=j and j is not None:
                return [i,j]



