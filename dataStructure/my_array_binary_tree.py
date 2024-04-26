# use array structure to implement a binary tree structure

# given a treenode, get it's val, left tree node, right tree node and parent node
# pre-order, in-order, post-order, and level order search

class ArrayBinaryTree:
    """
    use array structure to implement a binary tree structure
    
    get size
    given a treenode (represented by array index), get it's val, left tree node, right tree node and parent node
    pre-order, in-order, post-order, and level order search
    """

    def __init__(self, arr: list[int | None]) -> None:
        """
        maintain a _tree for internal operation
        """
        self._tree = list(arr)

    def size(self):
        """
        size of the array
        """
        return len(self._tree)
    
    def val(self, i: int) -> int:
        """
        get the val from the index i
        """
        # return None if i is greater than the size of the array
        if i < 0 or i >= self.size():
            return None
        
        return self._tree[i]
    
    def left(self, i: int) -> int | None:
        """
        get the left treenode represented by the index of the array
        not doing index range check as will do in the val method
        """
        return 2*i + 1
    
    def right(self, i: int) -> int | None:
        """
        get the right treenode represented by the index of the array
        not doing index range check as will do in the val method
        """
        return 2*i + 2

    def parent(self, i: int) -> int | None:
        """
        get the parent treenode represented by the index of the array
        """
        return  (i-1) // 2
    
    def level_order(self) -> list[int]:
        """
        breadth-first search for a array binary tree is equivalent to the loop through of the array
        """
        res: list[int] = [ ]

        for i in range(self.size()):
            if self.val(i) is not None:
                res.append(self.val(i)) 

        return res
    
    def depth_order(self, order: str) -> list[int]:
        """
        depth-first search for a binary tree
        """

        def _depth_order(i: int, order: str) -> None:
            """
            pre: self, left, right
            in: left, self, right
            post: left, right, self
            """
            if self.val(i) is None:
                return
                
            if order == "pre":
                res.append(self.val(i))

            _depth_order(i=self.left(i), order=order)

            if order == "in":
                res.append(self.val(i))

            _depth_order(i=self.right(i), order=order)

            if order == "post":
                res.append(self.val(i))
                
        res: list[int] = [ ]
        _depth_order(i=0, order=order)

        return res
                

def main():
    my_array_binary_tree = ArrayBinaryTree([1, 2, 3, 4, 5, 6, 7])

    print(my_array_binary_tree.level_order())
    print(my_array_binary_tree.depth_order(order="pre"))
    print(my_array_binary_tree.depth_order(order="in"))
    print(my_array_binary_tree.depth_order(order="post"))

if __name__ == "__main__":
    main()

