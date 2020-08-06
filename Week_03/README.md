# [Week3] - 学习笔记

## 分治与回溯

### 代码模板

```python
def divide_conque(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return

    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, p2, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, p2, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, p2, ...)
    ...

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

```

**递归的代码模板**

```python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
    process_result
    return 

    # process logic in current level
    process(level, data, ...)

    # drill down
    self.recursion(level+1, p1, p2, ...)

    # reverse the current level status if needed
```

## 深度优先与广度优先遍历

### 树的定义

```python

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### 深度优先遍历代码模板

1. 二叉树
```python
def dfs(node):
    if node in visited:
        # already visited
        return 

    visited.add(node)

    # process current logic here
    dfs(node.left)
    dfs(node.right)

```

2. 多叉树
```python
visited = set()

def dfs(node, visited):
    visited.add(node)
    for nxt_node in node.children:
        if not nxt_node in visited:
            dfs(nxt_node, visited)
```

```python
visited = set()

def dfs(node, visited):
    # Terminator
    if node in visited:
        # already visited
        return 

    for nxt_node in node.children:
```

3. 非递归写法
```python
visited = set()

def dfs(node, visited):
    # Terminator
    if not node: return []

    stack = [node]
    while stack:
        cur_node = stack.pop()
        visited.add(cur_node)

        process(cur_node)
        nodes = _generate_related_nodes(cur_node)
        stack.append(nodes)

    # other processing work
    ...
```

### 广度优先遍历代码模板

```python
def bfs(graph, startr, end):

    queue = collections.dqeue()
    queue.append(start)

    while queue:
        node = queue.popleft()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.extend(nodes)

    # other processing work
    ...
```

## 贪心算法

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优(即最有利)的选择, 从而希望导致结果是全局最好或最优的算法.

贪心算法与同台规划的不同在于它对每个子问题的解决方案都做出选择, 不能回退. 动态规划则会保存以前的运算结果, 并根据以前的结果对当前进行选择了, 有回退功能.

> **贪心算法**: 当下做局部最优判断.
> 
> **回溯算法**: 能够回退
> 
> **动态规划**: 最优判断加能够回退

## 二分查找

### 二分查找的前提

1. 目标函数单调性(单调递增或者递减)
2. 存在上下界(bounded)
3. 能够通过索引访问(index accessible)

### 代码模板

```python
left, right = 0, len(array)-1
while left <= right:
    mid = (right - left) / 2 + left
    if array[mid] == target:
        # Find the target
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### 课后作业

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if nums[-1] >= nums[0]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]: break
            else:
                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
        return mid + 1
```