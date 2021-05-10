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
        return f"<Node key={self.key} value={self.value} forward_size={self.forward_size} at {hex(id(self))}>"

    @property
    def forward_size(self) -> int:
        """ 这里仅表示 forward 列表中有几个Node对象, 并不是表示当前Node属于哪个链表层级. """
        return len(self.forward)


class SkipList(Generic[KT, VT]):
    def __init__(self, p: float = 0.5, max_level: int = 16):
        self.head = Node("root", None)           # 根节点
        self.level = 0                           # 跳表层级
        self.p = p                               # 硬币概率: 0.5 == 50%

        # 默认情况下, 最大层级: 16
        # pow(2, 16) = 65536, 即: max_level = 16 的情况下, 当前 SkipList 允许最多存储 65536 个节点.
        # math.log2(65536) = 16; 通过节点数量逆运算出理想的层高.
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
            forwards[: node.forward_size] = node.forward

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

        自问自答:
        这是一个理想状态下的跳表的间隔和层高.
        1       5       9
        1   3   5   7   9
        1 2 3 4 5 6 7 8 9
             样本-1

        由于跳表采用的是 random_level 来确定一个节点的层高,
        实际上的相同链表节点每次生成的结果是不一样的.
                  6
                5 6
                5 6 7
          2     5 6 7
        1 2 3 4 5 6 7 8 9
             样本-2

        在不采用跳表的情况下, 有序链表找到 8 需要查找 8 次, 即: O(n).
        在采用跳表的情况下, 最差情况下, 每次随机层高定级都是1, 那么查找到 8 也是需要查找 8 次, 即: O(n).
        在采用跳表的情况下, 理想情况下, 排列像样本-1, 那么查找到 8 需要查找 3 次, 即: O(logn).
        在采用跳表的情况下, 一般情况下, 排列像样本-2, 那么查找到 8 需要查找 4 次, 即: O(logn).
        """
        level = 1
        while random() < self.p and level < self.max_level:
            level += 1

        return level

    def _locate_node(self, key) -> tuple[Optional[Node[KT, VT]], list[Node[KT, VT]]]:
        update_vector = []

        node = self.head

        # reversed(range(self.level)): 从最高层级的链表的右侧开始查找.
        for i in reversed(range(self.level)):
            while True:
                # 当最高层级的索引 >= node.forward_size 数量时, 表示不能比较 key 对象.
                index_invalid = i >= node.forward_size
                if index_invalid:
                    break

                # 当前层级最大的节点的 key 小于 参数key.
                rightmost_node = node.forward[i]
                if rightmost_node.key < key:
                    node = rightmost_node

            # 将每个层级链表最右侧的节点, 并小于 key 的节点, 添加到 update_vector 中.
            # SkipList的层级有多高, update_vector 就有多少个元素.
            update_vector.append(node)

        # 由于 update_vector 的元素是反向匹配, 所以现在要反转回正序.
        update_vector.reverse()

        # key 匹配未命中.
        node_not_exist = len(node.forward) == 0
        if node_not_exist:
            return None, update_vector

        # key 匹配命中.
        if node.forward[0].key == key:
            return node.forward[0], update_vector

    def delete(self, key: KT):
        node, update_vector = self._locate_node(key)

        if node is not None:
            for i, update_node in enumerate(update_vector):
                # Remove or replace all references to removed node.
                if update_node.forward_size > i and update_node.forward[i].key == key:
                    if node.forward_size > i:
                        update_node.forward[i] = node.forward[i]
                    else:
                        update_node.forward = update_node.forward[:i]

    def insert(self, key: KT, value: VT):
        # 根据提供的 key 查找跳表:
        #
        # node:           当从跳表中查找到节点数据时, node 就是该数据节点.
        #                 当从跳表中没有查找到节点数据时, node is None.
        #
        # update_vector:  TODO: 这里查找的是 key 的层级?
        #                       如果 key 存在的话, update_vector 是该 key 所在层级的链表?
        #                       如果 key 不存在的话, update_vector 是什么?
        node, update_vector = self._locate_node(key)

        # 当 node is not None 时, 表示有重复 key, 这里采取覆盖的形式, 即: 不支持多个相同key存在.
        if node is not None:
            node.value = value

        # 当 node is None 时, 构建跳表结构.
        else:

            # 随机获取一个层级.
            level = self.random_level()

            # 当随机层级 高于 当前最高层级时.
            # 将 update_vector 的元素数量填充至 level + 1 高度, TODO: 为什么这里 + 1.
            if level > self.level:
                # After level increase we have to add additional nodes to head.
                for i in range(self.level - 1, level):
                    update_vector.append(self.head)
                self.level = level

            new_node = Node(key, value)

            for i, update_node in enumerate(update_vector[:level]):
                # Change references to pass through new node.
                if update_node.forward_size > i:
                    new_node.forward.append(update_node.forward[i])

                # 这里的 if else 试图构建一个有序的链表结构, TODO: 待确认.
                if update_node.forward_size < i + 1:
                    update_node.forward.append(new_node)
                #
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
    while node.forward_size != 0:
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
    while node.forward_size != 0:
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
    test_insert()
    test_insert_overrides_existing_value()

    test_searching_empty_list_returns_none()
    test_search()

    test_deleting_item_from_empty_list_do_nothing()
    test_deleted_items_are_not_founded_by_find_method()
    test_delete_removes_only_given_key()
    test_delete_doesnt_leave_dead_nodes()

    test_iter_always_yields_sorted_values()
    # skip_list = SkipList()
    # skip_list.insert(1, "2")
    # skip_list.insert(2, "2")
    # skip_list.insert(3, "4")
    # skip_list.insert(4, "4")
    # skip_list.insert(5, "5")
    #
    # print(skip_list)
    #
    # skip_list.insert(6, "4")
    # skip_list.insert(7, "5")
    # skip_list.insert(8, "4")
    # skip_list.insert(9, "4")
    #
    # print(skip_list)
    # print(skip_list)


if __name__ == "__main__":
    main()
