# 动态规划的实现和关键点
动态规划，本质上是动态递推，可以理解为一种迭代。
## 关键点
1. 动态规划和递归/分治，没有根本区别。主要查看有无最优子结构
2. 共性：找到重复子问题
3. 分治法没有最优子结构，动态规划有最优子结构，中途淘汰次优解。
4. 解题思路
    1. 自顶向下：分治+记忆化搜索；
    2. 自底向上：迭代法；（dp经常这样解决）

## 解题步骤
1. 寻找最优子结构
2. 存储中间状态，也就是存储最优子结构
3. 递推公式（DP方程）

## 递归代码模版
```
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 

    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

## 分治法代码模版
```
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```