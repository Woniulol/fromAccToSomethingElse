from collections import Counter


from typing import List


def show_store_name(store_names: List[str]) -> None:
    """A sample function to illustrate common practice in IO"""
    for store_name in store_names:
        print(store_name)




if __name__ == "__main__":
    [single] = (1, )
    print(single)

    s = "Test String"
    print(s.index(s))
    print(s.index(s))

    x = -1
    print(+x)
    print(-x)
    print(~x)
    print(x)

    lst = [1, 2, 3]
    lst2 = -lst
    lst3 = lst
    lst[0] = 10

    print(lst)
    print(lst2)
    print(lst3)
