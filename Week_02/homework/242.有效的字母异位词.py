#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #第一遍
        """
        # 1. 排序法
        '''
            sort & sorted的区别
            1. sort应用于list，sorted应用于所有的可迭代对象
            2. sort在原有的list上进行操作，sorted在返回一个新的list
        '''
        return sorted(s) == sorted(t)
        """
        '''
        # 2. 哈希表法

        if len(s) != len(t):
            return False
        
        count = {}
        #对原来的字符串字母进行计数
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        #判断两个str元素是否相等
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False

        for value in count.values():
            if value != 0:
                return False
        return True
        '''
        #第二遍
        # if len(s) == len(t):
        #     return sorted(s) == sorted(t)
        #     # if sorted(s) == sorted(t):
        #     #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
            else:
                return False

        for value in hashmap.values():
            if value != 0:
                return False
        return True
 


# @lc code=end

