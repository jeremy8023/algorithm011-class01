# 字典树和并查集
## 字典树Trie
### 背景
又称单词查找树，Trie树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。
### 1.数据结构
### 2.核心思想
1. 空间换时间
2. 利用字符串的公共前缀来
### 3.基本性质
1. 结点本身不存储完整单词；
2. 从根结点到某一节点，路径上经过的字符串连接起来，为该节点对应的字符串；
3. 每个节点的所有子节点路径代表的字符都不同。
### 4.实战题目
1. 208.实现Trie（前缀树）
2. 212.单词搜索ii

## 并查集
### 1.适用场景
1. 组团、配对问题
2. 是否在同一个组里面
### 2.基本操作
1. makeSet(s):新建一个并查集，其中包含s个单元素；
2. unionSet(x, y):如果元素x和元素y所在的集合不相交，则合并；否则，不相交；
3. find(x):找到元素x所在的集合；
### 3.实战题目
1. 547.朋友圈
2. 200.岛屿数量
3. 130.被围绕的岛屿

# 高级搜索：剪枝、双向BFS和启发式搜索
## 剪枝
采用回溯法，尝试分布解决一个问题。在分步解决问题的过程中，当
它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。
回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
> 找到一个可能存在的正确的答案

> 在尝试了所有可能的分步方法后宣告该问题没有答案
在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。


## 双向BFS
从前后分别进行BFS，找到第一次相遇的地方就是要找的答案

## 启发式搜索(A* 搜索)
### 代码模版
```
# Python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```
### 估价函数
启发式函数： h(n)，它用来评价哪些结点最有希望的是一个我们要找的结
点，h(n) 会返回一个非负实数,也可以认为是从结点n的目标结点路径的估计成本。
启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测
哪个邻居结点会导向一个目标。

# 高级树、红黑树和AVL树
## AVL树
自平衡的二叉搜索树
### 1.平衡因子：左子树的高度-右子树的高度
balance factor(平衡因子) = -1 or 0 or 1
### 2. 四种旋转操作
1. 左旋转
2. 右旋转
3. 左右旋转
4. 右左旋转
### 3.存在问题
1. 节点需要额外存储平衡因子；
2. 调整次数频繁

## 红黑树（Red-black Tree）
### 1.定义
红黑树是一种近似平衡的二叉搜索树，它能够确保任何一个节点的左右子树的高度差小于2倍。
### 2.满足条件
1. 每一个节点要么是红色，要么是黑色；
2. 根结点是黑色；
3. 每个叶子结点是黑色；
4. 不能有相邻的两个红色节点；
5. 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点

## AVL和红黑树的对比
1. AVL trees provide faster lookups than Red Black Trees because they are more strictly balanced.
2. Red Black Trees provide faster insertion and removal operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
3. AVL trees store balance factors or heights with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
4. Red Black Trees are used in most of the language libraries like map, multi-map, multi-setin C++ whereas AVL trees are use in databases where faster retrievals are required.

# 思考题
## 1.思考单词搜索ii用Trie树实现方式的时间复杂度