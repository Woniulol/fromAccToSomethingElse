"""
全排列问题(Permutation)

给定1 2 3, 求出所有可能的排列组合。

* 组合出现的顺序在某种程度上反映了决定的先后顺序
e.g.
[1, 2, 3] 不等于 [2, 1, 3]

* ?回退
[1, 2, 3] 回退到 [1, 2] -> [1, 3, 2]

* choices and state
whether 1, 2, 3 has been used or not
"""
def backtrack(
        choices: list[int],  # all available choices
        state: list[int],  # choice has been used
        selected: list[bool], # whether a choice has been selected
        res: list[list[int]]  # all possible permutations
) -> None:
    """
    permutation result will be appended to res
    function will return None
    """
    if len(state) == len(choices):
        res.append(list(state))

    # for i in range(len(choices)):
    for i, choice in enumerate(choices):
        if not selected[i]:
            state.append(choice)
            selected[i] = True

            backtrack(choices, state, selected, res)

            state.pop()
            selected[i] = False

    return

def backtrack_w_duplication(
        choices: list[int],
        state: list[int],
        selected: list[bool],
        res: list[list[int]]
) -> None:
    """
    1, 2, 2
    permutation result is [1, 2, 2], [1, 2, 2], [2, 1, 2], [2, 2, 1]
    
    if remove duplication, result 1, 2
    permutation result is [1, 2], [2, 1]
    """

    if len(state) == len(choices):
        res.append(list(state))
    
    """
    consider set() as a hash table without key
    purely for the purpose of removing duplication
    """
    duplicated: set[int] = set()

    for i, choice in enumerate(choices):

        if not selected[i] and choice not in duplicated:

            state.append(choice)
            selected[i] = True
            duplicated.add(choice)

            backtrack_w_duplication(choices, state, selected, res)

            state.pop()
            selected[i] = False

    return

def main():
    choices: list[int] = [1, 2, 3]
    res: list[list[int]] = [ ]
    selected: list[bool] = [False] * len(choices)
    backtrack(choices=choices, state=[], selected=selected, res=res)

    choices: list[int] = [1, 1, 2]
    res: list[list[int]] = [ ]
    selected: list[bool] = [False] * len(choices)
    backtrack_w_duplication(choices=choices, state=[], selected=selected, res=res)
    
    print(res)

    return

if __name__ == '__main__':
    main()
