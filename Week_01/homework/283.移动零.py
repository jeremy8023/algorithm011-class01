#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
		j = 0
		for i in range(len(nums)):
			# 当前元素!=0，就把其交换到左边，等于0的交换到右边
			if nums[i]:
				nums[j],nums[i] = nums[i],nums[j]
				j += 1



# @lc code=end

