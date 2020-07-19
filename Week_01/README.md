# [Week1] - 学习笔记


## 源码分析

> 因为对Java不熟悉, 平时使用Python3作为主要编程语言, 所以分析的源码为Python3

Python 中 Queue 与 Priority Queue 的源码可参考 Appendix. Python 通过 Queue 类提供了一中先进先出的数据结构 —— 队列. 同时也实现了一系列常用的方法: 
- Queue.qsize(): 返回队列大小(不可靠!)
- Queue.empty(): 返回队列是否为空(不可靠!)
- Queue.full(): 返回队列是否已满(不可靠!)
- Queue.get(): 从队列中删除并返回一个项目.
- Queue.put(): 在队列中加入一个项目.

### qsize()
源码文件中首先导入了 `collections.dequde`. 而 Queue 类的构造函数中调用了一个名为 `_init()` 的方法. `_init()` 方法则是初始化了一个属性 `self.queue` 为一个双端队列. 当调用 `qsize()` 方法时, 返回 `self.deque` 的长度.

### empty()
本方法调用时根据 `self.deque` 的长度来判断是否为空. 若长度为 0 则为空, 若不为 0 则非空.

### full()
在 Queue 类初始化时, 定义了一个属性为 `self.maxsize` 表示队列的最大尺寸. `full()` 函数调用时根据 `_qsize()` 函数返回的队列长度与 `self.maxsize` 相比较. 当队列长度大于最大尺寸时, 返回为队列已满. 否则不满.

### get()
`get()` 在调用时实际是调用了双端队列 `deque` 的 `popleft()` 函数, 以实现队列的FIFO特性.

### put()
`get()` 在调用时实际是调用了双端队列 `deque` 的 `append()` 函数, 以实现队列的FIFO特性.


## 脚踏实地

在看超哥的视频时, 总觉得自己明白了, 对自己盲目的自信, 但是真实上手解题时总会感觉思路混乱. 但其实实际上就是还没有完全弄明白, 或者对刚弄明白的技巧或是知识还不够熟练. 所以在这个时候放弃那股较真的劲, 遵循超哥的"五毒神掌"原则. 虽然感觉上像是一种"投降", 没有自己想出来或是没有自己AC. 但实际上是在时间和动力还有记忆中的一种取舍平衡. 所以我意识到真正重要的是保持住那股冲劲, 不要被某道题影响. 多次重复, 多见不同的题. 把更多的精力分散在更多的题或是一道题的更多次数. 这样既不会打击自信心也能多重复遍数加强印象, 还能多见不同的题.

## 不要嫌弃暴力法

也许所有的人都希望自己在解题时能立马就想到最优的最巧的方法. 但是很不幸图灵奖的获得者寥寥无几, 所以一定~~认清形势放弃幻想~~不要妄想一道没见过类型的题上来就能想的出来最好的解法, 相信暴力的方法肯定都是能想得到的. 一定不要认为暴力算法没有任何可取之处. 往往比较巧妙的想法是在暴力算法的改进的基础上, 一步一步的优化而来的. 而且当面试时, 从暴力算法开始一步一步的给出较优的最后给出最优的算法也是一种思路明确展现的方式. 有时不一定要给出最优的解法, 反而清晰的思路更吸引人.

## 双指针不止两个指针

在看视频和解题时, 常常会遇到需要双指针的方法进行解题的时候. 而对于刚接触这类方法或者是对于稍微复杂的问题时, 很容易想不清楚具体的指针的位置和想要做什么. 思维很容易陷入混乱. 而这个时候一支笔一张纸是最好的帮手. 在纸上画一下思路的过程, 把两个指针的位置明确的画出来, 把自己头脑里的想象具象化. 远比光是干想来的效率来的清晰. 同样的经验也适用于所有思维容易混乱时, 想不明白的时候都可以借用一下纸和笔.

## Appendix(Python 3.8.3 Source Code)

```python
class Queue:
    '''Create a queue object with a given maximum size.

    If maxsize is <= 0, the queue size is infinite.
    '''

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)

        # mutex must be held whenever the queue is mutating.  All methods
        # that acquire mutex must release it before returning.  mutex
        # is shared between the three conditions, so acquiring and
        # releasing the conditions also acquires and releases mutex.
        self.mutex = threading.Lock()

        # Notify not_empty whenever an item is added to the queue; a
        # thread waiting to get is notified then.
        self.not_empty = threading.Condition(self.mutex)

        # Notify not_full whenever an item is removed from the queue;
        # a thread waiting to put is notified then.
        self.not_full = threading.Condition(self.mutex)

        # Notify all_tasks_done whenever the number of unfinished tasks
        # drops to zero; thread waiting to join() is notified to resume
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0

    def task_done(self):
        '''Indicate that a formerly enqueued task is complete.

        Used by Queue consumer threads.  For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.

        If a join() is currently blocking, it will resume when all items
        have been processed (meaning that a task_done() call was received
        for every item that had been put() into the queue).

        Raises a ValueError if called more times than there were items
        placed in the queue.
        '''
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished

    def join(self):
        '''Blocks until all items in the Queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.

        When the count of unfinished tasks drops to zero, join() unblocks.
        '''
        with self.all_tasks_done:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()

    def qsize(self):
        '''Return the approximate size of the queue (not reliable!).'''
        with self.mutex:
            return self._qsize()

    def empty(self):
        '''Return True if the queue is empty, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() == 0
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can grow before the result of empty() or
        qsize() can be used.

        To create code that needs to wait for all queued tasks to be
        completed, the preferred technique is to use the join() method.
        '''
        with self.mutex:
            return not self._qsize()

    def full(self):
        '''Return True if the queue is full, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() >= n
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can shrink before the result of full() or
        qsize() can be used.
        '''
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def put(self, item, block=True, timeout=None):
        '''Put an item into the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until a free slot is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise ('block' is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception ('timeout'
        is ignored in that case).
        '''
        with self.not_full:
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()

    def get(self, block=True, timeout=None):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        '''
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        '''
        return self.put(item, block=False)

    def get_nowait(self):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        '''
        return self.get(block=False)

    # Override these methods to implement other queue organizations
    # (e.g. stack or priority queue).
    # These will only be called with appropriate locks held

    # Initialize the queue representation
    def _init(self, maxsize):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        return self.queue.popleft()


class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)
```