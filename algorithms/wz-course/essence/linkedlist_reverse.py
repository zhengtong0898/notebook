from typing import List


class ListNode:

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"{self.walk()}"

    def walk(self) -> List[int]:
        result = []
        curr_node = self
        while curr_node:
            result.append(curr_node.val)
            curr_node = curr_node.next
        return result


def reverse(head: ListNode) -> ListNode:
    """
    做完整链表反转, 必须增加一个 外部节点(这里是 prev_node)来截断 head 节点.
    做部分链表反转, 可以不需要增加外部节点完成, 例如: 0025-reverse-k-group.py
    """
    prev_node = None
    curr_node = head
    while curr_node:                                                  # 时间复杂度: O(n), 空间复杂度: O(1)
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


def reverse_v2(head: ListNode) -> ListNode:
    reverse_node = ListNode()
    curr_node = head
    while curr_node:                                                  # 时间复杂度: O(n)
        next_node = curr_node.next
        curr_node.next = None                        # 截断 head
        curr_node.next = reverse_node.next           # 反向拼接
        reverse_node = ListNode(next_=curr_node)     # 反向添加        # 空间复杂度: O(n)
        curr_node = next_node
    return reverse_node.next


def reverse_v3(head: ListNode) -> ListNode:
    """
    链表的禁忌

    当链表不慎指向到自己时, 会产生环引用.
    环引用会导致进程将内存全部打满最终被操作系统oom-kill.
    """
    prev_node = head
    curr_node = head
    while curr_node:                                                  # 时间复杂度: O(n), 空间复杂度: O(1)
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node


def main():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next = ListNode(val=5)
    assert reverse_v3(ln_10).walk() == [5, 4, 3, 2, 1]


if __name__ == '__main__':
    main()
