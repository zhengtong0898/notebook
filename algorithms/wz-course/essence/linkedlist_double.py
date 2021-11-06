# 双向链表
# 每个节点都有两个指针: previous, next
# 每个节点都可以找到相邻节点，而不是重新遍历.


class ListNode:

    def __init__(self, val=0, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_
