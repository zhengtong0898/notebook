import sys
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    # def __str__(self):
    #     return f"{self.walk()}"

    def __str__(self):
        return f"<ListNode val={self.val}>"

    def __repr__(self):
        return self.__str__()

    def walk(self) -> List[int]:
        result = []
        curr_node = self
        while curr_node:
            result.append(curr_node.val)
            curr_node = curr_node.next
        return result


class Solution:

    """
    141. 环形链表

    给定一个链表，判断链表中是否有环。

    如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
    如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

    如果链表中存在环，则返回 true 。 否则，返回 false 。

    进阶：
    你能用 O(1)（即，常量）内存解决此问题吗？

    示例-1:
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

    示例-2:
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。

    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/linked-list-cycle
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def hasCycle(self, head: ListNode) -> bool:
        """
        快慢指针
        如果是环形链表，那么它们两总归会相遇.
        慢指针初始在头节点, 快指针初始在头节点的下一个节点.
        慢指针每次走一步,  快指针每次走两步
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:                             # 空间复杂度: O(1), 时间复杂度: O(n)
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    def hasCycle_refcount(self, head: ListNode) -> bool:
        """
        为什么是大于4则表示是环链表?

        1 ref comes from the calling of this function itself according to the documentation
        2 Refs from the object being created, compiled and stored for optimization
        1 ref from a node A's next
        1 ref comes from another node B's next [if this happens, then there is a cycle]
        """
        while head:                                             # 空间复杂度: O(1), 时间复杂度: O(n)
            if sys.getrefcount(head) > 4: return True
            head = head.next
        return False

    def hasCycle_dict(self, head: ListNode) -> bool:
        caches = {}                                             # 空间复杂度: O(n)
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = None
            if caches.get(curr): return True                    # 时间复杂度: O(1)
            caches[curr] = 1
            curr = curr_next

        return False

    def hasCycle_list(self, head: ListNode) -> bool:
        """
        1. 遍历链表
        2. 将每个节点添加到 caches.
        3. 每次遍历都需要做一次 in 比较.
        4. 当链表节点已存在 caches 则表示是一个环链表.
        """
        caches = []                                             # 空间复杂度: O(n)
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = None
            if curr in caches: return True                      # # 时间复杂度: O(n^2)
            caches.append(curr)
            curr = curr_next

        return False


def test_1():
    l10 = ListNode(val=3)
    l10.next = ListNode(val=2)
    l10.next.next = ListNode(val=0)
    l10.next.next.next = ListNode(val=-4)
    l10.next.next.next.next = l10.next

    ss = Solution().hasCycle(l10)
    assert ss is True


def main():
    test_1()


if __name__ == '__main__':
    main()
