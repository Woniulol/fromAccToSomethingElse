import  heapq


min_heap, flag = [ ], 1
max_heap, flag = [ ], -1

heapq.heappush(max_heap, flag * 1)
heapq.heappush(max_heap, flag * 3)
heapq.heappush(max_heap, flag * 2)
heapq.heappush(max_heap, flag * 5)
heapq.heappush(max_heap, flag * 4)

peek: int = flag * max_heap[0]

val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)
val = flag * heapq.heappop(max_heap)

size: int = len(max_heap)

is_empty: bool = not max_heap

min_heap: list[int] = [1,3,2,5,4]
heapq.heapify(min_heap)
print(min_heap)