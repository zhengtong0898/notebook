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

    def __repr__(self) -> str:
        return f"<Node key={self.key} value={self.value} at {hex(id(self))}>"

    @property
    def level(self) -> int:
        return len(self.forward)


class SkipList(Generic[KT, VT]):
    def __init__(self, p: float = 0.5, max_level: int = 16):
        self.head = Node("root", None)           # 根节点
        self.level = 0                           # 跳表层级
        self.p = p                               # 硬币概率: 0.5 == 50%

        # 默认情况下, 最大层级: 16
        # pow(2, 16) = 65536, 即: max_level = 16 的情况下, 当前 SkipList 允许最多存储 65536 个节点.
        #
        # 第 1层链表,包含所有节点.                                               一共有 65536 个节点
        # 第 2层链表,每间隔    2个(第1层链表)节点,复制当前节点作为第 2层链表的节点;一共有 32768 个节点
        # 第 3层链表,每间隔    4个(第1层链表)节点,复制当前节点作为第 3层链表的节点;一共有 16384 个节点
        # 第 4层链表,每间隔    8个(第1层链表)节点,复制当前节点作为第 4层链表的节点;一共有 8192 个节点
        # 第 5层链表,每间隔   16个(第1层链表)节点,复制当前节点作为第 5层链表的节点;一共有 4096 个节点
        # 第 6层链表,每间隔   32个(第1层链表)节点,复制当前节点作为第 6层链表的节点;一共有 2048 个节点
        # 第 7层链表,每间隔   64个(第1层链表)节点,复制当前节点作为第 7层链表的节点;一共有 1024 个节点
        # 第 8层链表,每间隔  128个(第1层链表)节点,复制当前节点作为第 8层链表的节点;一共有 512 个节点
        # 第 9层链表,每间隔  256个(第1层链表)节点,复制当前节点作为第 9层链表的节点;一共有 256 个节点
        # 第10层链表,每间隔  512个(第1层链表)节点,复制当前节点作为第10层链表的节点;一共有 128 个节点
        # 第11层链表,每间隔 1024个(第1层链表)节点,复制当前节点作为第11层链表的节点;一共有 64 个节点
        # 第12层链表,每间隔 2048个(第1层链表)节点,复制当前节点作为第12层链表的节点;一共有 32 个节点
        # 第13层链表,每间隔 4096个(第1层链表)节点,复制当前节点作为第13层链表的节点;一共有 16 个节点
        # 第14层链表,每间隔 8192个(第1层链表)节点,复制当前节点作为第14层链表的节点;一共有  8 个节点
        # 第15层链表,每间隔16384个(第1层链表)节点,复制当前节点作为第15层链表的节点;一共有  4 个节点(node-0, node-16384, node-49152, node-65536)
        # 第16层链表,每间隔32768个(第1层链表)节点,复制当前节点作为第16层链表的节点;一共有  3 个节点(node-0, node-32768, node-65536)
        #
        # 边界情况:
        # 第 16 层会在 32768 个节点出建立一个节点, 即: 0-32767 为有效左, 32768 - 65535 为有效右,
        # 由此得出第 16 层最多可以存储 65536 个节点.
        self.max_level = max_level

    def __str__(self) -> str:
        # 从 self.head。forward 中的第0个元素中一直去到末端.
        # 即: items = 第0层数据的Node的所有keys.
        items = list(self)

        if len(items) == 0:
            return f"SkipList(level={self.level})"

        label_size = max((len(str(item)) for item in items), default=4)
        label_size = max(label_size, 4) + 4

        # self.head           == <Node key='root' value=None>
        # id(node)            == id(self.head)
        # id(node.forward)    == id(self.head.forward)
        # id(node.forward[0]) == id(self.head.forward[0])
        #
        # node 完全引用 self.head
        node = self.head
        lines = []

        # python 语言中 copy 有三种情况, 这里仅描述的是 class obj; 因为 python 的 int 和 string 没有引用概念, 是deepcopy概念.
        # 第一种: forwards     = node.forward
        #        id(forwards) == id(node.forward)
        #        forwards 完全引用 node.forward, 即: forwards 发生变化(元素的属性发生变化, 增加元素, 删除元素),
        #                                           node.forward 也会同步变化, 因为这两个变量名共同引用同一个(内存)对象.
        #
        # 第二种: forwards        = node.forward.copy()
        #        id(forwards)    != id(node.forward)
        #        id(forwards[0]) == id(node.forward[0])
        #        forwards 元素引用 node.forward, 即: forwards 的元素属性发生变化, node.forward 也会同步变化, 因为两个list共同引用元素对象.
        #                                           forwards 增加元素, node.forward 不会同步增加元素.
        #                                           forwards 删除元素, node.forward 不会同步删除元素, 因为这只是针对元素减少一次引用.
        #
        # 第三种: forwards = copy.deepcopy(node.forward)
        #        id(forwards)    != id(node.forward)
        #        id(forwards[0]) != id(node.forward[0])
        #        forwards 完全独立于 node.forward.
        forwards = node.forward.copy()
        lines.append(f"[{node.key}]".ljust(label_size, "-") + "* " * len(forwards))         # [root]--* * * * * * *
        lines.append(" " * label_size + "| " * len(forwards))                               #         | | | | | | |

        # 虽然 node.forward 有一层含义是 level, 但是这里关注的不是level,
        # 当 len(node.forward) == 0 时, 表示是链表的最末端节点.
        while len(node.forward) != 0:

            # node.forward[0] -> node.forward[0] -> node.forard[0] -> node.forard[0] ...
            # 切换到链表的下一个节点.
            #
            # 容易混淆的地方:
            # node == self.head, 虽然是完全引用, 当node发生变化时, self.head也会变化, 因为这两个变量名共同引用同一个(内存)对象.
            # 但是这里 node = node.forward[0]; 并不会影响 self.head 对象, 因为变量的覆盖只是让 self.head 引用的内存对象减少一个引用而已.
            node = node.forward[0]

            lines.append(
                f"[{node.key}]".ljust(label_size, "-") +                                  # 重点
                " ".join(str(n.key) if n.key == node.key else "|" for n in forwards)      # [1]-----1 | | | | | |
            )
            lines.append(" " * label_size + "| " * len(forwards))                         #         | | | | | | |

            # forwards 采用的是元素引用, 即: 只要元素的属性不变更.
            # forwards 的新增元素, 插入元素, 删除元素, 都不会影响上面的 node.forward.
            #
            # forwards 这个列表有几个元素, 取决于SkipList.level的层级.
            # forwards 是一个算法集合, 它通过高精度排列而成.
            #
            # forwards 从外部视角看, 即: SkipList.head.forward
            #          它的存储规则是: 最后一个元素是抛硬币连续递增1得出最大层级的那个数字.
            #
            forwards[: node.level] = node.forward

        lines.append("None".ljust(label_size) + "* " * len(forwards))
        return f"SkipList(level={self.level})\n" + "\n".join(lines)                         # None    * * * * * * *

    def __iter__(self):
        node = self.head

        # 从 self.head。forward 中的第0个元素中一直去到末端.
        while len(node.forward) != 0:
            yield node.forward[0].key
            node = node.forward[0]

    def random_level(self) -> int:
        """
        随机算法:
        1. random()返回的随机数: 0.56, 0.17, 0.68, 0.45, ...
        2. self.p: 0.5
        3. random() < self.p == 随机数 < 0.5, 即: 小于0.5, 相当于是扔硬币的概率, 百分之五十.
        4. 只要扔出来的硬币小于 0.5, 则 level 递增 1; 直到扔出来的硬币大于 0.5 则退出当前定级函数.

        TODO: 如何保证每个level的链表不超过该链表应有长度?            思路: 插入时, 增加一个边界条件.
        TODO: 如何保证每个level的链表都是按照理想的间隔位置排列?      思路: 插入时, 增加一个求模条件.
        """
        level = 1
        while random() < self.p and level < self.max_level:
            level += 1

        return level

    def _locate_node(self, key) -> tuple[Optional[Node[KT, VT]], list[Node[KT, VT]]]:
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
        # 根据提供的 key 查找跳表:
        #
        # node:           当从跳表中查找到节点数据时, node 就是该数据节点.
        #                 当从跳表中没有查找到节点数据时, node is None.
        #
        # update_vector:
        node, update_vector = self._locate_node(key)

        # 当 node is not None 时, 表示有重复 key, 这里采取覆盖的形式, 即: 不支持多个相同key存在.
        if node is not None:
            node.value = value

        # 当 node is None 时, 构建跳表结构.
        else:

            #
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
        node, _ = self._locate_node(key)

        if node is not None:
            return node.value

        return None


