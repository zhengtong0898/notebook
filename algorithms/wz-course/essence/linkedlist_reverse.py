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
    将链表反向排序

    特别注意:
    慎重使用 None 来截断链表, 因为这会导致所有引用节点都会同步这个截断操作,
    比如说下面的 curr_node = head 这个赋值操作，其实就是对 head 多增加一个引用,
    当触发下面的 curr_node.next = None 时, curr_node 和 head 会同时被截断.
    """
    reverse_node = ListNode()
    curr_node = head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = None                        # 截断 head
        curr_node.next = reverse_node.next           # 反向拼接
        reverse_node = ListNode(next_=curr_node)     # 反向添加
        curr_node = next_node
    return reverse_node.next


def main():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next = ListNode(val=5)
    assert reverse(ln_10).walk() == [5, 4, 3, 2, 1]


if __name__ == '__main__':
    main()
