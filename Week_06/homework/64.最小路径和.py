class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 动态规划法:向下/向右
        # 1.寻找最优子结构
        # 2.存储中间状态
        # 3.dp方程错误：min_path[k] = min(min_path[k-1] + list[i+1][j], min_path[k-1] +list[i][j+1])
        # 4.dp方程正确：min_path[i][j] = min(min_path[i-1][j]+ grid[i][j], min_path[i][j-1]+ grid[i][j])
                # 优化:min_path[i][j] = min(min_path[i-1][j], min_path[i][j-1]) + grid[i][j]
        # 注意边界条件的判断
        
        # min_path = grid
        # min_path = copy.deepcopy(grid)
        # 直接把结果复用在grid——list里面
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0: continue
                elif i==0: grid[i][j] = grid[i][j]+grid[i][j-1]
                elif j==0: grid[i][j] = grid[i][j]+grid[i-1][j]
                else:grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        # dp的返回值要视情况而定
        return grid[-1][-1]
        
        

