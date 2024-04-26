from random import randint

def binary_search(nums: list[int], target: int) -> int:
    # [i, j]
    i, j = 0, len(nums) - 1 

    while i <= j:
        idx = ( i+j ) // 2
        val = nums[idx]

        if val == target:
            return idx
        
        if val < target:
            i = idx + 1
        else:
            j = idx - 1
    
    return -1

def binary_insert_simple(nums: list[int], target: int) -> int:
    """
    with unique value inside nums, and target is not inside nums
    因此二分结束时一定有：
    i指向首个大于 target 的元素，
    j指向首个小于 target 的元素。
    易得当数组不包含 target时,
    插入索引为i。
    """
    i, j = 0, len(nums) - 1

    while i <= j:
        idx = ( i+j ) // 2
        val = nums[idx]

        if val == target:
            return idx
        
        if val < target:
            i = idx + 1
        else:
            j = idx - 1
    
    return i

def binary_insert_advance(nums: list[int], target: int) -> int:
    """
    target could be duplicated in the nums
    and for the duplicated item, we want to insert to the left hand side of the duplication
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        idx = ( i+j ) // 2
        val = nums[idx]

        if val == target:
            j = idx - 1 
            # right hand side
            # i = idx + 1
        
        if val < target:
            i = idx + 1
        else:
            j = idx - 1
    
    return i

def main():
    """当数组不包含 target 时, 最终i和j会分别指向首个大于,小于target的元素。"""
    nums = [i for i in range(1, 100+1)]
    res = binary_search(nums, 80)
    print(res)
    print(nums[res])

    nums = [i for i in range(1, 10+1, 2)]
    res = binary_insert_simple(nums, target=2)
    print(res)
    print(nums)

    nums = [1,3,6,6,6,6,6,10,12,15]
    res = binary_insert_advance(nums, target=6)
    print(res)
    print(nums)


if __name__ == "__main__":
    main()
