class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 记录p, s字母个数
        p_count = [0] * 26
        s_count = [0] * 26
        res = []
        for a in p:
            p_count[ord(a) - 97] += 1
        left = 0
        for right in range(len(s)):
            # print(p_count, s_count)
            if right < len(p) - 1:
                s_count[ord(s[right]) - 97] += 1
                continue
            # 窗口加一个， 减一个，维护长度为len(p)的长度
            s_count[ord(s[right]) - 97] += 1
            if p_count == s_count:
                res.append(left)
            s_count[ord(s[left]) - 97] -= 1
            left += 1
        return res