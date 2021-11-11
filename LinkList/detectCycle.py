# 对于一个给定的链表，返回环的入口节点，如果没有环，返回null
# 拓展：
# 你能给出不利用额外空间的解法么？
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def detectCycle(self , head ):
        # write code here
        if (not head) or (not head.next) or (not head.next.next):
            return None
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                fast=head
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None