def test_insert():
    skip_list = SkipList()
    skip_list.insert("Key1", 3)
    skip_list.insert("Key2", 12)
    skip_list.insert("Key3", 41)
    skip_list.insert("Key4", -19)

    node = skip_list.head
    all_values = {}
    while node.level != 0:
        node = node.forward[0]
        all_values[node.key] = node.value

    assert len(all_values) == 4
    assert all_values["Key1"] == 3
    assert all_values["Key2"] == 12
    assert all_values["Key3"] == 41
    assert all_values["Key4"] == -19


def test_insert_overrides_existing_value():
    skip_list = SkipList()
    skip_list.insert("Key1", 10)
    skip_list.insert("Key1", 12)

    skip_list.insert("Key5", 7)
    skip_list.insert("Key7", 10)
    skip_list.insert("Key10", 5)

    skip_list.insert("Key7", 7)
    skip_list.insert("Key5", 5)
    skip_list.insert("Key10", 10)

    node = skip_list.head
    all_values = {}
    while node.level != 0:
        node = node.forward[0]
        all_values[node.key] = node.value

    if len(all_values) != 4:
        print()
    assert len(all_values) == 4
    assert all_values["Key1"] == 12
    assert all_values["Key7"] == 7
    assert all_values["Key5"] == 5
    assert all_values["Key10"] == 10


