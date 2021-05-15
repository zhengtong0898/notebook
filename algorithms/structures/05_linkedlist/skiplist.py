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
        return f"<Node key={self.key} value={self.value} level={self.level} at {hex(id(self))}>"

    @property
    def level(self) -> int:
        """
        level 表示的是链表层级总数.


        样本 level = 4
        结构
                    7                                                         SkipList.head.forward[3] == <Node key=7>
          2 3     6 7                                                         SkipList.head.forward[2] == <Node key=2>
          2 3     6 7 8                                                       SkipList.head.forward[1] == <Node key=2>
        1 2 3 4 5 6 7 8 9                                                     SkipList.head.forward[0] == <Node key=1>
              Root                                                            SkipList.head

        链表结构
        SkipList.head            ==                                           Node
        SkipList.head.forward    ==                                           Node.forward

        SkipList.head.forward[0]                                              第一层链表第0个节点(最左节点)  <Node key=1>
        SkipList.head.forward[0].forward[0]                                   第一层链表第1个节点           <Node Key=2>
        SkipList.head.forward[0].forward[0].forward[0]                        第一层链表第2个节点           <Node Key=3>
        SkipList.head.forward[0].forward[0].forward[0].forward[0]             第一层链表第3个节点           <Node key=4>
        SkipList.head.forward[0].forward[0].forward[0].forward[0]
                     .forward[0].forward[0].forward[0].forward[0].forward[0]  以此类推到最后一个节点是       <Node key=9>


        SkipList.head.forward[1]                                              第二层链表第0个节点(最左节点)  <Node key=2>
        SkipList.head.forward[1].forward[1]                                   第二层链表第1个节点           <Node key=3>
        SkipList.head.forward[1].forward[1].forward[1]                        第二层链表第2个节点           <Node key=6>
        SkipList.head.forward[1].forward[1].forward[1].forward[1]             第二层链表第3个节点           <Node key=7>
        SkipList.head.forward[1].forward[1].forward[1].forward[1].forward[1]  第二层链表第4个节点(最右节点)  <Node key=8>


        SkipList.head.forward[2]                                              第三层链表第0个节点(最左节点)  <Node key=2>
        SkipList.head.forward[2].forward[0]                                   第三层链表第1个节点           <Node key=3>
        SkipList.head.forward[2].forward[0].forward[0]                        第三层链表第2个节点           <Node key=6>
        SkipList.head.forward[2].forward[0].forward[0].forward[0]             第三层链表第3个节点(最右节点)  <Node key=7>


        SkipList.head.forward[3]                                              第四层链表第0个节点(最左节点)  <Node key=7>





        样本 level = 5
        结构
        1                                                                     SkipList.head.forward[4] == <Node key=1>
        1 2                                                                   SkipList.head.forward[3] == <Node key=1>
        1 2   4   6 7                                                         SkipList.head.forward[2] == <Node key=1>
        1 2 3 4   6 7 8                                                       SkipList.head.forward[1] == <Node key=1>
        1 2 3 4 5 6 7 8 9                                                     SkipList.head.forward[0] == <Node key=1>
              Root                                                            SkipList.head

        链表结构
        SkipList.head            ==                                           Node
        SkipList.head.forward    ==                                           Node.forward

        SkipList.head.forward[0]                                              第一层链表第0个节点(最左节点)  <Node key=1>
        SkipList.head.forward[0].forward[0]                                   第一层链表第1个节点           <Node Key=2>
        SkipList.head.forward[0].forward[0].forward[0]                        第一层链表第2个节点           <Node Key=3>
        SkipList.head.forward[0].forward[0].forward[0].forward[0]             第一层链表第3个节点           <Node key=4>
        SkipList.head.forward[0].forward[0].forward[0].forward[0]
                     .forward[0].forward[0].forward[0].forward[0]
                     .forward[0]                                              以此类推到最后一个节点是       <Node key=9>


        SkipList.head.forward[1]                                              第二层链表第0个节点(最左节点)  <Node key=1>
        SkipList.head.forward[1].forward[1]                                   第二层链表第1个节点           <Node key=2>
        SkipList.head.forward[1].forward[1].forward[1]                        第二层链表第2个节点           <Node key=3>
        SkipList.head.forward[1].forward[1].forward[1].forward[1]             第二层链表第3个节点           <Node key=4>
        SkipList.head.forward[1].forward[1].forward[1].forward[1].forward[1]  第二层链表第4个节点           <Node key=6>
        SkipList.head.forward[1].forward[1].forward[1].forward[1].forward[1]
                     .forward[1]                                              第二层链表第5个节点           <Node key=7>
        SkipList.head.forward[1].forward[1].forward[1].forward[1].forward[1]
                     .forward[1].forward[1]                                   第二层链表第6个节点(最右节点)  <Node key=8>


        SkipList.head.forward[2]                                              第三层链表第0个节点(最左节点)  <Node key=1>
        SkipList.head.forward[2].forward[2]                                   第三层链表第1个节点           <Node key=2>
        SkipList.head.forward[2].forward[2].forward[2]                        第三层链表第2个节点           <Node key=4>
        SkipList.head.forward[2].forward[2].forward[2].forward[2]             第三层链表第3个节点           <Node key=6>
        SkipList.head.forward[2].forward[2].forward[2].forward[2].forward[2]  第三层链表第4个节点(最右节点)  <Node key=7>


        SkipList.head.forward[3]                                              第四层链表第0个节点(最左节点)  <Node key=1>
        SkipList.head.forward[3].forward[3]                                   第四层链表第1个节点(最右节点)  <Node key=2>


        SkipList.head.forward[4]                                              第四层链表第0个节点           <Node key=1>
        """
        return len(self.forward)


