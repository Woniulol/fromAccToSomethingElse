from backtracking import TreeNode


def is_solution(state: list[TreeNode]) -> bool:
    return state and state[-1].val == 7

def record_solution(state: list[TreeNode], res: list[list[TreeNode]]) -> None:
    """
    solution is recorded in res and is based on state
    """
    res.append(list(state))
    return

def is_valid(state: list[TreeNode], choice: TreeNode) -> bool:
    """
    check if choice is valid based on state
    """
    return choice is not None and choice.val != 3

def make_choice(state: list[TreeNode], choice: TreeNode) -> None:
    """
    """
    state.append(choice)
    return

def undo_choice(state: list[TreeNode]) -> None:
    """
    """
    state.pop()
    return

def backtrack(
        state: list[TreeNode],
        choices: list[TreeNode],
        res: list[list[TreeNode]]
) -> list[list[TreeNode]]:
    
    # add to res if is solution
    if is_solution(state):
        record_solution(state, res)
        # here we dont have return as we want to continue the backtracking process

    # iterate over choices
    # choice is just a tree node ... 
    for choice in choices:
        # add choice to state
        if is_valid(state, choice):
            make_choice(state, choice)
            # only make recursive call if the choice is valid
            backtrack(state, [choice.left, choice.right], res)
            # backtrack
            undo_choice(state)


def main():
    root = TreeNode(1)

    root.left = TreeNode(7)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.left.left.left = TreeNode(7)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res: list[int] = []
    backtrack(state=[ ], choices=[root], res=res)
    for i in res:
        print([node.val for node in i])

if __name__ == '__main__':
    main()