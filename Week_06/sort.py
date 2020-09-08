import numpy as np

class Sorter:
    def __init__(self, arr=None):
        self._get_arr(arr)

    def _get_arr(self, arr):
        if not arr:
            s = input()
            arr = [int(num.strip(' ')) for num in s[1:-1].split(',')]
        self.arr = arr
    
    def ground_truth(self):
        arr = self.arr.copy()
        return sorted(arr)
    
    # 冒泡排序
    def bubble_sort(self):
        arr = self.arr.copy()
        n = len(arr)
        if n <= 1: return arr
        for i in range(0, n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # 选择排序
    def selective_sort(self):
        arr = self.arr.copy()
        n = len(arr)
        if n < 1: return arr
        for i in range(n):
            minval, minidx = float('inf'), None
            for j in range(i, n):
                if arr[j] < minval:
                    minidx, minval = j, arr[j]
            if i != minidx:
                arr[i], arr[minidx] = arr[minidx], arr[i]
        return arr

    # 插入排序
    def insertion_sort(self):
        arr = self.arr.copy()
        for i in range(len(arr)):
            preIdx = i - 1
            current = arr[i]
            while preIdx >= 0 and arr[preIdx] > current:
                arr[preIdx + 1] = arr[preIdx]
                preIdx -= 1
            arr[preIdx + 1] = current
        return arr

    # 快速排序
    def quick_sort(self):
        arr = self.arr.copy()
        arr = self._quick_sort(arr, 0, len(arr))
        return arr

    def _quick_sort(self, arr, left, right):
        if left < right:
            q = self._partition(arr, left, right)
            self._quick_sort(arr, left, q - 1)
            self._quick_sort(arr, q + 1, right)
        return arr
    
    def _partition(self, arr, l, r):
        counter, pivot = l, r-1
        for i in range(l, r):
            if arr[i] < arr[pivot]:
                arr[counter], arr[i] = arr[i], arr[counter]
                counter += 1
        arr[counter], arr[pivot] = arr[pivot], arr[counter]
        return counter

    # 归并排序
    def merge_sort(self):
        arr = self.arr.copy()
        self._merge_sort(arr, 0, len(arr)-1)
        return arr

    def _merge_sort(self, nums, left, right):
        if right <= left:
            return
        mid = (left+right) >> 1
        self._merge_sort(nums, left, mid)
        self._merge_sort(nums, mid+1, right)
        self._merge(nums, left, mid, right)

    def _merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid+1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i +=1
            else:
                temp.append(nums[j])
                j +=1
        while i<=mid:
            temp.append(nums[i])
            i +=1
        while j<=right:
            temp.append(nums[j])
            j +=1
        nums[left:right+1] = temp

if __name__ == "__main__":
    nums = np.random.randint(1,100,size=(20,)).tolist()
    # sorter = Sorter(nums)
    # gt = sorter.ground_truth()
    # bb = sorter.bubble_sort()
    # sl = sorter.selective_sort()
    # ins = sorter.insertion_sort()
    # qs = sorter.quick_sort()
    # ms = sorter.merge_sort()
    # print(nums)
    # print("gt: ", gt)
    # print("bb: ", bb)
    # print("sl: ", sl)
    # print("in: ", ins)
    # print("qs: ", qs)
    # print("ms: ", ms)

    # def quick_sort(array, l, r):
    #     if l < r:
    #         q = partition(array, l, r)
    #         quick_sort(array, l, q - 1)
    #         quick_sort(array, q + 1, r)
    #   
    # def partition(array, l, r):
    #     x = array[r]
    #     i = l - 1
    #     for j in range(l, r):
    #         if array[j] <= x:
    #             i += 1
    #             array[i], array[j] = array[j], array[i]
    #     array[i + 1], array[r] = array[r], array[i+1]
    #     return i + 1

    def quick_sort(arr, left, right):
        if left < right:
            q = partition(arr, left, right)
            quick_sort(arr, left, q-1)
            quick_sort(arr, q+1, right)
    
    def partition(arr, left, right):
        pivot = right
        counter = left - 1
        for i in range(left, right):
            if arr[i] <= arr[pivot]:
                i += 1
                arr[i], arr[counter] = arr[counter], arr[i]
        arr[counter+1], arr[pivot] = arr[pivot], arr[counter+1]
        return counter + 1

    print(nums)
    quick_sort(nums, 0, len(nums)-1)
    print(nums)
    print(sorted(nums))



