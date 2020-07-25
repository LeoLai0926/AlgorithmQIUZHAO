# [Week2] - 学习笔记

## 学习感悟

1. 老师在视频中给出的递归代码是通用的模板, 具体到某道题应该如何实现, 还需要大量的练习. 利用模板的思路以及一些固定的套路, 具体问题具体分析, 才能做好递归这类的题. 
2. 在解决树类的问题时, 不能认为只能通过递归来解决, 实际上很多的题目通过迭代也能很好的解决, 迭代也是解题很好的思路, 因此对于各类问题都不能先入为主, 需要思维灵活.


## 树

> 1. **二叉搜索树(BST)的中序遍历是递增的**
> 
> 2. 二叉树的**层序遍历**满足数组中第 `i` 个结点的左子结点索引为 `2i`, 右子结点的索引为 `2i+1`. 可以利用这个特性类解决问题.

## 遍历代码模板
```python
def preorder(self, root):
    if root: 
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```

## 递归

### 思维要点

1. 不要人肉进行递归(最大误区)
2. 找到最近最简方法, 将其拆解成可重复解决的问题(重复子问题)
3. 数学归纳法思维

### 代码模板

```python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data, ...)

    # drill down
    self.recursion(level + 1, param1, param2', ...)

    # reverse the current level status if needed
```

## 图

## 扩展参考链接

