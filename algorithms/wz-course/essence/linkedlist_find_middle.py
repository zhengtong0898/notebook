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


def middle_node(head: ListNode) -> ListNode:
    """
    快慢指针可有效的用于查找链表的中间节点

    遍历三要素

    指针初始值:      slow = head; fast = head;           # 在同一个赛道上;
    遍历的结束条件:   fast is None or                     # 当链表数量是奇数时(触发 fast.next = None),
                    fast.next is None                   # 当链表数量是偶数时(触发 faster = None)
    遍历的核心逻辑:   slow = slow.next
                    fast = fast.next.next
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def main():
    ln_10 = ListNode(val=1)
    ln_10.next = ListNode(val=2)
    ln_10.next.next = ListNode(val=3)
    ln_10.next.next.next = ListNode(val=4)
    ln_10.next.next.next.next = ListNode(val=5)
    assert ln_10.walk() == [1, 2, 3, 4, 5]
    ss = middle_node(ln_10)
    xx = ss.walk()
    assert xx == [3, 4, 5]


if __name__ == '__main__':
    main()
