#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023/10/11 16:28
@user: jiananwang
@title: my_HashMapChaining
"""
import random


class Pair:
    """
    每个链表（列表/动态数组）节点中保存的键值对对象，
    """

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val


class HashMapChaining:
    """链式地址哈希表"""

    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对数量
        self.capacity = 10  # 哈希表容量
        self.load_threshold = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets: list[list[Pair]] = [[] for _ in range(self.capacity)]  # 桶数组

    def hash_funct(self, key: int) -> int:
        """hash function"""
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        """查询操作"""
        index: int = self.hash_funct(key)
        bucket: list[Pair] = self.buckets[index]
        # 遍历桶若找到key则返回val
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None

    def extend(self):
        """扩容哈希表"""
        # 将当前哈希表暂存
        buckets: list[list[Pair]] = self.buckets
        # 初始化扩容后的哈希表
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # 转移暂存的哈希表
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def put(self, key: int, val: str):
        """添加操作"""
        # 判断负载程度
        if self.load_factor() > self.load_threshold:
            self.extend()
        index: int = self.hash_funct(key)
        bucket: list[Pair] = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                # 如果key已经存在就更行对应的val
                # 注意这里找到的是相同的key 不是 index
                # index是导致hash冲突的问题，不是key
                return
        pair = Pair(key=key, val=val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """删除"""
        index = self.hash_funct(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def print(self):
        """打印哈希表"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                if pair is not None:
                    res.append(str(pair.key) + "->" + pair.val)
                    print(res)


if __name__ == '__main__':
    myHashMapChaining = HashMapChaining()

    for i in [random.randint(1, 1000000) for i in range(1, 10000)]:
        myHashMapChaining.put(i, str(i)+"self")

    myHashMapChaining.print()
