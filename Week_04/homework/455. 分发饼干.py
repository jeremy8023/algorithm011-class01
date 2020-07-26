class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ## 先排序
        g = sorted(g)
        s = sorted(s)
        gi = si = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi   # gi是得到满足的孩子序号，同时也是得到满足的孩子个数
