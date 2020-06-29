#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1.暴力法
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        '''

        # 2. 两次遍历
        """
        hash_map = {}
            '''
            enumerate() 函数用于将一个可遍历的数据对象组合为一个索引序列
            同时列出数据下标（start=0）和数据，一般用在 for 循环当中。
            '''
        for k, v in enumerate(nums):
            # 用字典来实现hash table
            hash_map[v] = k

        for k, v in enumerate(nums):
            '''
                dict.get(key, default=None)
                返回指定键的值，如果值不在字典中返回default值
            '''
            j = hash_map.get(target-nums[k])
            if j is not None and j != k:
                return [k, j]
        """
        # 3. 一次遍历，最优
        '''
        hash_map = {}
        
        for k, v in enumerate(nums):
            # 判断另一个数是否在hash_map中，如果在，返回
            if target-v in hash_map:
                return [hash_map[target-v],k]
            # 不在hash_map中，添加到hash_map中
            else:
                hash_map[v] = k
        '''

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # hashmap = {}
        # for k, v in enumerate(nums):
        #     hash_map[v] = k

        # for k, v in enumerate(nums):
        #     index = hash_map[target-v]

        #     if index is not None and index!=k:
        #         return [k, index]

        # hash_map = {}
        # for k, v in enumerate(nums):
        #     if target-v in hash_map:
        #         return [hash_map[target-v], k]

        #     else:
        #         hash_map[v] = k

            
    
