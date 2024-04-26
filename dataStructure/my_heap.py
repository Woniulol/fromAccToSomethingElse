class MaxHeap:
    """
    self defined max heap
    """

    def __init__(self, nums: list[int]) -> None:
        self._max_heap = nums
        # heapify
        for i in range(self.parent((self.size() - 1)), -1, -1):
            self.sift_down(i)

    def size(self) -> int:
        return len(self._max_heap)
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def peek(self) -> int:
        return self._max_heap[0]
    
    def left(self, i: int) -> int:
        return 2*i + 1
    
    def right(self, i: int) -> int:
        return 2*i + 2
    
    def parent(self, i: int) -> int:
        return (i-1) // 2
    
    def swap(self, i: int, j: int) -> None:
        self._max_heap[i], self._max_heap[j] = self._max_heap[j], self._max_heap[i]

    def push(self, val: int) -> None:
        self._max_heap.append(val)
        self.sift_up((self.size() - 1))

    def sift_up(self, i: int) -> None:
        while True:
            parent = self.parent(i)
            if parent < 0 or self._max_heap[i] <= self._max_heap[parent]:
                break
            self.swap(i, parent)
            i = parent

    def pop(self) -> int:
        self.swap(0, self.size() - 1)
        val = self._max_heap.pop()
        
        self.sift_down(0)

        return val
    
    def sift_down(self, i: int) -> None:
        while True:
            left = self.left(i)
            right = self.right(i)
            max_val_index = i

            if left < self.size() and self._max_heap[left] >= self._max_heap[max_val_index]:
                max_val_index = self.left(i)

            if right < self.size() and self._max_heap[right] >= self._max_heap[max_val_index]:
                max_val_index = self.right(i)
            
            if max_val_index == i:
                break
            
            self.swap(max_val_index, i)
            i = max_val_index

if __name__ == "__main__":
    max_heap = MaxHeap(nums=[9,8,6,6,7,5,2,1,4,3,6,2])
    print(max_heap._max_heap)
    max_heap.push(7)
    print(max_heap._max_heap)
    
    print(max_heap.pop())
    print(max_heap._max_heap)