class SkipList(Generic[KT, VT]):

    def __init__(self, p: float = 0.5, max_level: int = 16):
        self.head = Node("root", None)           # 根节点
        self.level = 0                           # 跳表层级
        self.p = p                               # 硬币概率: 0.5 == 50%
        self.max_level = max_level               # 限定最大层级; 关于层级和节点数量关系的思考, 参考 skiplist_utils.py 文件.

    def __str__(self) -> str:
        # 从 self.head.forward 中的第0个元素中一直去到末端.
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

        自问自答:
        这是一个理想状态下的跳表的间隔和层高.                                 被称为平衡树结构.
        1       5       9
        1   3   5   7   9
        1 2 3 4 5 6 7 8 9
             样本-1

        由于跳表采用的是 random_level 来确定一个节点的层高,
        实际上的相同链表节点每次生成的结果是不一样的.                          被称为随机概率树结构.
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
        """
        这是一个根据 参数key 查找 node.key 的函数,
        当匹配到   参数key 相同的 node 节点时, node是一个有效对象.
        当未匹配到 参数key 相同的 node 节点时, node是一个 None 对象.

        查找的过程中无论是否匹配到 参数key, 都会维护一个完整的 update_vector,
        update_vector 是一个列表集合,
        update_vector 列表的长度代表着链表的层级高度,
        update_vector 第0个元素表示, 第一层链表最接近或等于参数key的节点,
        update_vector 第1个元素表示, 第二层链表最接近或等于参数key的节点,
        update_vector 第2个元素表示, 第三层链表最接近或等于参数key的节点.

        返回值: node, update_vector 或 None, update_vector
        """

        # 列表的长度对标层级, 比如说: 有三个元素, 则表示有三个层级.
        # 每个层级都是最接近或等于 参数key 的node节点.
        update_vector = []

        # self.head 是 root 节点, 它是跳表的入口, 不属于任何层级.
        # node 在这里是完全引用 self.head.
        node = self.head

        # 从最高一层的链表的最右节点开始遍历跳表.
        for i in reversed(range(self.level)):

            while True:

                # 无效索引, 下沉一级, 再进行下一次比较.
                index_invalid = i >= node.level
                if index_invalid:
                    break

                # 当 rightmost_node.key >= key 时, 下沉一级, 再进行下一次比较.            关键字: 下沉
                rightmost_node = node.forward[i]
                if rightmost_node.key >= key:
                    break

                # 当 rightmost_node.key < key 时, 保持在同一层级,
                # rightmost_node向左移一个节点, 再进行下一次比较.                         关键字: 左移
                node = rightmost_node

            # 每次下沉之前, 都需要将 node 添加到 update_vector.
            # 当 rightmost_node.key 大于或等于 参数key 时, 该 rightmost_node 一定是同层级内最右节点.
            # 当 rightmost_node.key 小于      参数key 时, 该 rightmost_node 一定是同层级内最接近 参数key 的节点.(左边最靠右)
            update_vector.append(node)

        # 由于 update_vector 的元素是从高层级到低层级匹配,
        # 所以现在要将结果反转回正序(即: 反转回从低层级到高层级).
        update_vector.reverse()

        # 当 len(node.forward) == 0 时, node是第1层链表的最右节点, 因为没有下一个节点了.
        # 由于这里采取前置匹配, 当 node.forward 为空时, 无法做前置匹配, 所以
        node_notexist = len(node.forward) == 0
        if node_notexist:
            return None, update_vector

        # 当 len(node.forward) != 0 时, node是第1层链表, 但不是最右节点.
        # 当 node.forward[0].key != 参数key 时, 则表示匹配没有命中.
        nodekey_notequal = node.forward[0].key != key
        if nodekey_notequal:
            return None, update_vector

        # 当 len(node.forward) != 0 时, node是第1层链表, 但不是最右节点.
        # 当 node.forward[0].key == 参数key 时, 则表示匹配命中.
        return node.forward[0], update_vector

    def delete(self, key: KT):
        node, update_vector = self._locate_node(key)

        if node is None:
            return

        # node 匹配命中, 即: node.key == 参数key
        # node.forward[0] == 第 1 层链表中的下一个元素.
        # node.forward[1] == 第 2 层链表中的下一个元素.
        # node.forward[2] == 第 3 层链表中的下一个元素.
        # node.forward[3] == 第 4 层链表中的下一个元素.
        # 以此类推.
        for i, update_node in enumerate(update_vector):
            # 当 i = 0 时, 表示当前是要做第1层链表的匹配工作.
            # 当 i = 1 时, 表示当前是要做第2层链表的匹配工作.
            # 以此类推.
            index_invalid = update_node.level <= i
            if index_invalid:
                continue

            if update_node.forward[i].key != key:
                continue

            rightmost_node = node.level <= i
            if not rightmost_node:
                # update_node.forward[i]     == node
                # update_node.forward[i].key == node.key == key
                # 因此 node.forward[i] 是 node 和 update_node.forward[i] 的下一个节点.
                # 因此 update_node.forward[i] = node.forward[i] 等同于 node = node.forward[i].
                # 具体的意思是:
                # 当 node 不是最右节点时, 将下一个节点覆盖掉当前节点, 目的时起到删除作用.
                update_node.forward[i] = node.forward[i]

            # else 等同于 rightmost_node == True
            else:
                #   2
                # 1 2   4 5
                # 1 2 3 4 5   7 
                # 1 2 3 4 5 6 7 8 9
                # 假设 i == 1, key == 7;
                # update_node         ==  <Node key=5 value='' level=2>
                # update_node.forward == [<Node key=6 value='' level=1>,        第 0 层级链表的下一个节点
                #                         <Node key=7 value='' level=1>]        第 1 层级链表的下一个节点
                #
                # update_node.forward[:1] == [<Node key=6 value='' level=1>]    即: 移除了第 1 层级链表的下一个节点.
                # 具体的意思是:
                # 当 node 是最右节点时, 从 update_node.forward 中移除掉 == node 的那个节点.
                update_node.forward = update_node.forward[:i]

    def insert(self, key: KT, value: VT):
        # 根据提供的 key 查找跳表:
        #
        # node:           当从跳表中查找到节点数据时, node 就是该数据节点.
        #                 当从跳表中没有查找到节点数据时, node is None.
        #
        # update_vector:  这是一个层级集合, 比如说:
        #                 update_vector[0] 表示跳表的第1层的链表, 是同层级内最接近 参数key 的节点.
        #                 update_vector[1] 表示跳表的第2层的链表, 是同层级内最接近 参数key 的节点.
        #                 update_vector[2] 表示跳表的第3层的链表, 是同层级内最接近 参数key 的节点, 以此类推...
        node, update_vector = self._locate_node(key)

        # 表示有重复 key, 这里采取覆盖的形式, 即: 不支持多个相同key存在.
        if node is not None:
            node.value = value

        # 当 node is None 时, 构建跳表结构.
        else:

            # 随机获取一个层级.
            level = self.random_level()

            # 当随机层级 高于 当前最高层级时.
            # 将 update_vector 的元素数量填充至 level + 1 高度,
            # TODO: 为什么这里 + 1.
            # FIXED: 移除掉也没有问题, 因为下面代码中并没有使用到 + 1 的特性.
            if level > self.level:
                # After level increase we have to add additional nodes to head.
                for i in range(self.level, level):
                    update_vector.append(self.head)
                self.level = level

            new_node = Node(key, value)

            for i, update_node in enumerate(update_vector[:level]):
                # i, update_node 层级强一致;
                #
                # 当 i=0 时, update_node=第1层级;
                # 当 i=1 时, update_node=第2层级;
                # 当 i=2 时, update_node=第3层级;
                #
                # 当 update_node.key >= 参数key 时, update_node 一定是该层级最右节点.
                #
                # 当 update_node.level > i 意味着 update_node 不是最右节点(右侧还有节点),
                #                         间接意味着 update_node.key 小于 参数key,
                #                         因此, 这里需要将右侧节点截断, 重新指向到 new_node,
                #                         然后将 new_node 放在 update_node 的右侧,
                #                         通过这种方式完成一个节点的有序插入.
                if update_node.level > i:
                    nextone_node = update_node.forward[i]
                    new_node.forward.append(nextone_node)
                    update_node.forward[i] = new_node

                # 当 update_node.level <= i 时, 等同于 else, 意味着 update_node 是最右节点(右侧没有节点了).
                #                               因此将 new_node 放在 update_node 的右侧.
                else:
                    update_node.forward.append(new_node)

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
    pytests()
    skip_list = SkipList()
    skip_list.insert(1, "2")
    skip_list.insert(2, "2")
    skip_list.insert(3, "4")
    skip_list.insert(4, "4")
    skip_list.insert(5, "5")
    skip_list.insert(6, "4")
    skip_list.insert(7, "5")
    skip_list.insert(8, "4")

    print(skip_list)
    skip_list.insert(9, "4")

    key = input("find key: ")
    skip_list.delete(int(key))


if __name__ == "__main__":
    main()
