import random

def init_nums() -> list[int]:
    random.seed(2000)
    return [random.randint(0, 100) for i in range (0, 200)]

def selection_sort(nums: list[int]) -> list[int]:
    """"""
    # for n, only need sort on n - 1, the rest one will be sorted automatically
    for i in range(len(nums)-1):
        k = i
        
        for j in range(i+1, len(nums)):
            if nums[k] > nums[j]:
                k = j
            j += 1

        nums[k], nums[i] = nums[i], nums[k]
        
    return nums

def bubble_sort(nums: list[int]) -> list[int]:
    """"""
    n = len(nums)    
    # 未排序空间
    for i in range(n-1, 0, -1):

        for j in range(i):

            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]

    return nums

def insertion_sort(nums: list[int]) -> list[int]:
    """"""
    n = len(nums)
    for i in range(1, n):
        # i: 1, 2, 3, ..., n-1
        base = nums[i]

        j = i - 1
        # j: 0, 1, 2, 3, ..., n-2
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = base
    
    return nums

def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    """选取三个候选元素的中位数"""
    l, m, r = nums[left], nums[mid], nums[right]
    if (l <= m <= r) or (r <= m <= l):
        return mid  # m 在 l 和 r 之间
    if (m <= l <= r) or (r <= l <= m):
        return left  # l 在 m 和 r 之间
    return right

def fast_sort(nums: list[int], left: int, right: int) -> list[int]:
    def _partition(nums: list[int], left: int, right: int) -> int:
        """
        return the sign position "pivot"
        """
        # 以 nums[left] 为基准数
        med = median_three(nums, left, (left + right) // 2, right)
        # 将中位数交换至数组最左端
        nums[left], nums[med] = nums[med], nums[left]
        # 以 nums[left] 为基准数

        i, j = left, right
        
        while i < j:
            
            # from right to left search for the first number that is smaller than the pivot
            while i < j and nums[j] >= nums[left]:
                j -= 1

            # from left to right search for the first number that is greater than the pivot
            while i < j and nums[i] <= nums[left]:
                i += 1
            
            # swap the position
            nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[i] = nums[i], nums[left]

        return i
    
    ###
    if left >= right:
        return

    pivot = _partition(nums, left, right)

    fast_sort(nums, left=left, right=pivot-1)
    fast_sort(nums, left=pivot+1, right=right)

    return pivot

def merge_sort(nums: list[int], left: int, right: int) -> None:
    """
    inplace sort of nums
    """

    def _merge(nums: list[int], left: int, mid: int, right: int) -> None:
        """
        """
        tmp = [None] * (right - left + 1)
        
        i, j, k = left, mid + 1, 0
        
        while i <= mid and j <= right:

            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            
            k += 1
        
        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            tmp[k] = nums[j]
            j += 1
            k += 1

        # replace the origin nums with new tmp
        for k in range(0, len(tmp)):
            nums[left + k] = tmp[k]

        return
    

    ###
    if left >= right:
        return
    
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)

    _merge(nums, left=left, mid=mid, right=right)
    return

def head_sort(nums: list[int]) -> None:
    
    def _heapify(nums: list[int]) -> None:
        """
        heapify nums inplace
        """
        for i in range(len(nums) // 2 - 1, -1, -1):
            _sift_down(nums=nums, n=len(nums), i=i)

        return nums
    
    def _sift_down(nums: list[int], n: int, i: int = 0):
        """
        """
        while True:
            left = i * 2 + 1
            right = i * 2 + 2
            max_idx = i

            if left < n and nums[left] > nums[max_idx]:
                max_idx = left
            
            if right < n and nums[right] > nums[max_idx]:
                max_idx = right
            
            if max_idx != i:
                nums[max_idx], nums[i] = nums[i], nums[max_idx]
                i = max_idx
            else:
                break

    ###
    _heapify(nums)

    # switch the first node (biggest) with the last node 
    # and then do a sift_down for the range of none heapify array

    # loop only need to do n - 1 times and 
    # the last one will be in order automatically
    n = len(nums)
    for i in range(len(nums) - 1):
        # after this step there should already been part of the nums is sequencialized 
        nums[0], nums[n - len(nums) - 1] = nums[n - len(nums) - 1], nums[0]
        n -= 1

        _sift_down(nums=nums, n=n, i=0)

    return nums

def count_sort_naive(nums: list[int]) -> None:
    """
    nums should be non_negative integer
    """
    m = 0
    for i in nums:
        if m < i:
            m = i
    
    count = [0 for _ in range(0, m+1, 1)]
    for i in nums:
        count[i] += 1

    # number to sort is from 0 to 100, so the index for count should be 0 to 100 thus the len should be 101
    k = 0
    for i in range(0, len(count), 1):  
        for _ in range(0, count[i], 1):
            nums[k] = i
            k += 1

    return

def count_sort(nums: list[int]) -> None:
    """
    nums should be non_negative integer
    """
    m = 0
    for i in nums:
        if m < i:
            m = i
    
    count = [0 for _ in range(0, m+1, 1)]
    for i in nums:
        count[i] += 1

    for i in range(len(count) - 1):
        count[i+1] += count[i]

    n = len(nums)
    res = [None] * n

    for i in range(n-1, -1, -1):
        num = nums[i]
        res[count[num] - 1] = num
        count[num] -= 1

    for i in range(len(res)):
        nums[i] = res[i]

    return

def main():
    nums = init_nums()
    print(selection_sort(nums))

    nums = init_nums()
    print(bubble_sort(nums))

    nums = init_nums()
    print(insertion_sort(nums))

    nums = init_nums()
    fast_sort(nums=nums, left=0, right=len(nums)-1)
    print(nums)

    nums = init_nums()
    merge_sort(nums=nums, left=0, right=len(nums)-1)
    print(nums)

    nums = init_nums()
    print(head_sort(nums=nums))

    nums = init_nums()
    count_sort_naive(nums=nums)
    print(nums)

    nums = init_nums()
    count_sort(nums=nums)
    print(nums)

    return

if __name__ == "__main__":
    main()