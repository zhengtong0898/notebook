# 双向循环链表
# 可以从头节点的 previous 指针直达尾节点,
# 也可以从尾节点的 next 指针直达头节点.


class ListNode:

    def __init__(self, val=0, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_
