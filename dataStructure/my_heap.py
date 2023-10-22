class MaxHeap:
    """使用数组自定义大顶堆"""
    
    def __init__(self, nums: list[int]) -> None:
        self.max_heap = nums
        # 内部维护了一个叫max_heap的数组
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    # 使用数组表示堆
    def left(self, i:int) -> int:
        """获取左子节点索引"""
        return 2 * i + 1

    def right(self, i:int) -> int:
        """获取右子节点索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取父节点索引"""
        return (i - 1) // 2  # 向下取整

    def peek(self) -> int:
        """访问堆顶元素"""
        return self.max_heap[0]
    
    def size(self) -> int:
        """获取堆大小"""
        return len(self.max_heap)
    
    def push(self, val: int):
        """元素入堆"""
        # 为了防止入堆改变所有的索引，先append，交换，再从顶到下heapify
        self.max_heap.append(val)
        