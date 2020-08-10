# [Week4] - 学习笔记

## 代码模板

### 递归

```python
def recursion(level, param1, param2, ...):
    # Terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # Process logic in current level
    process(level, data, ...)

    # Drill down
    self.recursion(level + 1, p1, p2, ...)

    # Reverse the state if needed
```

### 分治

```python
def divide_conquer(problem, param1, param2, ...):
    # Terminator
    if problem is None:
        print_result
        return 
    
    # Prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # Conquer subproblems
    subresult1 = self.divide_conquer(subproblem[0], p1, p2, ...)
    subresult2 = self.divide_conquer(subproblem[1], p1, p2, ...)
    subresult3 = self.divide_conquer(subproblem[2], p1, p2, ...)
    ...

    # Process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # Reverse the state if needed
```

## 动态规划

### 定义

> Dynamic programming refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. [[wiki]](https://en.wikipedia.org/wiki/Dynamic_programming)

> 动态规划是指通过递归的方式将复杂问题分解为更简单的子问题来解决.

### 动态规划关键点
1. 最优子结构 `opt[n] = best_of(opt[n-1], opt[n-2], ...)`
2. 储存中间状态: `opt[i]`
3. 地推公式(美其名曰: 状态装壹方城或者 DP 方程)
    > Fib: opt[i] = opt[n-1] + opt[n-2]
    > 
    > 二维路径: opt[i, j] = opt[i+1][j] + opt[i][j+1] (且要判断 a[i,j] 是否为空地)

### 动态规划总结
1. 打破自己的思维惯性, 形成机器思维.
2. 理解复杂逻辑的关键.
3. 也是职业进阶的要点要领.

### 5 "easy" steps to DP:
1. Define subproblems
2. Guess (part of solution)
3. Relate subproblem solutions
4. Recurse and memorize or build DP table bottom-up
5. Solve original problem

