from my_binary_tree import TreeNode

class BinarySearchTree:
    def __init__(self) -> None:
        self._root = binary_search_tree_initialize()

    def search(self, num: int) -> TreeNode | None:
        """
        find the node with value num
        """
        cur: TreeNode = self._root

        while cur is not None:
            if num == cur.val:
                return cur
            
            if num > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        return f"{num} is not found in binary search tree"
    
    def insert(self, num: int) -> None:
        """
        """
        cur: TreeNode | None = self._root
        pre: TreeNode | None = None

        if self._root is None:
            self._root = TreeNode(num)
            return self._root

        while cur is not None:
            if num == cur.val:
                print(f"{num} already exist")
                return
            
            pre = cur
            if num > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        if num > pre.val:
            pre.right = TreeNode(num)

        if num < pre.val:
            pre.left = TreeNode(num)

        return
    
    def remove(self, num: int) -> None:
        """
        remove the node in the binary search tree with value num
        """

        if self._root == None:
            return
        
        # search for the treenode with value num
        cur: TreeNode = self._root
        pre: TreeNode | None = None
        while cur is not None:
            if num == cur.val:
                break
            
            pre = cur
            if num > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        # if the degree of the treenode to be removed is 0
        if cur.left is None and cur.right is None:
            if cur != self._root:
                if pre.left == cur:
                    pre.left = None
                if pre.right == cur:
                    pre.right = None
            else:
                self._root = None

        # if the degree of the treenode to be removed is 1
        if cur.left is None or cur.right is None:
            if cur != self._root:
                if pre.left == cur:
                    pre.left = cur.left or cur.right
                if pre.right == cur:
                    pre.left = cur.left or cur.right
            else:
                self._root = cur.left or cur.right

        # if the degree of the treenode to be removed is 2, the replacement for the 
        # removed treenode could be the greatest on the left hand tree or the smallest node
        # on the right hand tree
        
        # here we use the smallest treenode on the right hand tree
        
        if cur.left and cur.right:
            tmp: TreeNode = cur.right
            
            while tmp.left is not None:
                tmp = tmp.left
            
            self.remove(num=tmp.val)

            cur.val = tmp.val

        return

    def in_order(self) -> list[int]:
        """
        in order depth search for a binary search tree should be in ascending order
        """
        def _in_order(root: TreeNode) -> None:
            """
            """
            if root is None:
                return
            
            _in_order(root=root.left)
            res.append(root.val)
            _in_order(root=root.right)
        
        res: list[int] = [ ]
        _in_order(root=self._root)

        return res

def binary_search_tree_initialize() -> TreeNode | None:
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
    n8 = TreeNode(value=8)
    n9 = TreeNode(value=9)
    n10 = TreeNode(value=10)
    n11 = TreeNode(value=11)
    n12 = TreeNode(value=12)
    n13 = TreeNode(value=13)
    n14 = TreeNode(value=14)
    n15 = TreeNode(value=15)

    n8.left = n4
    n8.right = n12

    n4.left = n2
    n4.right = n6

    n2.left = n1
    n2.right = n3

    n6.left = n5
    n6.right = n7

    n12.left = n10
    n12.right = n14

    n10.left = n9
    n10.right = n11

    n14.left = n13
    n14.right = n15

    return n8


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    print(binary_search_tree.search(10).val)
    print(binary_search_tree.search(16))
    binary_search_tree.insert(16)
    print(binary_search_tree.search(16).val)
    binary_search_tree.insert(16)
    binary_search_tree.remove(10)
    print(binary_search_tree.search(16).val)
    print(binary_search_tree.in_order())

