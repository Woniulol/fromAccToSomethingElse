class TreeNode:
    """
    This class represents a node in a binary tree.

    Attributes:
    - val: The value of the node (default is 0).
    - left: The left child node of the current node (default is None).
    - right: The right child node of the current node (default is None).
    """

    def __init__(self, val: int = 0, left = None, right = None):
        """
        Initializes a TreeNode with the given value and optional left and right child nodes.

        Args:
        - val: The value to be assigned to the node.
        - left: The left child node (default is None).
        - right: The right child node (default is None).
        """
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def backtracking(root: TreeNode | None, target: int) -> list[list[int]]:
    """
    Returns a list of paths from the root to a node with the given target value.

    Args:
    - root: TreeNode | None: The root node of the tree.
    - target: int: The target value to search in the tree.

    Returns:
    - list[list[int]]: A list of paths from the root to a node with the target value.
    """
    # Initialize the result list
    res: list[list[int]] = [ ]  
    # Initialize the path list for storing the current path
    path: list[int] = [ ]  

    def _recur_backtrack(node: TreeNode | None):
        """
        Recursively explores the tree nodes in a preto find paths with the target value.

        Args:
        - node: TreeNode | None: The current node in the tree.

        Returns:
        - None
        """
        if not node:
            return  # Return if the current node is None

        # Update the path with the current node's value
        path.append(node.val)

        # If the current node's value matches the target, add the path to the result list
        if node.val == target:
            res.append(path.copy())

        # Recursively explore the left and right children of the current node
        _recur_backtrack(node.left)
        _recur_backtrack(node.right)

        # Remove the last node from the path when backtracking
        path.pop()

    _recur_backtrack(root)  # Call the recursive function with the root node
    return res  # Return the list of paths

def backtracking_w_prune(root: TreeNode | None, target: int) -> list[list[int]]:
    """
    backtracking with pruning condition
    """
    res: list[list[int]] = [ ]  
    path: list[int] = [ ]

    def _recur_backtrack(node: TreeNode | None):
        if (not node) or (node.val == 3):
            return
        
        path.append(node.val)
        if node.val == target:
            res.append(list(path))
        
        _recur_backtrack(node=node.left)
        _recur_backtrack(node=node.right)

        path.pop()
    
    ###
    _recur_backtrack(node=root)

    return res


if __name__ == '__main__':

    root = TreeNode(1)

    root.left = TreeNode(7)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    """
    1
    7 3
    4 5 6 7 
    """

    print(backtracking(root, 7))
    print(backtracking_w_prune(root, 7))


        