1. [连通图个数](http://leetcode-cn.com/problems/number-of-islands/)
2. [拓扑排序（Topological Sorting）](http://zhuanlan.zhihu.com/p/34871092)
3. [最短路径（Shortest Path）：Dijkstra](http://www.bilibili.com/video/av25829980)
4. [最小生成树（Minimum Spanning Tree）](http://www.bilibili.com/video/av84820276)

### DFS 代码模板

```python
visited = set()
def dfs(node, visited):
    if node in visited: # terminator
        # already visited
        return

    visited.add(node)

    # process current node here
    # ...

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

### BFS 代码模板

```python
def bfs(graph, start, end):
    queue = []
    queue.append([start])

    visited = set()     # 与树中的bfs最大的不同

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```


## Heap Sort（堆排序）自学笔记

### Heap Sort

堆排序利用堆的特性来对数组进行排序, 在大根堆中, 最大元素始终为根节点. 堆排序循环的从堆中取出根节点来排序. 具体步骤如下:

1. 从未排序的数组构造大根堆 `heap`
2. 提取最大元素 `A[0]`.
3. 交换 `A[-1]` 与 `A[0]`. (此时最大元素已位于堆的最后)
4. 从堆中 `pop` 出最大值
5. 对堆进行 `max_heapify`
6. 转至2, 除非堆已空

### 复杂度分析

构造大根堆 `build_maxHeap` 具有 $O(N)$ 的复杂度, `max_heapify` 具有 $O(\log{N})$ 的复杂度, 在排序过程中共执行 $N-1$ 次 `max_heapify`. 因此堆排序的复杂度为 $O(N\log{N})$

### Python 实现

```python
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest)
```

```python
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
```

```python
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 
# Reference link: https://www.geeksforgeeks.org/python-program-for-heap-sort/
```



## [代码模板（二叉树遍历）](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s/)

### 递归

> 时间复杂度：$O(n)$，$n$为节点数，访问每个节点恰好一次。
> 
> 空间复杂度：空间复杂度：$O(h)$，$h$为树的高度。最坏情况下需要空间$O(n)$，平均情况为$O(\log{n})$

#### 递归1

二叉树遍历最易理解和实现版本

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序递归
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归 
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

#### 递归2

通用模板，可以适应不同的题目，添加参数、增加返回条件、修改进入递归条件、自定义返回值

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return      
            # 前序递归
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right) 
            # # 中序递归
            # dfs(cur.left)
            # res.append(cur.val)
            # dfs(cur.right)
            # # 后序递归
            # dfs(cur.left)
            # dfs(cur.right)
            # res.append(cur.val)      
        res = []
        dfs(root)
        return res
```


### 迭代

> 时间复杂度：$O(n)$，$n$为节点数，访问每个节点恰好一次。
> 
> 空间复杂度：$O(h)$，$h$为树的高度。取决于树的结构，最坏情况存储整棵树，即$O(n)$

#### 迭代1

前序遍历最常用模板（后序同样可以用）

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []        
        res = []
        stack = [root]
        # # 前序迭代模板：最常用的二叉树DFS迭代遍历模板
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
        
        # # 后序迭代，相同模板：将前序迭代进栈顺序稍作修改，最后得到的结果反转
        # while stack:
        #     cur = stack.pop()
        #     if cur.left:
        #         stack.append(cur.left)
        #     if cur.right:
        #         stack.append(cur.right)
        #     res.append(cur.val)
        # return res[::-1]
```

#### 迭代2

层序遍历最常用模板

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur, res = [root], []
        while cur:
            lay, layval = [], []
            for node in cur:
                layval.append(node.val)
                if node.left: lay.append(node.left)
                if node.right: lay.append(node.right)
            cur = lay
            res.append(layval)
        return res
```

#### 迭代3

前、中、后序遍历通用模板（只需一个栈的空间）

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        
        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res
        
        # # 后序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]
```

#### 迭代4

标记法迭代（需要双倍的空间来存储访问状态）

前、中、后、层序通用模板，只需改变进栈顺序或即可实现前后中序遍历，而层序遍历则使用队列先进先出。0表示当前未访问，1表示已访问。

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(0, root)]
        while stack:
            flag, cur = stack.pop()
            if not cur: continue
            if flag == 0:
                # 前序，标记法
                stack.append((0, cur.right))
                stack.append((0, cur.left))
                stack.append((1, cur))
                
                # # 后序，标记法
                # stack.append((1, cur))
                # stack.append((0, cur.right))
                # stack.append((0, cur.left))
                
                # # 中序，标记法
                # stack.append((0, cur.right))
                # stack.append((1, cur))
                # stack.append((0, cur.left))  
            else:
                res.append(cur.val)  
        return res
        
        # # 层序，标记法
        # res = []
        # queue = [(0, root)]
        # while queue:
        #     flag, cur = queue.pop(0)  # 注意是队列，先进先出
        #     if not cur: continue
        #     if flag == 0:
                  # 层序遍历这三个的顺序无所谓，因为是队列，只弹出队首元素
        #         queue.append((1, cur))
        #         queue.append((0, cur.left))
        #         queue.append((0, cur.right))
        #     else:
        #         res.append(cur.val)
        # return res
```

### 莫里斯遍历

> 时间复杂度：$O(n)$，$n$为节点数，看似超过$O(n)$，有的节点可能要访问两次，实际分析还是$O(n)$，具体参考大佬博客的分析。
> 
> 空间复杂度：$O(1)$，如果在遍历过程中就输出节点值，则只需常数空间就能得到中序遍历结果，空间只需两个指针。如果将结果储存最后输出，则空间复杂度还是$O(n)$。
>
> >PS：莫里斯遍历实际上是在原有二叉树的结构基础上，构造了线索二叉树，

**线索二叉树定义为**：原本为空的右子节点指向了中序遍历顺序之后的那个节点，把所有原本为空的左子节点都指向了中序遍历之前的那个节点


此处只给出中序遍历，前序遍历只需修改输出顺序即可。而后序遍历，由于遍历是从根开始的，而线索二叉树是将为空的左右子节点连接到相应的顺序上，使其能够按照相应准则输出。但是后序遍历的根节点却已经没有额外的空间来标记自己下一个应该访问的节点，所以这里需要建立一个临时节点dump，令其左孩子是root。并且还需要一个子过程，就是倒序输出某两个节点之间路径上的各个节点。

莫里斯遍历，借助线索二叉树中序遍历（附前序遍历）

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        # cur = pre = TreeNode(None)
        cur = root

        while cur:
            if not cur.left:
                res.append(cur.val)
                # print(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    # print(cur.val) 这里是前序遍历的代码，前序与中序的唯一差别，只是输出顺序不同
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    res.append(cur.val)
                    # print(cur.val)
                    cur = cur.right
        return res
```

### N叉树遍历

> 时间复杂度：时间复杂度：$O(M)$，其中 $M$ 是 $N$ 叉树中的节点个数。每个节点只会入栈和出栈各一次。
>
> 空间复杂度：$O(M)$。在最坏的情况下，这棵 $N$ 叉树只有 $2$ 层，所有第 $2$ 层的节点都是根节点的孩子。将根节点推出栈后，需要将这些节点都放入栈，共有 $M−1$ 个节点，因此栈的大小为 $O(M)$。

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
```

#### N叉树简洁递归

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res
```

#### N叉树通用递归模板

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res
```

#### N叉树迭代方法

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        # s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            # for child in node.children[::-1]:
            #     s.append(child)
            s.extend(node.children[::-1])
        return res
```

### 相关题目

- [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/)
- [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/)
- [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/)
- [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/)
- [589. N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)