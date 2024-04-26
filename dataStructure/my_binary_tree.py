from collections import deque


class TreeNode:
    """
    self defined binary tree node
    """
    def __init__(
            self, value: int
    ) -> None:
        self.val: int = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def level_order(
        root: TreeNode | None
) -> list[int]:
    """
    breadth-first search implemented by collections.deque
    """
    # take the result in each node
    res = [ ]
    # start from the root node
    queue: deque[TreeNode] = deque()
    queue.append(root)

    # loop through all possible nodes
    while queue:
        # get the next node
        node = queue.popleft()
        res.append(node.val)
        # update the queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    return res

def pre_order_wrapper(
        root: TreeNode | None
) -> list[int]:
    """
    pre_order depth-first search
    """

    def _pre_order(
            root: TreeNode | None
    ) -> None:
        """
        recursive pre_order binary search function
        """

        if root is None:
            return 
        
        res.append(root.val)
        _pre_order(root=root.left)
        _pre_order(root=root.right)

    res = [ ]
    _pre_order(root=root)

    return res

def in_order_wrapper(
        root: TreeNode | None
) -> list[int]:
    """
    in_order depth_first search
    """

    def _in_order(
            root: TreeNode | None
    ) -> None:
        """
        recursive in_order binary search function
        """

        if root is None:
            return 
        
        _in_order(root=root.left)
        res.append(root.val)
        _in_order(root=root.right)

    res = [ ]
    _in_order(root=root)

    return res

def post_order_wrapper(
        root: TreeNode | None
) -> list[int]:
    """
    post_order depth_first search
    """

    def _post_order(
            root: TreeNode | None
    ) -> None:
        """
        recursive post_order binary search function
        """

        if root is None:
            return 
        
        _post_order(root=root.left)
        _post_order(root=root.right)
        res.append(root.val)

    res = [ ]
    _post_order(root=root)

    return res

def binary_tree_initialize() -> TreeNode:
    """
    initialize a binary tree and return the root node of that tree
    """
    n1 = TreeNode(value=1)
    n2 = TreeNode(value=2)
    n3 = TreeNode(value=3)
    n4 = TreeNode(value=4)
    n5 = TreeNode(value=5)
    n6 = TreeNode(value=6)
    n7 = TreeNode(value=7)

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n2.right = n5

    n3.left = n6
    n3.right = n7

    return n1

def main():
    """
    """
    binary_tree = binary_tree_initialize()
    
    res = level_order(root=binary_tree)
    print(res)

    res = pre_order_wrapper(root=binary_tree)
    print(res)

    res = in_order_wrapper(root=binary_tree)
    print(res)

    res = post_order_wrapper(root=binary_tree)
    print(res)
    

if __name__ == "__main__":
    main()
    