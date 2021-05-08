"""
Based on "Skip Lists: A Probabilistic Alternative to Balanced Trees" by William Pugh
https://epaperpress.com/sortsearch/download/skiplist.pdf
"""
from __future__ import annotations

from random import random
from typing import Generic, Optional, TypeVar


KT = TypeVar("KT")
VT = TypeVar("VT")


# 实现参考: https://github.com/TheAlgorithms/Python/blob/master/data_structures/linked_list/skip_list.py
# 概念参考: https://www.bilibili.com/video/BV1QK4y1Y7mS?from=search&seid=3191975880203391183
# 概念参考: https://mp.weixin.qq.com/s/AGPCfFg7bEiCsa5zNeCi4A
# 概念参考: 数据结构、算法于应用 c++ 语言描述
class Node(Generic[KT, VT]):
    def __init__(self, key: KT, value: VT):
        self.key = key
        self.value = value
        self.forward: list[Node[KT, VT]] = []

    def __repr__(self):
        return "<%s.Node key=%s value=%s at %s>" % (__name__, self.key, self.value, hex(id(self)))

    @property
    def level(self) -> int:
        return len(self.forward)


class SkipList(Generic[KT, VT]):
    def __init__(self, p: float = 0.5, max_level: int = 16):
        self.head = Node("root", None)                  # 根节点
        self.level = 0                                  # 跳表层级
        self.p = p                                      # 百分比, 默认是0.5, 意思是: 50%
        self.max_level = max_level                      # 跳表最大允许的层级

    # def __iter__(self):
    #     node = self.head
    #
    #     while len(node.forward) != 0:
    #         yield node.forward[0].key
    #         node = node.forward[0]

    def random_level(self) -> int:
        level = 1
        # random(): 0.56, 0.13, 0.75, ...
        # 随机数小于 0.5, 且 当前层级 < 16 则层级 +1.
        # 即: 抛硬币来决定新插入结点跨越的层数.
        while random() < self.p and level < self.max_level:
            level += 1

        return level

    def _locate_node(self, key) -> tuple[Optional[Node[KT, VT]], list[Node[KT, VT]]]:
        """
        :param key: Searched key,
        :return: Tuple with searched node (or None if given key is not present)
                 and list of nodes that refer (if key is present) of should refer to
                 given node.
        """

        # Nodes with refer or should refer to output node
        update_vector = []

        node = self.head

        for i in reversed(range(self.level)):
            # i < node.level - When node level is lesser than `i` decrement `i`.
            # node.forward[i].key < key - Jumping to node with key value higher
            #                             or equal to searched key would result
            #                             in skipping searched key.
            while i < node.level and node.forward[i].key < key:
                node = node.forward[i]
            # Each leftmost node (relative to searched node) will potentially have to
            # be updated.
            update_vector.append(node)

        update_vector.reverse()  # Note that we were inserting values in reverse order.

        # len(node.forward) != 0 - If current node doesn't contain any further
        #                          references then searched key is not present.
        # node.forward[0].key == key - Next node key should be equal to search key
        #                              if key is present.
        if len(node.forward) != 0 and node.forward[0].key == key:
            return node.forward[0], update_vector
        else:
            return None, update_vector

    def delete(self, key: KT):
        node, update_vector = self._locate_node(key)

        if node is not None:
            for i, update_node in enumerate(update_vector):
                # Remove or replace all references to removed node.
                if update_node.level > i and update_node.forward[i].key == key:
                    if node.level > i:
                        update_node.forward[i] = node.forward[i]
                    else:
                        update_node.forward = update_node.forward[:i]

    def insert(self, key: KT, value: VT):
        # 为了要保持跳表结构, 插入耗时O(n).
        node, update_vector = self._locate_node(key)
        if node is not None:
            node.value = value
        else:
            level = self.random_level()

            if level > self.level:
                # After level increase we have to add additional nodes to head.
                for i in range(self.level - 1, level):
                    update_vector.append(self.head)
                self.level = level

            new_node = Node(key, value)

            for i, update_node in enumerate(update_vector[:level]):
                # Change references to pass through new node.
                if update_node.level > i:
                    new_node.forward.append(update_node.forward[i])

                if update_node.level < i + 1:
                    update_node.forward.append(new_node)
                else:
                    update_node.forward[i] = new_node

    def find(self, key: VT) -> Optional[VT]:
        # TODO: 根据搜索次数来观察跳表是否符合预期
        node, _ = self._locate_node(key)

        if node is not None:
            return node.value

        return None


def main():

    skip_list = SkipList()
    skip_list.insert(2, "2")
    skip_list.insert(4, "4")
    skip_list.insert(6, "4")
    skip_list.insert(5, "5")
    skip_list.insert(8, "4")
    skip_list.insert(9, "4")

    skip_list.find(5)


if __name__ == "__main__":
    main()