def test_searching_empty_list_returns_none():
    skip_list = SkipList()
    assert skip_list.find("Some key") is None


def test_search():
    skip_list = SkipList()

    skip_list.insert("Key2", 20)
    assert skip_list.find("Key2") == 20

    skip_list.insert("Some Key", 10)
    skip_list.insert("Key2", 8)
    skip_list.insert("V", 13)

    assert skip_list.find("Y") is None
    assert skip_list.find("Key2") == 8
    assert skip_list.find("Some Key") == 10
    assert skip_list.find("V") == 13


def test_deleting_item_from_empty_list_do_nothing():
    skip_list = SkipList()
    skip_list.delete("Some key")

    assert len(skip_list.head.forward) == 0


def test_deleted_items_are_not_founded_by_find_method():
    skip_list = SkipList()

    skip_list.insert("Key1", 12)
    skip_list.insert("V", 13)
    skip_list.insert("X", 14)
    skip_list.insert("Key2", 15)

    skip_list.delete("V")
    skip_list.delete("Key2")

    assert skip_list.find("V") is None
    assert skip_list.find("Key2") is None


def test_delete_removes_only_given_key():
    skip_list = SkipList()

    skip_list.insert("Key1", 12)
    skip_list.insert("V", 13)
    skip_list.insert("X", 14)
    skip_list.insert("Key2", 15)

    skip_list.delete("V")
    assert skip_list.find("V") is None
    assert skip_list.find("X") == 14
    assert skip_list.find("Key1") == 12
    assert skip_list.find("Key2") == 15

    skip_list.delete("X")
    assert skip_list.find("V") is None
    assert skip_list.find("X") is None
    assert skip_list.find("Key1") == 12
    assert skip_list.find("Key2") == 15

    skip_list.delete("Key1")
    assert skip_list.find("V") is None
    assert skip_list.find("X") is None
    assert skip_list.find("Key1") is None
    assert skip_list.find("Key2") == 15

    skip_list.delete("Key2")
    assert skip_list.find("V") is None
    assert skip_list.find("X") is None
    assert skip_list.find("Key1") is None
    assert skip_list.find("Key2") is None


def test_delete_doesnt_leave_dead_nodes():
    skip_list = SkipList()

    skip_list.insert("Key1", 12)
    skip_list.insert("V", 13)
    skip_list.insert("X", 142)
    skip_list.insert("Key2", 15)

    skip_list.delete("X")

    def traverse_keys(node):
        yield node.key
        for forward_node in node.forward:
            yield from traverse_keys(forward_node)

    assert len(set(traverse_keys(skip_list.head))) == 4


def test_iter_always_yields_sorted_values():
    def is_sorted(lst):
        for item, next_item in zip(lst, lst[1:]):
            if next_item < item:
                return False
        return True

    skip_list = SkipList()
    for i in range(10):
        skip_list.insert(i, i)
    assert is_sorted(list(skip_list))
    skip_list.delete(5)
    skip_list.delete(8)
    skip_list.delete(2)
    assert is_sorted(list(skip_list))
    skip_list.insert(-12, -12)
    skip_list.insert(77, 77)
    assert is_sorted(list(skip_list))


def pytests():
    for i in range(100):
        # Repeat test 100 times due to the probabilistic nature of skip list
        # random values == random bugs
        test_insert()
        test_insert_overrides_existing_value()

        test_searching_empty_list_returns_none()
        test_search()

        test_deleting_item_from_empty_list_do_nothing()
        test_deleted_items_are_not_founded_by_find_method()
        test_delete_removes_only_given_key()
        test_delete_doesnt_leave_dead_nodes()

        test_iter_always_yields_sorted_values()


def main():
    skip_list = SkipList()
    skip_list.insert(1, "2")
    skip_list.insert(2, "2")
    skip_list.insert(3, "4")
    skip_list.insert(4, "4")
    skip_list.insert(5, "5")
    skip_list.insert(6, "4")
    skip_list.insert(7, "5")
    skip_list.insert(8, "4")
    skip_list.insert(9, "4")

    print(skip_list)
    print(skip_list)


if __name__ == "__main__":
    main()
