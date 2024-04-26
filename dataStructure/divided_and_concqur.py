class TreeNode:
    def __init__(self, val:int) -> None:
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        
        return


def binary_search_recur(nums: list[int], target: int) -> int:
    """
    nums 是一个“有序”数组
    """
    def _recur(nums: list[int], left: int, right: int, target:int) -> int:

        if left > right:
            return -1
        
        """
        1 2 3
        0 1 2

        3

        left = 0, right = 2
        mid = (0 + 2) // 2 = 1

        left = mid + 1 = 2
        now left == right
        but still need a round of search until
        left is > right (not left >= right)

        """
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1
            return _recur(nums=nums, left=left, right=right, target=target)
        else:
            right = mid - 1
            return _recur(nums=nums, left=left, right=right, target=target)

    res = _recur(nums=nums, left=0, right=len(nums)-1, target=target)
    
    print(res)
    return

def rebuild_binary_tree(order_pre: list[int], order_in: list[int]) -> list[int]:
    """
    给定一棵二叉树的前序遍历order_pre和中序遍历order_in, 请从中构建二叉树并返回
    假设二叉树中没有重复的节点
    e.g.
    order_pre = [3, 9, 2, 1, 7]
    order_in = [9, 3, 1, 2, 7]

    * order_pre的首元素一定是根结点
    * order_in中根结点左右分别代表了根结点下的左子树和右子树

    * 对于order_pre中的每一个节点对应的index i, 其左子树的根结点对应的index 一定是 i+1, 
        * 困难在于如何确定其右子树的根结点的 index
    * 可以通过root节点在order_in中的位置得知左子树和右子树子节点的数量
        * 从而获得下一个右子树的idx
        * 对应到下面的idx_root - left

    e.g.
    if root is 3, then the number of node for the left tree for 3 is 1, for the right tree is 3
    so, from the index in order_pre, the next 1 node is the order_pre for the left tree
    from the index in order_pre, the next 3 node from next 1 node is the order_pre for the right tree
    """
    # for efficiency, create a hash table to store the index of each tree node in order_in
    # otherwise each time need to search within order_in
    map_order_in = {
        # node_val: index
        key: value for value, key in enumerate(order_in)
    }

    def _recur(left: int, right: int, i: int) -> list[int]:
        """
        """
        if right - left < 0:
            return None
        
        # root for current tree, from order_pre
        root = TreeNode(val=order_pre[i])

        # index for root in order_in
        idx_root = map_order_in[root.val]

        # get the index for sub tree nodes based on idx_root
        left_root = i + 1
        right_root = i + 1 + (idx_root - left)
        
        left_begin = left
        left_end = idx_root - 1 

        right_begin = idx_root + 1
        right_end = right

        # complete the tree
        root.left = _recur(left=left_begin, right=left_end, i=left_root)
        root.right = _recur(left=right_begin, right=right_end, i=right_root)

        return root

    root = _recur(left=0, right=len(order_in)-1, i=0) 

    return root

def solve_hanota(n: int, A: list[int], B: list[int], C: list[int]) -> None:

    def move(src: list[int], tar: list[int]) -> None:
        """
        move the last one of src to the last one of tar
        """
        pop = src.pop()
        tar.append(pop)

        return

    def _recur(n: int, scr: list[int], buf: list[int], tar: list[int]) -> None:
        """
        # 将 A 顶部 n 个圆盘借助 B 移到 C
        """
        if n == 1:
            move(scr, tar)
            return
        
        # 将 n-1 个圆盘从 A 移动到 B
        _recur(n=n-1, scr=scr, buf=tar, tar=buf)
        
        # 将剩余一个圆盘从 A 移动至 C
        move(scr, tar)

        # 将 n-1 个圆盘从 B 移动至 C
        _recur(n=n-1, scr=buf, buf=scr, tar=tar)

    ###
    _recur(n=n, scr=A, buf=B, tar=C)

    return

def main():
    nums = [i for i in range(1, 100+1)]
    binary_search_recur(nums=nums, target=98)

    order_pre = [3, 9, 2, 1, 7]
    order_in = [9, 3, 1, 2, 7]
    root = rebuild_binary_tree(order_pre, order_in)

    print(root.val)
    print(root.left.val)
    print(root.right.val)

    print(root.right.left.val)
    print(root.right.right.val)


    A = [i for i in range(2 ** 3, 0, -1)]
    print(A)
    B = [ ]
    C = [ ]
    solve_hanota(n=len(A), A=A, B=B, C=C)
    print(C)

    return

if __name__ == "__main__":
    main()
