#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/11 15:46
@user: jiananwang
@title: my_ArrayHashMap
"""
import random


class Pair:
    """
    每个桶中保存的键值对对象，
    """

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val


class ArrayHashMap:
    """
    基于数组建议实现哈希表
    """
    def __init__(self):
        """
        初始化一个包含100个桶（空位）的数组
        """
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        """
        hash function
        :param key:
        :return:
        """
        index = key % 100
        return index

    def get(self, key: int) -> None | str:
        """获取"""
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str):
        """添加"""
        pair = Pair(key=key, val=val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key):
        """删除"""
        index: int = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        """获取所有键值对"""
        res: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                res.append(pair)
        return res

    def key_set(self) -> list[int]:
        """获取所有键"""
        res: list[int] = []
        for pair in self.buckets:
            if pair is not None:
                res.append(pair.key)
        return res

    def val_set(self) -> list[str]:
        """获取所有键"""
        res: list[str] = []
        for pair in self.buckets:
            if pair is not None:
                res.append(pair.val)
        return res

    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)


if __name__ == '__main__':
    my_HashTable = ArrayHashMap()

    my_HashTable.put(key=23, val="a")
    my_HashTable.put(key=33, val="b")
    my_HashTable.put(key=356, val="c")
    my_HashTable.put(key=97, val="d")
    my_HashTable.put(key=92, val="e")

    print(my_HashTable.get(23))
    print(my_HashTable.get(97))
    my_HashTable.remove(356)

    print(my_HashTable.entry_set())
    print(my_HashTable.key_set())
    print(my_HashTable.val_set())
    print(my_HashTable.print())


