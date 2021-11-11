#给定一个单链表的头结点pHead，长度为n，反转该链表后，返回新链表的表头。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 
# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#
class Solution:
        def ReverseList(self , head: ListNode) -> ListNode:
            if head==None: return head
            node = head
            pre = None

            while node!=None:
                next=node.next
                node.next=pre
                pre=node
                node=next

            return pre